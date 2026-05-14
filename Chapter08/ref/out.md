__The    Laplace    Transform__

<span style="color:#000066"> __1\.  __ </span>  <span style="color:#000066"> __双边拉普拉斯变换；__ </span>

<span style="color:#000066"> __2\.  __ </span>  <span style="color:#000066"> __双边拉普拉斯变换的收敛域；__ </span>

<span style="color:#000066"> __3\.  __ </span>  <span style="color:#000066"> __零极点图；__ </span>

<span style="color:#000066"> __4\.  __ </span>  <span style="color:#000066"> __双边拉普拉斯变换的性质；__ </span>

<span style="color:#000066"> __ 系统函数；__ </span>
****
<span style="color:#000066"> __  单边拉普拉斯变换；__ </span>

<span style="color:#000066"> __9\.0   __ </span>  <span style="color:#000066"> __引言  __ </span>  <span style="color:#000066"> __Introduction__ </span>  __ __

__  __  <span style="color:#000066"> __傅里叶分析方法之所以在信号与__ </span>  <span style="color:#000066"> __LTI__ </span>  <span style="color:#000066"> __系统分析中如此有用，很大程度上是因为相当广泛的信号都可以表示成复指数信号的线性组合，而__ </span>  <span style="color:#901f16"> __复指数函数是一切 __ </span>  <span style="color:#901f16"> __LTI __ </span>  <span style="color:#901f16"> __系统的特征函数。__ </span>

<span style="color:#000066"> __    傅里叶变换是以复指数函数中的特例，即以 　  和        为基底分解信号的。对于更一般的复指数函数       和       ，也理应能以此为基底对信号进行分解。__ </span>

__  __  <span style="color:#000066"> __将傅里叶变换推广到更一般的情况就是本章及下一章要讨论的中心问题。__ </span>

__  __  <span style="color:#000066"> __通过本章及下一章，会看到拉氏变换和__ </span>  <span style="color:#000066"> __Ｚ__ </span>  <span style="color:#000066"> __变换不仅具有很多与傅里叶变换相同的重要性质，不仅能适用于用傅里叶变换的方法可以解决的信号与系统分析问题，而且还能解决傅里叶分析方法不适用的许多方面。__ </span>  <span style="color:#a50021"> __拉氏变换与__ </span>  <span style="color:#a50021"> __Ｚ__ </span>  <span style="color:#a50021"> __变换的分析方法是傅里叶分析法的推广，傅里叶分析是它们的特例。__ </span>

<span style="color:#000066"> __The  Laplace  Transform__ </span>

__  __  <span style="color:#000066"> __复指数信号      是一切连续时间__ </span>  <span style="color:#000066"> __LTI__ </span>  <span style="color:#000066"> __系统的特征函数。如果__ </span>  <span style="color:#000066"> __LTI__ </span>  <span style="color:#000066"> __系统的单位冲激响应为         ，则系统对         产生的响应是__ </span>  <span style="color:#000066"> __:  __ </span>

<span style="color:#000066"> __显然当      时，就是傅里叶变换__ </span>  <span style="color:#000066"> __。__ </span>

<span style="color:#000066"> __称为    的__ </span>  <span style="color:#760c04"> __双边拉氏变换__ </span>  <span style="color:#000066"> __，其中  __ </span>  <span style="color:#000066"> __         __ </span>

<span style="color:#000066"> __若      ，     则有__ </span>  <span style="color:#000066"> __:__ </span>

<span style="color:#000066"> __即：__ </span>  <span style="color:#760c04"> __CTFT__ </span>  <span style="color:#760c04"> __是双边拉普拉斯变换在      或是在__ </span>  <span style="color:#760c04"> __σ__ </span>  <span style="color:#760c04"> __，__ </span>  <span style="color:#760c04"> __ω__ </span>  <span style="color:#760c04"> __复平面上的__ </span>  <span style="color:#760c04"> __j__ </span>  <span style="color:#760c04"> __ω__ </span>  <span style="color:#760c04"> __轴上的特例__ </span>  <span style="color:#760c04"> __。__ </span>

__  __  <span style="color:#000066"> __所以__ </span>  <span style="color:#760c04"> __拉氏变换是对傅里叶变换的推广__ </span>  <span style="color:#000066"> __， 　 的拉氏变换就是        的傅里叶变换。只要有合适的  存在，就可以使某些本来不满足狄里赫利条件的信号在引入    后满足该条件。即有些信号的傅氏变换不收敛而它的拉氏变换存在。__ </span>

<span style="color:#000066"> __ __ </span>  <span style="color:#760c04"> __拉氏变换比傅里叶变换有更广泛的适用性。__ </span>

<span style="color:#000066"> __说明：一个连续信号如果存在傅立叶变换，__ </span>

<span style="color:#000066"> __这个信号必须绝对可积，即__ </span>

<span style="color:#000066"> __在此例中，要求    ，   才有傅里叶变换：__ </span>

![](img/ch9_0.png)

![](img/ch9_1.png)

![](img/ch9_2.png)

<span style="color:#760c04"> __要求         ，信号       才有傅立叶变换存在__ </span>

![](img/ch9_3.png)

<span style="color:#000066"> __1__ </span>  <span style="color:#000066"> __、比较例__ </span>  <span style="color:#000066"> __1__ </span>  <span style="color:#000066"> __和例__ </span>  <span style="color:#000066"> __2__ </span>  <span style="color:#000066"> __的两个信号，它们的拉氏变换的代数表示式是一样的，但使这个代数表示式成立的__ </span>  <span style="color:#901f16"> __S__ </span>  <span style="color:#901f16"> __域__ </span>  <span style="color:#000066"> __却不相同。__ </span>

<span style="color:#901f16"> __结论：__ </span>  <span style="color:#000066"> __给出一个信号的拉氏变换时，__ </span>  <span style="color:#760c04"> _代数表示式_ </span>  <span style="color:#000066"> __和使该表示式成立的__ </span>  <span style="color:#760c04"> _变量_ </span>  <span style="color:#760c04"> _s_ </span>  <span style="color:#760c04"> _的范围_ </span>  <span style="color:#000066"> __都应给出。__ </span>

