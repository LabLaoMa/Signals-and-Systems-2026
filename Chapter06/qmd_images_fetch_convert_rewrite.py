import re
import os
import hashlib
import mimetypes
from pathlib import Path
from urllib.parse import urlparse, unquote

import requests
from PIL import Image


# ================== 配置区 ==================
QMD_PATH = Path("Chapter06.qmd")  # 你的 qmd 文件
OUT_DIR = Path("imglink")            # 下载目录
REWRITE_QMD = True               # 是否把远程链接改成本地链接
KEEP_JPG = True                  # 是否保留原始 jpg（你要求不删，所以 True）
TIMEOUT = 60
# ===========================================

# 提取规则：Markdown 图片、HTML img、CSS background-image/url(...)
PATTERNS = [
    r'!\[[^\]]*\]\(\s*(https?://[^)\s]+)',                        # ![](...)
    r'<img[^>]+src=["\'](https?://[^"\']+)["\']',                 # <img src="">
    r'background-image\s*:\s*url\(\s*["\']?(https?://[^)"\']+)["\']?\s*\)',
    r'url\(\s*["\']?(https?://[^)"\']+)["\']?\s*\)',
]

def _sha16(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()[:16]

def ensure_unique_path(path: Path) -> Path:
    if not path.exists():
        return path
    stem, suffix = path.stem, path.suffix
    for i in range(2, 9999):
        p = path.with_name(f"{stem}_{i}{suffix}")
        if not p.exists():
            return p
    raise RuntimeError(f"Too many duplicates for {path}")

def filename_from_url(url: str) -> str:
    """尽量从 URL 取得文件名；没有就用 hash.bin 占位"""
    parsed = urlparse(url)
    name = Path(unquote(parsed.path)).name
    if not name or "." not in name:
        name = f"{_sha16(url)}.bin"
    # 去掉奇怪的 query-like suffix（极少数站点会把扩展名放 query）
    name = name.split("?")[0].split("#")[0]
    return name

def guess_ext_from_content_type(content_type: str) -> str:
    ctype = (content_type or "").split(";")[0].strip().lower()
    if not ctype:
        return ""
    ext = mimetypes.guess_extension(ctype) or ""
    # 某些情况下 .jpe -> .jpg
    if ext == ".jpe":
        ext = ".jpg"
    return ext

def download_url(url: str, out_dir: Path) -> Path | None:
    out_dir.mkdir(parents=True, exist_ok=True)
    base_name = filename_from_url(url)
    target = ensure_unique_path(out_dir / base_name)

    try:
        r = requests.get(url, stream=True, timeout=TIMEOUT, headers={"User-Agent": "Mozilla/5.0"})
        r.raise_for_status()

        # 如果是 .bin 或没有扩展名，尝试根据 Content-Type 补扩展名
        if target.suffix in {".bin", ""}:
            ext = guess_ext_from_content_type(r.headers.get("Content-Type", ""))
            if ext:
                target = ensure_unique_path(target.with_suffix(ext))

        with open(target, "wb") as f:
            for chunk in r.iter_content(chunk_size=1024 * 256):
                if chunk:
                    f.write(chunk)
        return target
    except Exception as e:
        print(f"[FAIL] download {url} -> {e}")
        return None

def convert_jpg_to_png(jpg_path: Path) -> Path | None:
    """把 jpg/jpeg 转 png，不删除原文件"""
    try:
        png_path = jpg_path.with_suffix(".png")
        # 避免覆盖已有 png（比如同名已存在），必要时做唯一化
        if png_path.exists():
            png_path = ensure_unique_path(png_path)

        with Image.open(jpg_path) as im:
            im = im.convert("RGB")
            im.save(png_path, format="PNG", optimize=True)

        return png_path
    except Exception as e:
        print(f"[FAIL] convert {jpg_path} -> png: {e}")
        return None

def collect_urls(qmd_text: str) -> list[str]:
    urls = set()
    for pat in PATTERNS:
        for m in re.findall(pat, qmd_text, flags=re.IGNORECASE):
            u = m.strip()
            # 去掉结尾多余的 )
            u = u.rstrip(")")
            urls.add(u)
    return sorted(urls)

def main():
    if not QMD_PATH.exists():
        print(f"QMD not found: {QMD_PATH}")
        return

    text = QMD_PATH.read_text(encoding="utf-8", errors="ignore")
    urls = collect_urls(text)

    if not urls:
        print("No remote image URLs found in qmd.")
        return

    print(f"Found {len(urls)} remote image URLs.")

    # url -> local_rel_path (最终要写入 qmd 的路径)
    rewrite_map: dict[str, str] = {}

    for url in urls:
        local_file = download_url(url, OUT_DIR)
        if not local_file:
            continue

        # 若下载为 jpg/jpeg，则转换为 png，并让 qmd 指向 png
        suf = local_file.suffix.lower()
        if suf in {".jpg", ".jpeg"}:
            png_file = convert_jpg_to_png(local_file)
            if png_file:
                # 保留 jpg（KEEP_JPG=True），qmd 只指向 png
                rewrite_map[url] = png_file.as_posix()
            else:
                # 转换失败就先用 jpg
                rewrite_map[url] = local_file.as_posix()
        else:
            rewrite_map[url] = local_file.as_posix()

        print(f"[OK] {url} -> {rewrite_map[url]}")

    if REWRITE_QMD and rewrite_map:
        backup = QMD_PATH.with_suffix(QMD_PATH.suffix + ".bak")
        backup.write_text(text, encoding="utf-8")

        new_text = text
        # 仅替换“远程 URL”本身，避免误伤其它内容
        for url, rel_path in rewrite_map.items():
            new_text = new_text.replace(url, rel_path)

        QMD_PATH.write_text(new_text, encoding="utf-8")
        print(f"Rewrote QMD: {QMD_PATH} (backup: {backup})")

    print("Done.")

if __name__ == "__main__":
    # Pillow 依赖提示更友好
    try:
        import PIL  # noqa
    except Exception:
        print("Missing dependency: Pillow. Please run: pip install pillow")
        raise
    main()