<span style="color:#000066"> __2__ </span>  <span style="color:#000066"> __、 拉氏变换与傅里叶变换一样存在收敛问题。__ </span>  <span style="color:#760c04"> __并非任何信号的拉氏变换都存在，也不是 __ </span>  <span style="color:#760c04"> __S __ </span>  <span style="color:#760c04"> __平面上的任何复数都能使拉氏变换收敛。__ </span>

<span style="color:#000066"> __3__ </span>  <span style="color:#000066"> __、使拉氏变换积分收敛的复数 __ </span>  <span style="color:#000066"> __S__ </span>  <span style="color:#000066"> __的范围，称为拉氏变换的__ </span>  <span style="color:#760c04"> __收敛域__ </span>  <span style="color:#000066"> __ ，简记为__ </span>  <span style="color:#760c04"> __ROC__ </span>  <span style="color:#000066"> __ __ </span>  <span style="color:#000066"> __。（__ </span>  <span style="color:#000066"> __Region of Convergence__ </span>  <span style="color:#000066"> __）__ </span>

<span style="color:#000066"> __4__ </span>  <span style="color:#000066"> __、__ </span>  <span style="color:#760c04"> __不同的信号可能会有完全相同的拉氏变换表达式，只是它们的收敛域不同。__ </span>

<span style="color:#000066"> __5__ </span>  <span style="color:#000066"> __、__ </span>  <span style="color:#760c04"> __只有拉氏变换表达式连同相应的收敛域，才能和信号建立一一对应的关系__ </span>  <span style="color:#000066"> __。__ </span>

<span style="color:#000066"> __6__ </span>  <span style="color:#000066"> __、__ </span>  <span style="color:#760c04"> __如果拉氏变换的__ </span>  <span style="color:#760c04"> __ROC__ </span>  <span style="color:#760c04"> __包含      轴__ </span>  <span style="color:#000066"> __，则有__ </span>

<span style="color:#760c04"> __二__ </span>  <span style="color:#760c04"> __\. __ </span>  <span style="color:#760c04"> __ROC__ </span>  <span style="color:#760c04"> __的表示方法：（复平面__ </span>  <span style="color:#760c04"> __\)__ </span>

![](img/ch9_4.png)

![](img/ch9_5.png)

<span style="color:#760c04"> __有理函数__ </span>  <span style="color:#760c04"> __X\(S\)__ </span>  <span style="color:#760c04"> __的__ </span>  <span style="color:#760c04"> __ROC__ </span>  <span style="color:#760c04"> __的性质：__ </span>  <span style="color:#000066"> __1__ </span>  <span style="color:#000066"> __）__ </span>  <span style="color:#000066"> __X\(s\)__ </span>  <span style="color:#000066"> __的__ </span>  <span style="color:#000066"> __ROC__ </span>  <span style="color:#000066"> __在__ </span>  <span style="color:#000066"> __s__ </span>  <span style="color:#000066"> __平面内由平行于     轴的带状区域组成；__ </span>

<span style="color:#000066"> __2__ </span>  <span style="color:#000066"> __）右边信号的__ </span>  <span style="color:#000066"> __ROC__ </span>  <span style="color:#000066"> __在__ </span>  <span style="color:#000066"> __s__ </span>  <span style="color:#000066"> __平面的右半部；__ </span>

<span style="color:#000066"> __3__ </span>  <span style="color:#000066"> __）左边信号的__ </span>  <span style="color:#000066"> __ROC__ </span>  <span style="color:#000066"> __在__ </span>  <span style="color:#000066"> __s__ </span>  <span style="color:#000066"> __平面的左半部；__ </span>

<span style="color:#000066"> __若   是右边信号__ </span>  <span style="color:#000066"> __\,       \,   __ </span>  <span style="color:#000066"> __在__ </span>  <span style="color:#000066"> __ROC__ </span>  <span style="color:#000066"> __内__ </span>  <span style="color:#000066"> __，则有         绝对可积，即：__ </span>

<span style="color:#000066"> __表明   也在收敛域内，右边信号的__ </span>  <span style="color:#000066"> __ROC__ </span>  <span style="color:#000066"> __在极点的右边。__ </span>

__  __  <span style="color:#000066"> __若      是左边信号，定义于            __ </span>  <span style="color:#000066"> __\,      __ </span>  <span style="color:#000066"> __在 __ </span>  <span style="color:#000066"> __ROC __ </span>  <span style="color:#000066"> __内，            ，则__ </span>

<span style="color:#000066"> __表明   也在收敛域内__ </span>  <span style="color:#000066"> __。__ </span>  <span style="color:#000066"> __左边信号的__ </span>  <span style="color:#000066"> __ROC__ </span>  <span style="color:#000066"> __在最左极点的的左边__ </span>

![](img/ch9_6.png)

![](img/ch9_7.png)

![](img/ch9_8.png)

![](img/ch9_9.png)

__  __  <span style="color:#000066"> __显然    在       也有一阶零点，由于零极点相抵消，致使在整个__ </span>  <span style="color:#000066"> __S__ </span>  <span style="color:#000066"> __平面上无极点。__ </span>

![](img/ch9_10.png)

<span style="color:#000066"> __当         时，上述__ </span>  <span style="color:#000066"> __ROC__ </span>  <span style="color:#000066"> __有公共部分，__ </span>

<span style="color:#000066"> __当         时，上述 __ </span>  <span style="color:#000066"> __ROC __ </span>  <span style="color:#000066"> __无公共部分，表明       	不存在。__ </span>

![](img/ch9_11.png)

__    __  <span style="color:#000066"> __前面的例子给出的拉氏变换式都是关于__ </span>  <span style="color:#000066"> __s__ </span>  <span style="color:#000066"> __的两个多项式之比，这种形式的拉氏变换称为有理拉氏变换。__ </span>

<span style="color:#000066"> __令分子多项式       的根称为    的__ </span>  <span style="color:#760c04"> __零点__ </span>  <span style="color:#000066"> __，用  表示__ </span>

<span style="color:#000066"> __令分母多项式       的根称为    的__ </span>  <span style="color:#760c04"> __极点__ </span>  <span style="color:#000066"> __，用  表示__ </span>

![](img/ch9_12.png)

![](img/ch9_13.png)

![](img/ch9_14.png)

<span style="color:#760c04"> __    __ </span>  <span style="color:#760c04"> __的零极点图：__ </span>  <span style="color:#000066"> __在__ </span>  <span style="color:#000066"> __s__ </span>  <span style="color:#000066"> __平面标出    的零点和极点。__ </span>

<span style="color:#000066"> __例：画出                             的零极点图__ </span>

__    __  <span style="color:#000066"> __在有限__ </span>  <span style="color:#000066"> __S__ </span>  <span style="color:#000066"> __平面内，    的零点和极点可以完全表征    的代数表示式。（__ </span>  <span style="color:#760c04"> __常数因子除外__ </span>  <span style="color:#000066"> __）__ </span>

<span style="color:#000066"> __例：已知    的零、极点分布如图，且                                                        	   写出     的表示式。__ </span>

![](img/ch9_15.png)

![](img/ch9_16.png)

![](img/ch9_17.png)

![](img/ch9_18.png)

<span style="color:#000066"> __    __ </span>  <span style="color:#000066"> __零极点图及其收敛域可以表示一个 	  最多与真实的    相差一个常数因子   。__ </span>

<span style="color:#000066"> __  因此，__ </span>  <span style="color:#760c04"> __零极点图是拉氏变换的图示方法__ </span>  <span style="color:#000066"> __。__ </span>

<span style="color:#000066"> __例：画出                          __ </span>

<span style="color:#000066"> __的零极点图__ </span>

<span style="color:#000066"> __可以形成三种 __ </span>  <span style="color:#000066"> __ROC__ </span>  <span style="color:#000066"> __：__ </span>

<span style="color:#000066"> __   __ </span>  <span style="color:#000066"> __ROC__ </span>  <span style="color:#000066"> __：             此时       是右边信号。__ </span>

<span style="color:#000066"> __   __ </span>  <span style="color:#000066"> __ROC__ </span>  <span style="color:#000066"> __：                   此时       是左边信号。__ </span>

<span style="color:#000066"> __   __ </span>  <span style="color:#000066"> __ROC__ </span>  <span style="color:#000066"> __：                      此时       是双边信号__ </span>

<span style="color:#000066"> __Properties  of  the  Laplace  Transform__ </span>

<span style="color:#000066"> __ __ </span>  <span style="color:#000066"> __拉氏变换与傅氏变换一样具有很多重要的性质。这里只着重于__ </span>  <span style="color:#760c04"> __ROC__ </span>  <span style="color:#000066"> __的讨论。__ </span>

<span style="color:#760c04"> __1\. __ </span>  <span style="color:#760c04"> __线性__ </span>  <span style="color:#760c04"> __（__ </span>  <span style="color:#760c04"> __Linearity __ </span>  <span style="color:#760c04"> __）：__ </span>

<span style="color:#760c04"> __ __ </span>  <span style="color:#760c04"> __当  与  无交集时，表明    不存在。__ </span>

![](img/ch9_19.png)



  * <span style="color:#760c04"> __2\. __ </span>  <span style="color:#760c04"> __时移性质__ </span>  <span style="color:#760c04"> __（__ </span>  <span style="color:#760c04"> __Time Shifting__ </span>  <span style="color:#760c04"> __）__ </span>  <span style="color:#760c04"> __:__ </span>
  * <span style="color:#760c04"> __3\. S__ </span>  <span style="color:#760c04"> __域平移__ </span>  <span style="color:#760c04"> __（__ </span>  <span style="color:#760c04"> __Shifting in the s\-Domain__ </span>  <span style="color:#760c04"> __）__ </span>  <span style="color:#760c04"> __:__ </span>


<span style="color:#000066"> __    __ </span>  <span style="color:#000066"> __表明             的__ </span>  <span style="color:#000066"> __ROC__ </span>  <span style="color:#000066"> __是将        的__ </span>  <span style="color:#000066"> __ROC__ </span>  <span style="color:#000066"> __平移了一个__ </span>  <span style="color:#000066"> __            。__ </span>

![](img/ch9_20.png)

![](img/ch9_21.png)

![](img/ch9_22.png)

![](img/ch9_23.png)

![](img/ch9_24.png)

![](img/ch9_25.png)

__ __  <span style="color:#760c04"> __4\.  __ </span>  <span style="color:#760c04"> __时域尺度变换__ </span>  <span style="color:#760c04"> __（__ </span>  <span style="color:#760c04"> __Time Scaling__ </span>  <span style="color:#760c04"> __）__ </span>  <span style="color:#760c04"> __:__ </span>

![](img/ch9_26.png)

<span style="color:#000066"> __求                           的拉氏变换及__ </span>  <span style="color:#000066"> __ROC__ </span>

<span style="color:#000066"> __  __ </span>  <span style="color:#000066"> __可见：__ </span>  <span style="color:#760c04"> __若信号在时域尺度变换，其拉氏变换的__ </span>  <span style="color:#760c04"> __ROC__ </span>  <span style="color:#760c04"> __在__ </span>  <span style="color:#760c04"> __S__ </span>  <span style="color:#760c04"> __平面上作相反的尺度变换。__ </span>

<span style="color:#760c04"> __5\.  __ </span>  <span style="color:#760c04"> __共轭对称（__ </span>  <span style="color:#760c04"> __Conjugation__ </span>  <span style="color:#760c04"> __）性__ </span>  <span style="color:#760c04"> __：__ </span>

<span style="color:#000066"> __如果    是实信号，且    在  有极点（或零点），则    一定在    也有极点或零点。这表明：__ </span>  <span style="color:#760c04"> __实信号的拉氏变换其复数零、极点必共轭成对出现。__ </span>

__ __  <span style="color:#760c04"> __6\.  __ </span>  <span style="color:#760c04"> __卷积性质__ </span>  <span style="color:#760c04"> __:__ </span>  <span style="color:#760c04"> __（__ </span>  <span style="color:#760c04"> __Convolution Property__ </span>  <span style="color:#760c04"> __）__ </span>

__    __  <span style="color:#000066"> __原因是       与       相乘时，发生了零极点相抵消的现象。当被抵消的极点恰好在__ </span>  <span style="color:#000066"> __ROC__ </span>  <span style="color:#000066"> __的边界上时，就会使收敛域扩大__ </span>  <span style="color:#000066"> __。__ </span>

<span style="color:#760c04"> __7\. __ </span>  <span style="color:#760c04"> __时域微分__ </span>  <span style="color:#760c04"> __:__ </span>  <span style="color:#760c04"> __（__ </span>  <span style="color:#760c04"> __Differentiation in theTime Domain__ </span>  <span style="color:#760c04"> __）__ </span>

![](img/ch9_27.png)

![](img/ch9_28.png)

![](img/ch9_29.png)

![](img/ch9_30.png)

<span style="color:#760c04"> __8\.  S__ </span>  <span style="color:#760c04"> __域微分__ </span>  <span style="color:#760c04"> __:__ </span>  <span style="color:#760c04"> __（__ </span>  <span style="color:#760c04"> __Differentiation in the s\-Domain__ </span>  <span style="color:#760c04"> __）__ </span>

![](img/ch9_31.png)

<span style="color:#000066"> __例__ </span>  <span style="color:#000066"> __\.__ </span>  <span style="color:#000066"> __求                的拉氏变换__ </span>

![](img/ch9_32.png)

__ __  <span style="color:#760c04"> __9\.  __ </span>  <span style="color:#760c04"> __时域积分__ </span>  <span style="color:#760c04"> __:__ </span>  <span style="color:#760c04"> __（__ </span>  <span style="color:#760c04"> __Integration in the Time Domain __ </span>  <span style="color:#760c04"> __）__ </span>

![](img/ch9_33.png)

__ 10__  <span style="color:#760c04"> __\. __ </span>  <span style="color:#760c04"> __初值与终值定理__ </span>  <span style="color:#760c04"> __:__ </span>

<span style="color:#760c04"> __（__ </span>  <span style="color:#760c04"> __The Initial\- and  Final\- Value Theorems\)__ </span>

<span style="color:#000066"> __例：已知因果信号    的拉氏变换__ </span>

<span style="color:#000066"> __    				求     和__ </span>

![](img/ch9_34.png)

![](img/ch9_35.png)

<span style="color:#000066"> __时     ，且在    不包含奇异函数。__ </span>

<span style="color:#000066"> __将       在        展开为__ </span>  <span style="color:#000066"> __Taylor__ </span>  <span style="color:#000066"> __级数有：__ </span>

<span style="color:#000066"> __是因果信号，且在    无奇异函数__ </span>  <span style="color:#000066"> __\,__ </span>

<span style="color:#000066"> __除了    在    可以有一阶极点外，其它极点均在__ </span>  <span style="color:#000066"> __S__ </span>  <span style="color:#000066"> __平面__ </span>  <span style="color:#000066"> __的左半平面（即__ </span>  <span style="color:#760c04"> __保证    有终值__ </span>  <span style="color:#000066"> __）。__ </span>  <span style="color:#000066"> __故          的__ </span>  <span style="color:#000066"> __ROC__ </span>  <span style="color:#000066"> __中必包含     轴。表明__ </span>

![](img/ch9_36.png)

<span style="color:#000066"> __若                 在__ </span>  <span style="color:#000066"> __ROC__ </span>  <span style="color:#000066"> __内，则有__ </span>  <span style="color:#000066"> __:__ </span>

<span style="color:#000066"> __The Inverse Laplace Transform__ </span>

<span style="color:#000066"> __当  从         时__ </span>  <span style="color:#000066"> __\,  __ </span>  <span style="color:#000066"> __从__ </span>

<span style="color:#760c04"> __拉氏反变换表明__ </span>  <span style="color:#760c04"> __:__ </span>

<span style="color:#000066"> __        __ </span>  <span style="color:#000066"> __可以被分解成复振幅为__ </span>

<span style="color:#000066"> __  的复指数信号   的线性组合。__ </span>

<span style="color:#000066"> __对有理函数形式的    求反变换一般有两种方法__ </span>  <span style="color:#000066"> __\,__ </span>  <span style="color:#000066"> __即__ </span>  <span style="color:#760c04"> __部分分式展开法__ </span>  <span style="color:#000066"> __和__ </span>  <span style="color:#760c04"> __留数法__ </span>  <span style="color:#000066"> __。__ </span>

__  __  <span style="color:#000066"> __1\. __ </span>  <span style="color:#000066"> __将         展开为部分分式。                                __ </span>  <span style="color:#000066"> __2\. __ </span>  <span style="color:#000066"> __根据       的__ </span>  <span style="color:#000066"> __ROC__ </span>  <span style="color:#000066"> __，确定每一项的__ </span>  <span style="color:#000066"> __ROC __ </span>  <span style="color:#000066"> __。         __ </span>  <span style="color:#000066"> __3\. __ </span>  <span style="color:#000066"> __利用常用信号的变换对与拉氏变换的性质__ </span>  <span style="color:#000066"> __\,__ </span>  <span style="color:#000066"> __对每一项进行反变换。__ </span>

<span style="color:#000066"> __确定其可能的收敛域及所对应信号的属性。__ </span>

<span style="color:#000066"> __9\.4  __ </span>  <span style="color:#000066"> __由零极点图对傅里叶变换几何求值__ </span>

<span style="color:#000066"> __Geometric Evaluation of the Fourier Transform __ </span>  <span style="color:#000066"> __from the Pole\-Zero Plot__ </span>

<span style="color:#760c04"> __可以用零极点图表示         的特征__ </span>  <span style="color:#000066"> __。当__ </span>  <span style="color:#000066"> __ROC__ </span>  <span style="color:#000066"> __包括　　轴时，以            代入__ </span>

<span style="color:#000066"> __就可以得到          。以此为基础可以用几何求值的方法从零极点图求得		            的特性。这在定性分析系统频率特性时有很大用处。__ </span>

<span style="color:#760c04"> __令             即在__ </span>  <span style="color:#760c04"> __S__ </span>  <span style="color:#760c04"> __平面中__ </span>  <span style="color:#760c04"> __s__ </span>  <span style="color:#760c04"> __沿虚轴移动，可得：__ </span>

![](img/ch9_37.png)

<span style="color:#760c04"> __例：已知                                     ，用几何法确定傅立叶变换的幅频和相频特性。__ </span>

<span style="color:#760c04"> __注：__ </span>  <span style="color:#000066"> __用几何法确定傅立叶变换的意义：__ </span>

<span style="color:#000066"> __      由零极点图来近似观察傅立叶变换的整体特性。__ </span>

![](img/ch9_38.png)

![](img/ch9_39.png)

__  __  <span style="color:#000066"> __随着    ，      单调下降__ </span>  <span style="color:#000066"> __，__ </span>

![](img/ch9_40.png)

__ __  <span style="color:#000066"> __随着    ，       趋向     。__ </span>

![](img/ch9_41.png)

![](img/ch9_42.png)

![](img/ch9_43.png)

![](img/ch9_44.png)

__  __  <span style="color:#000066"> __1\. __ </span>  <span style="color:#000066"> __当     时，    有两个实数极点，      随着   的增加而单调下降，而        则由__ </span>

<span style="color:#000066"> __     时为__ </span>  <span style="color:#000066"> __0__ </span>  <span style="color:#000066"> __变到        的     。__ </span>

![](img/ch9_45.png)

![](img/ch9_46.png)

![](img/ch9_47.png)

![](img/ch9_48.png)

__ __  <span style="color:#000066"> __2\.__ </span>  <span style="color:#000066"> __　当            时，则二阶 极点分裂为__ </span>  <span style="color:#760c04"> __共轭复数极点，__ </span>  <span style="color:#000066"> __且随    的减小而逐步靠近     轴。极点运动的轨迹__ </span>  <span style="color:#000066"> __——__ </span>  <span style="color:#760c04"> __根轨迹是一个半径为      的圆周__ </span>  <span style="color:#000066"> __。__ </span>

__  __  <span style="color:#000066"> __由于第__ </span>  <span style="color:#000066"> __2__ </span>  <span style="color:#000066"> __象限的极点矢量变得很短，因而会使      出现峰值。其峰点位于         __ </span>

![](img/ch9_49.png)

<span style="color:#000066"> __随着   ，位于第__ </span>  <span style="color:#000066"> __2__ </span>  <span style="color:#000066"> __象限的极点矢量比第__ </span>  <span style="color:#000066"> __3 __ </span>  <span style="color:#000066"> __象限的极点矢量更短，因此它对系统特性的影响较大。__ </span>

__ __  <span style="color:#000066"> __该系统的      在任何时候都等于__ </span>  <span style="color:#000066"> __1__ </span>  <span style="color:#000066"> __，所以称为__ </span>  <span style="color:#760c04"> __全通系统__ </span>  <span style="color:#000066"> __。__ </span>

![](img/ch9_50.png)

![](img/ch9_51.png)

__  __  <span style="color:#000066"> __考查两个系统，它们的极点相同，零点分布关于    轴对称。其中一个系统的零点均在左半平面，另一个系统的零点均在右半平面。__ </span>

__  __  <span style="color:#000066"> __显然这两个系统的幅频特性是相同的。但零点在左半平面的系统其相位总小于零点在右半平面的系统。因此将__ </span>  <span style="color:#760c04"> __零极点均位于左半平面的系统称为最小相位系统。__ </span>

__  __  <span style="color:#000066"> __工程应用中设计的各种频率选择性滤波器，如：__ </span>  <span style="color:#000066"> __Butterworth __ </span>  <span style="color:#000066"> __、__ </span>  <span style="color:#000066"> __Chebyshev__ </span>  <span style="color:#000066"> __、 __ </span>  <span style="color:#000066"> __Cauer__ </span>  <span style="color:#000066"> __滤波器都是最小相位系统。__ </span>

<span style="color:#000066"> __从本质上讲__ </span>  <span style="color:#760c04"> __系统的特性是由系统的零、极点分布决定的__ </span>  <span style="color:#000066"> __。对系统进行优化设计，实质上就是优化其零、极点的位置。__ </span>

<span style="color:#000066"> __当工程应用中要求实现一个非最小相位系统时，通常采用将一个最小相位系统和一个全通系统级联来实现。__ </span>

<span style="color:#000066"> __Some Laplace Transform Pairs__ </span>

<span style="color:#000066"> __9\.7__ </span>  <span style="color:#000066"> __用拉氏变换分析与表征__ </span>  <span style="color:#000066"> __LTI__ </span>  <span style="color:#000066"> __系统__ </span>

<span style="color:#000066"> __Analysis and Characterized of LTI Systems Using  the Laplace Transform__ </span>

__  __  <span style="color:#000066"> __以卷积特性为基础，可以建立__ </span>  <span style="color:#000066"> __LTI__ </span>  <span style="color:#000066"> __系统的拉氏变换分析方法，即__ </span>

__  __  <span style="color:#000066"> __其中    是    的拉氏变换，称为__ </span>  <span style="color:#760c04"> __系统函数__ </span>  <span style="color:#000066"> __或__ </span>  <span style="color:#760c04"> __转移函数__ </span>  <span style="color:#000066"> __。__ </span>

![](img/ch9_52.png)

![](img/ch9_53.png)

![](img/ch9_54.png)

![](img/ch9_55.png)

![](img/ch9_56.png)

![](img/ch9_57.png)

<span style="color:#000066"> __如果     时      ，则__ </span>  <span style="color:#760c04"> __系统是因果的__ </span>  <span style="color:#000066"> __。__ </span>

![](img/ch9_58.png)

<span style="color:#000066"> __             __ </span>  <span style="color:#000066"> __连同相应的__ </span>  <span style="color:#000066"> __ROC__ </span>  <span style="color:#000066"> __也能完全描述一个__ </span>  <span style="color:#000066"> __LTI__ </span>  <span style="color:#000066"> __系统。系统的许多重要特性在        及其__ </span>  <span style="color:#000066"> __ROC__ </span>  <span style="color:#000066"> __中一定有具体的体现。__ </span>

<span style="color:#760c04"> __二__ </span>  <span style="color:#760c04"> __\.  __ </span>  <span style="color:#760c04"> __用系统函数表征__ </span>  <span style="color:#760c04"> __LTI__ </span>  <span style="color:#760c04"> __系统：__ </span>

__   __  <span style="color:#000066"> __因此，__ </span>  <span style="color:#760c04"> __因果系统__ </span>  <span style="color:#000066"> __的       是右边信号，结论 ：其        的__ </span>  <span style="color:#760c04"> __ROC__ </span>  <span style="color:#760c04"> __必位于最右极点右边__ </span>  <span style="color:#000066"> __。__ </span>

__  __  <span style="color:#000066"> __应该强调指出，由__ </span>  <span style="color:#000066"> __ROC__ </span>  <span style="color:#000066"> __的特征，反过来并不能判定系统是否因果。__ </span>  <span style="color:#000066"> __ROC__ </span>  <span style="color:#000066"> __是最右边极点的右边并不一定系统因果。__ </span>

<span style="color:#760c04"> __因果性判定：__ </span>

<span style="color:#000066"> __If__ </span>

<span style="color:#000066"> __Then    __ </span>  <span style="color:#000066"> __系统是因果的。__ </span>

__  __  <span style="color:#000066"> __如果系统稳定，则有                            。因此            必存在。意味着        的__ </span>  <span style="color:#000066"> __ROC__ </span>  <span style="color:#000066"> __必然包括      轴。__ </span>

<span style="color:#760c04"> __系统稳定性判定：__ </span>

<span style="color:#000066"> __if__ </span>  <span style="color:#000066"> __系统函数        的__ </span>  <span style="color:#000066"> __ROC__ </span>  <span style="color:#000066"> __包括      轴，__ </span>  <span style="color:#000066"> __then__ </span>  <span style="color:#000066"> __系统稳定。__ </span>

<span style="color:#760c04"> __因果系统稳定性判定：    __ </span>

<span style="color:#000066"> __if    __ </span>  <span style="color:#000066"> __的__ </span>  <span style="color:#000066"> __全部极点必须位于__ </span>  <span style="color:#000066"> __S__ </span>  <span style="color:#000066"> __平面的左半边，__ </span>  <span style="color:#000066"> __Then__ </span>  <span style="color:#000066"> __具有有理        的因果系统稳定。__ </span>

<span style="color:#000066"> __例__ </span>  <span style="color:#000066"> __1__ </span>  <span style="color:#000066"> __：某系统的                               __ </span>

<span style="color:#000066"> __显然该系统是因果的，确定系统的稳定性__ </span>  <span style="color:#000066"> __。__ </span>

<span style="color:#000066"> __显然，__ </span>  <span style="color:#000066"> __ROC__ </span>  <span style="color:#000066"> __是最右边极点的右边。__ </span>

__       __  <span style="color:#000066"> __的__ </span>  <span style="color:#000066"> __ROC__ </span>  <span style="color:#000066"> __是最右边极点的右边，但       是非有理函数，__ </span>  <span style="color:#000066"> __                ，系统是非因果的。__ </span>

__  __  <span style="color:#000066"> __由于__ </span>  <span style="color:#000066"> __ROC__ </span>  <span style="color:#000066"> __包括     轴，该系统仍是稳定的。__ </span>

__     __  <span style="color:#000066"> __仍是非有理函数，__ </span>  <span style="color:#000066"> __ROC__ </span>  <span style="color:#000066"> __是最右边极点的右边，__ </span>  <span style="color:#000066"> __但由于              ，是因果的。__ </span>  <span style="color:#000066"> __  __ </span>

<span style="color:#000066"> __如果__ </span>  <span style="color:#000066"> __LTI__ </span>  <span style="color:#000066"> __系统的系统函数是有理函数，且全部极点位于__ </span>  <span style="color:#000066"> __S__ </span>  <span style="color:#000066"> __平面的左半边，则__ </span>  <span style="color:#000066"> __因果__ </span>  <span style="color:#000066"> __系统是稳定的。 __ </span>

<span style="color:#000066"> __2\. __ </span>  <span style="color:#000066"> __如果__ </span>  <span style="color:#000066"> __LTI__ </span>  <span style="color:#000066"> __系统的系统函数是有理函数，且系统因果，则系统函数的__ </span>  <span style="color:#000066"> __ROC__ </span>  <span style="color:#000066"> __位于最右边极点的右边。__ </span>

<span style="color:#000066"> __ 3\.__ </span>  <span style="color:#000066"> __如果__ </span>  <span style="color:#000066"> __LTI__ </span>  <span style="color:#000066"> __系统是稳定的，则系统函数的__ </span>  <span style="color:#000066"> __ROC__ </span>  <span style="color:#000066"> __必然包括      轴。__ </span>

<span style="color:#760c04"> __三__ </span>  <span style="color:#760c04"> __\. __ </span>  <span style="color:#760c04"> __由__ </span>  <span style="color:#760c04"> __LCCDE__ </span>  <span style="color:#760c04"> __描述的__ </span>  <span style="color:#760c04"> __LTI__ </span>  <span style="color:#760c04"> __系统的系统函数：__ </span>

<span style="color:#000066"> __的__ </span>  <span style="color:#000066"> __ROC__ </span>  <span style="color:#000066"> __需要由系统的相关特性来确定。__ </span>

<span style="color:#000066"> __1__ </span>  <span style="color:#000066"> __）__ </span>  <span style="color:#000066"> __如果已知__ </span>  <span style="color:#000066"> __LCCDE__ </span>  <span style="color:#000066"> __描述的系统是因果的，则              的__ </span>  <span style="color:#000066"> __ROC__ </span>  <span style="color:#000066"> __必是最右边极点的右边。__ </span>

<span style="color:#000066"> __2__ </span>  <span style="color:#000066"> __）如果已知__ </span>  <span style="color:#000066"> __LCCDE__ </span>  <span style="color:#000066"> __描述的系统是稳定的，则           的__ </span>  <span style="color:#000066"> __ROC __ </span>  <span style="color:#000066"> __必包括      轴__ </span>  <span style="color:#000066"> __。__ </span>

<span style="color:#000066"> __例__ </span>  <span style="color:#000066"> __1:__ </span>  <span style="color:#000066"> __已知__ </span>  <span style="color:#000066"> __LTI__ </span>  <span style="color:#000066"> __系统的输入            ，输出                  ，试确定系统函数及系统的其它性质，以及表征系统的微分方程。__ </span>  <span style="color:#760c04"> __   __ </span>

<span style="color:#000066"> __例__ </span>  <span style="color:#000066"> __2__ </span>  <span style="color:#000066"> __：一因果__ </span>  <span style="color:#000066"> __LTI__ </span>  <span style="color:#000066"> __系统，其输入和输出满足：__ </span>

<span style="color:#000066"> __微分方程：__ </span>

![](img/ch9_59.png)

<span style="color:#000066"> __求系统函数及收敛域；画出零极点图；判定系统稳定性？__ </span>

<span style="color:#000066"> __自学。请关注例__ </span>  <span style="color:#000066"> __9\.25__ </span>  <span style="color:#000066"> __、__ </span>  <span style="color:#000066"> __9\.26__ </span>  <span style="color:#000066"> __、__ </span>  <span style="color:#000066"> __9\.27__ </span>

__ __  <span style="color:#760c04"> __五__ </span>  <span style="color:#760c04"> __\.  Butterworth__ </span>  <span style="color:#760c04"> __滤波器__ </span>  <span style="color:#760c04"> __:__ </span>

__  __  <span style="color:#000066"> __通常__ </span>  <span style="color:#000066"> __Butterworth__ </span>  <span style="color:#000066"> __滤波器的特性由频率响应的模平方函数给出。对__ </span>  <span style="color:#000066"> __N__ </span>  <span style="color:#000066"> __阶 __ </span>  <span style="color:#000066"> __Butterworth__ </span>  <span style="color:#000066"> __低通滤波器有：__ </span>

<span style="color:#000066"> __Butterworth__ </span>  <span style="color:#000066"> __滤波器的冲激响应是实信号__ </span>  <span style="color:#000066"> __，__ </span>

<span style="color:#000066"> __将      函数拓展到整个__ </span>  <span style="color:#000066"> __S__ </span>  <span style="color:#000066"> __平面有：__ </span>

<span style="color:#000066"> __表明__ </span>  <span style="color:#000066"> __N__ </span>  <span style="color:#000066"> __阶__ </span>  <span style="color:#000066"> __Butterworth__ </span>  <span style="color:#000066"> __低通滤波器模平方函数__ </span>  <span style="color:#760c04"> __全部__ </span>  <span style="color:#760c04"> __2N__ </span>  <span style="color:#760c04"> __个极点均匀分布在半径为     的圆周上__ </span>

<span style="color:#760c04"> __极点分布的特征：__ </span>

<span style="color:#000066"> __2N__ </span>  <span style="color:#000066"> __个极点等间隔均匀分布在半径为    的圆周上__ </span>  <span style="color:#000066"> __。__ </span>

__   __  <span style="color:#000066"> __轴上不会有极点。当__ </span>  <span style="color:#000066"> __N__ </span>  <span style="color:#000066"> __为奇数时在实轴上有极点，__ </span>  <span style="color:#000066"> __N__ </span>  <span style="color:#000066"> __为偶数时实轴上无极点。__ </span>

<span style="color:#000066"> __相邻两极点之间的角度差为     。__ </span>

<span style="color:#000066"> __极点分布总是关于原点对称的。__ </span>

__  __  <span style="color:#000066"> __要实现的滤波器应该是因果稳定系统，因此位于左半平面的__ </span>  <span style="color:#000066"> __N__ </span>  <span style="color:#000066"> __个极点一定是属于       的。__ </span>

<span style="color:#000066"> __    __ </span>  <span style="color:#000066"> __据此，确定出         后，也就可以综合出一个__ </span>  <span style="color:#000066"> __Butterworth __ </span>  <span style="color:#000066"> __滤波器。__ </span>

<span style="color:#000066"> __9\.8 __ </span>  <span style="color:#000066"> __系统函数的代数属性与系统的级联并联型结构__ </span>

<span style="color:#000066"> __System  Function  Algebra  and  Block  Diagram  Representations__ </span>

![](img/ch9_60.png)

![](img/ch9_61.png)

<span style="color:#760c04"> __二__ </span>  <span style="color:#760c04"> __\. __ </span>  <span style="color:#760c04"> __LTI__ </span>  <span style="color:#760c04"> __系统的级联和并联型结构__ </span>  <span style="color:#760c04"> __：__ </span>

<span style="color:#000066"> __LTI__ </span>  <span style="color:#000066"> __系统可以由一个__ </span>  <span style="color:#000066"> __LCCDE__ </span>  <span style="color:#000066"> __来描述。__ </span>

<span style="color:#000066"> __将     的分子和分母多项式因式分解__ </span>

__  __  <span style="color:#760c04"> __这表明：__ </span>  <span style="color:#000066"> __一个__ </span>  <span style="color:#000066"> __N__ </span>  <span style="color:#000066"> __阶的__ </span>  <span style="color:#000066"> __LTI__ </span>  <span style="color:#000066"> __系统可以分解为若干个二阶系统和一阶系统的级联。在__ </span>  <span style="color:#000066"> __N__ </span>  <span style="color:#000066"> __为偶数时，可全部组合成二阶系统的级联形式。__ </span>

<span style="color:#000066"> __如果__ </span>  <span style="color:#000066"> __N__ </span>  <span style="color:#000066"> __为奇数，则有一个一阶系统出现。__ </span>

__  __  <span style="color:#000066"> __将    展开为部分分式 __ </span>  <span style="color:#000066"> __\(__ </span>  <span style="color:#000066"> __假定    的分子阶数不高于分母阶数，所有极点都是单阶的），则有：__ </span>

<span style="color:#000066"> __将共轭成对的复数极点所对应的两项合并__ </span>  <span style="color:#000066"> __:__ </span>

__   __  <span style="color:#000066"> __N__ </span>  <span style="color:#000066"> __为偶数时又可将任意两个一阶项合并为二阶项，由此可得出系统的并联结构：__ </span>

<span style="color:#000066"> __The  Unilateral  Laplace  Transform__ </span>

__  __  <span style="color:#000066"> __单边拉氏变换是双边拉氏变换的特例。也就是因果信号的双边拉氏变换。单边拉氏变换对分析__ </span>  <span style="color:#000066"> __LCCDE __ </span>  <span style="color:#000066"> __描述的增量线性系统具有重要的意义。__ </span>

__  __  <span style="color:#000066"> __如果    是因果信号，对其做双边拉氏变换和做单边拉氏变换是完全相同的。__ </span>

__  __  <span style="color:#000066"> __单边拉氏变换也同样存在__ </span>  <span style="color:#000066"> __ROC __ </span>  <span style="color:#000066"> __。其__ </span>  <span style="color:#000066"> __ROC__ </span>  <span style="color:#000066"> __必然遵从因果信号双边拉氏变换时的要求，即：__ </span>  <span style="color:#760c04"> __一定位于最右边极点的右边。__ </span>

__  __  <span style="color:#000066"> __正因为这一原因，在讨论单边拉氏变换时，一般不再强调其__ </span>  <span style="color:#000066"> __ROC__ </span>  <span style="color:#000066"> __。__ </span>

<span style="color:#000066"> __    __ </span>  <span style="color:#000066"> __单边拉氏变换的反变换一定与双边拉氏变换的反变换相同。__ </span>

![](img/ch9_62.png)

__      __  <span style="color:#000066"> __与    不同，是因为    在     的部分对    有作用而对   没有任何作用所致。__ </span>

![](img/ch9_63.png)

__　__  <span style="color:#000066"> __单边拉氏变换的大部分性质与双边拉氏变换相同，但也有几个不同的性质。__ </span>

<span style="color:#760c04"> __1\. __ </span>  <span style="color:#760c04"> __时域微分__ </span>  <span style="color:#760c04"> __（__ </span>  <span style="color:#760c04"> __Differentiation in the Time Domain__ </span>  <span style="color:#760c04"> __）__ </span>

<span style="color:#760c04"> __2\. __ </span>  <span style="color:#760c04"> __时域积分__ </span>  <span style="color:#760c04"> __（__ </span>  <span style="color:#760c04"> __Integration in the Time Domain__ </span>  <span style="color:#760c04"> __）__ </span>

<span style="color:#760c04"> __3\.__ </span>  <span style="color:#760c04"> __时延性质__ </span>  <span style="color:#760c04"> __（__ </span>  <span style="color:#760c04"> __Time Shifting__ </span>  <span style="color:#760c04"> __）__ </span>

__       __  <span style="color:#000066"> __是因果信号时，单边拉氏变换的时延特性与双边变换时一致__ </span>  <span style="color:#000066"> __。__ </span>

<span style="color:#760c04"> __三__ </span>  <span style="color:#760c04"> __\.__ </span>  <span style="color:#760c04"> __利用单边拉氏变换求解增量线性系统__ </span>  <span style="color:#760c04"> __:__ </span>

__  __  <span style="color:#000066"> __单边拉氏变换特别适合于求解由__ </span>  <span style="color:#000066"> __LCCDE__ </span>  <span style="color:#000066"> __描述的增量线性系统。__ </span>

<span style="color:#000066"> __其中，第一项为__ </span>  <span style="color:#760c04"> __强迫响应__ </span>  <span style="color:#000066"> __，其它为__ </span>  <span style="color:#760c04"> __自然响应。__ </span>

<span style="color:#000066"> __9\.10 __ </span>  <span style="color:#000066"> __小结    __ </span>  <span style="color:#000066"> __Summary__ </span>

<span style="color:#000066"> __拉氏变换是傅氏变换的推广，在__ </span>  <span style="color:#000066"> __LTI__ </span>  <span style="color:#000066"> __系统分析中特别有用。它可以将微分方程变为代数方程，这对分析系统互联、系统结构、用系统函数表征系统、分析系统特性等都具有重要意义。__ </span>

<span style="color:#000066"> __ROC__ </span>  <span style="color:#000066"> __是双边拉氏变换的重要概念。离开了__ </span>  <span style="color:#000066"> __ROC__ </span>  <span style="color:#000066"> __，信号与双边拉氏变换的表达式将不再有一一对应的关系。__ </span>

<span style="color:#000066"> __ __ </span>  <span style="color:#000066"> __作为拉氏变换的几何表示，零极点图对分析系统的频率特性、零极点分布与系统特性的关系具有重要意义。从本质上讲，系统的特性完全是由系统函数的零极点分布决定的__ </span>

<span style="color:#000066"> __ 拉氏变换的许多性质对于在变换域分析__ </span>  <span style="color:#000066"> __LTI__ </span>  <span style="color:#000066"> __系统，具有重要作用。__ </span>

<span style="color:#000066"> __ 作为双边拉氏变换的特例，单边拉氏变换特别适用于分析增量线性系统。__ </span>

<span style="color:#000066"> __作业：__ </span>

<span style="color:#000066"> __9\.1__ </span>  <span style="color:#000066"> __、__ </span>  <span style="color:#000066"> __9\.5__ </span>  <span style="color:#000066"> __、__ </span>  <span style="color:#000066"> __9\.8__ </span>  <span style="color:#000066"> __、__ </span>  <span style="color:#000066"> __9\.14__ </span>  <span style="color:#000066"> __、__ </span>  <span style="color:#000066"> __9\.21__ </span>  <span style="color:#000066"> __、__ </span>  <span style="color:#000066"> __9\.22__ </span>  <span style="color:#000066"> __、__ </span>  <span style="color:#000066"> __9\.23__ </span>  <span style="color:#000066"> __、__ </span>  <span style="color:#000066"> __9\.33__ </span>  <span style="color:#000066"> __、__ </span>  <span style="color:#000066"> __9\.47__ </span>  <span style="color:#000066"> __、__ </span>  <span style="color:#000066"> __9\.48__ </span>

