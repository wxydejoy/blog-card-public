## 4.1 基本介绍

由于LaTeX编辑的数学公式颜值非常高，很多理工科研究领域的顶级期刊甚至明确要求投稿论文必须按照给定的LaTeX模板进行论文排版，这样做一方面能保证论文整体排版的美观程度，另一方面也能让生成出来的数学公式更加规范。一般而言，使用LaTeX编辑公式的一系列规则与数学公式的编写原则是一致的，例如，在LaTeX中，我们可以用`$\frac{\partial f}{\partial x}$`生成偏导数$\frac{\partial f}{\partial x}$。

### 4.1.1 数学公式环境

#### 美元符号

在LaTeX中生成数学公式也有一些基本规则，插入公式的方式有很多种，最基本的一种方式是使用美元符号，这种方式不仅在LaTeX适用，在Markdown中也是适用的，具体插入数学公式的方法是：

- 如果我们想插入行内公式，可以直接在两个美元符号中间编辑需要的公式。
- 如果想用美元符号插入行间公式，我们需要输入四个美元符号，与此同时，在四个美元符号中间编辑需要的公式。需要注意的是，这里生成的数学公式会自动居中对齐。

【**例1**】用美元符号分别在行内和行间生成一条简单的数学公式。

```tex
\documentclass[12pt]{article}
\begin{document}

$x+y=2$ is a simple linear equation

$$x+y=2$$

\end{document}
```
编译上述代码，得到幻灯片如图4-1-1所示。

<p align="center">
<img align="middle" src="docs/latex/chapter-4/graphics/example4_1_1.png" width="600" />
</p>

<center><b>图4-1-1</b> 编译后的幻灯片效果</center>

需要注意的是，LaTeX源文件中的美元符号一般都默认为申明数学公式环境，如果想要在文档中编译出美元符号，需要在美元符号前加上一个反斜线，这种做法同样适用于百分号，百分号一般被默认为注释功能。

#### `equation`环境

尽管美元符号可以在行间插入公式，但却没办法对公式进行编号。自动生成带有公式编号的行间公式需要用到数学公式环境`\begin{equation} \end{equation}`，使用数学公式环境`\begin{equation} \end{equation}`， LaTeX编译时会自动将公式进行居中对齐。

【**例2**】用`equation`数学公式环境生成一条带有编号的简单数学公式。

```tex
\documentclass[12pt]{article}
\begin{document}

\begin{equation}
x+y=2
\end{equation}

\end{document}
```

编译上述代码，得到幻灯片如图4-1-2所示。

<p align="center">
<img align="middle" src="docs/latex/chapter-4/graphics/example4_1_2.png" width="600" />
</p>

<center><b>图4-1-2</b> 编译后的幻灯片效果</center>

在`equation`环境中，如果不需要公式编号，只需要在数学公式环境中加上一个星号，例如，使用`\begin{equation*} \end{equation*}`就可以移除公式编号。

【**例3**】在数学公式环境中加上一个星号，来移除公式编号。

```tex
\documentclass[12pt]{article}
\begin{document}

\begin{equation*}
x+y=2
\end{equation*}

\end{document}
```

编译上述代码，得到幻灯片如图4-1-3所示。

<p align="center">
<img align="middle" src="docs/latex/chapter-4/graphics/example4_1_3.png" width="600" />
</p>

<center><b>图4-1-3</b> 编译后的幻灯片效果</center>

更进一步，在`equation`环境中，如果想对公式进行索引，可以使用`\label`和`\eqref`两个命令。

【**例4**】在数学公式环境中使用使用`\label`和`\eqref`两个命令对数学公式进行索引。

```tex
\documentclass[12pt]{article}
\begin{document}

Equation~\eqref{eq1} shows a simple formula.

\begin{equation}\label{eq1}
x+y=2
\end{equation}

\end{document}
```

编译上述代码，得到幻灯片如图4.1.4所示。

<p align="center">
<img align="middle" src="docs/latex/chapter-4/graphics/example4_1_4.png" width="600" />
</p>

<center><b>图4-1-4</b> 编译后的幻灯片效果</center>

#### `align`环境

在LaTeX中，除了`equation`数学公式环境，还有其他几种数学公式环境可以使用。我们要介绍的第一种是`\begin{align} \end{align}`，它主要用于数组型的数学表达式，`align`环境可以将公式进行自动对齐，它也能对每一条数学表达式分别进行公式编号。

【**例5**】使用`\begin{align} \end{align}`编译一个方程组。

```tex
\documentclass[12pt]{article}
\usepackage{amsmath}
\begin{document}

%% 使用align环境
\begin{align}
x+y&=2 \\
2x+y&=3
\end{align}

\end{document}
```
编译上述代码，得到幻灯片如图4-1-5所示。其中，`&`符号声明了不同行公式之间的对齐参照点。

<p align="center">
<img align="middle" src="docs/latex/chapter-4/graphics/example4_1_5.png" width="600" />
</p>

<center><b>图4-1-5</b> 编译后的幻灯片效果</center>


在`align`环境中，如果不需要公式编号，同样只需要在数学公式环境中加上一个星号即可，利用这一特性，我们可以使用`align`环境，定义多列公式。

【**例6**】使用`\begin{align*} \end{align*}`编译多列公式：

\begin{align*}
2x+1&=7 & 3y-2&=-5 & -5z+8&=-2 \\
  2x&=6 &   3y&=-3 &   -5z&=-10 \\
   x&=3 &    y&=-1 &     z&=2
\end{align*}

```tex
\documentclass[12pt]{article}
\usepackage{amsmath}
\begin{document}

\begin{align*}
2x+1&=7 & 3y-2&=-5 & -5z+8&=-2 \\
  2x&=6 &   3y&=-3 &   -5z&=-10 \\
   x&=3 &    y&=-1 &     z&=2
\end{align*}

\end{document}
```


需要注意的是，如果想对多行公式对齐，并且共用同一个公式编号，可以在`\begin{equation} \end{equation}`内使用`\begin{aligned} \end{aligned}`，这里的`aligned`与`align`功能类似。

【**例7**】在`\begin{equation} \end{equation}`内使用`\begin{aligned} \end{aligned}`编译多列公式：

\begin{equation}
\begin{aligned}
2x+1&=7 & 3y-2&=-5 & -5z+8&=-2 \\
  2x&=6 &   3y&=-3 &   -5z&=-10 \\
   x&=3 &    y&=-1 &     z&=2
\end{aligned}
\end{equation}

```tex
\documentclass[12pt]{article}
\usepackage{amsmath}
\begin{document}

\begin{equation}
\begin{aligned}
2x+1&=7 & 3y-2&=-5 & -5z+8&=-2 \\
  2x&=6 &   3y&=-3 &   -5z&=-10 \\
   x&=3 &    y&=-1 &     z&=2
\end{aligned}
\end{equation}

\end{document}
```


当然，我们也能只对`align`环境中的某一些公式进行编号，而其他公式不作编号。

> 参考[Eqnarray: numbering last line only.](https://latex.org/forum/viewtopic.php?f=46&t=4543)

【**例8**】使用`\begin{align} \end{align}`编译一个方程组，并且只对第2个方程进行编号。

```tex
\documentclass[12pt]{article}
\usepackage{amsmath}
\begin{document}

\begin{align}
x+y=2 \nonumber \\
2x+y=3
\end{align}

\end{document}
```

编译上述代码，得到幻灯片如图4-1-6所示。

<p align="center">
<img align="middle" src="docs/latex/chapter-4/graphics/example4_1_8.png" width="600" />
</p>

<center><b>图4-1-6</b> 编译后的幻灯片效果</center>

#### `gather`环境

我们要介绍的第二种数学公式环境是`\begin{gather} \end{gather}`，它既可以将公式进行居中对齐，也能对每一条数学表达式分别进行公式编号。同样的，如果想要移除公式编号，只需要在公式环境中加上星号即可。

【**例9**】使用`\begin{gather} \end{gather}`编译一个方程组。

```tex
\documentclass[12pt]{article}
\usepackage{amsmath}
\begin{document}

\begin{gather}
x+y=2 \\
2x+y=3
\end{gather}

\end{document}
```

编译上述代码，得到幻灯片如图4-1-7所示。

<p align="center">
<img align="middle" src="docs/latex/chapter-4/graphics/example4_1_9.png" width="600" />
</p>

<center><b>图4-1-7</b> 编译后的幻灯片效果</center>

### 4.1.2 基本格式调整

#### 字符类型

在文本编辑中，我们已经介绍了几种常见的字符类型，实际上，对于数学公式而言，书写时也可以设置不同的字符类型。以$X,Y,Z,x,y,z$为例，具体而言，

- 命令`\boldsymbol{X,Y,Z,x,y,z}`，编译后的效果为$\boldsymbol{X,Y,Z,x,y,z}$，使用之前需申明`\usepackage{amsmath}`；
- 命令`\mathrm{X,Y,Z,x,y,z}`，编译后的效果为$\mathrm{X,Y,Z,x,y,z}$；
- 命令`\mathit{X,Y,Z,x,y,z}`，编译后的效果为$\mathit{X,Y,Z,x,y,z}$；
- 命令`\mathbf{X,Y,Z,x,y,z}`，编译后的效果为$\mathbf{X,Y,Z,x,y,z}$；
- 命令`\mathsf{X,Y,Z,x,y,z}`，编译后的效果为$\mathsf{X,Y,Z,x,y,z}$；
- 命令`\mathtt{X,Y,Z,x,y,z}`，编译后的效果为$\mathtt{X,Y,Z,x,y,z}$；
- 命令`\boldmath{X,Y,Z,x,y,z}`，编译后的效果为${X,Y,Z,x,y,z}$；依赖于特定工具包，使用之前需申明`\usepackage{amssymb}`；
- 命令`\mathcal{X,Y,Z}`，编译后的效果为$\mathcal{X,Y,Z}$；
- 命令`\mathbb{X,Y,Z}`，依赖于特定工具包，使用之前需申明`\usepackage{amssymb, amsfonts}`，编译后的效果为$\mathbb{X,Y,Z}$，概率论与数理统计中常见的数学期望符号$\mathbb{E}$也是用该命令编译的，即`\mathbb{E}`；
- 命令`\mathfrak{X,Y,Z,x,y,z}`，依赖于特定工具包，使用之前需申明`\usepackage{amssymb, amsfonts, eufrak}`，编译后的效果为$\mathfrak{X,Y,Z,x,y,z}$。

【**例10**】使用`\boldmath`和`\unboldmath`对如下公式进行加粗：

\begin{equation}
x^{2}+y^{2}-\sin z=4
\end{equation}

```tex
\documentclass[12pt]{article}
\begin{document}

\begin{equation}
x^{2}+y^{2}-\sin z=4
\end{equation}

\boldmath
\begin{equation}
x^{2}+y^{2}-\sin z=4
\end{equation}
\unboldmath

\end{document}
```

编译上述代码，得到幻灯片如图4-1-8所示。

<p align="center">
<img align="middle" src="docs/latex/chapter-4/graphics/example4_1_10.png" width="600" />
</p>

<center><b>图4-1-8</b> 编译后的幻灯片效果</center>

除此之外，如果想在公式中插入正常的文本，可以使用`\text{}`命令，例如`T_{\text{start}}`编译后的效果为$T_{\text{start}}$。

#### 调整公式大小

如果想对单个公式调整公式字符大小，在美元符号插入的公式中，可以使用`\displaystyle、\textstyle、\scriptstyle和\scriptscriptstyle`等申明命令对公式大小进行调整，公式显示效果依次从小到大，这些命令一般放在公式前即可。

【**例11**】使用`\displaystyle`、`\textstyle`、`\scriptstyle`和`\scriptscriptstyle`这四种命令分别书写函数$f(x)=\sum_{i=1}^{n}\frac{1}{x_{i}}$。

```tex
\documentclass[12pt]{article}
\begin{document}

$\displaystyle{f(x)=\sum_{i=1}^{n}\frac{1}{x_{i}}}$, 
$\textstyle{f(x)=\sum_{i=1}^{n}\frac{1}{x_{i}}}$,
$\scriptstyle{f(x)=\sum_{i=1}^{n}\frac{1}{x_{i}}}$,
$\scriptscriptstyle{f(x)=\sum_{i=1}^{n}\frac{1}{x_{i}}}$.

\end{document}
```

编译上述代码，得到幻灯片如图4-1-9所示。

<p align="center">
<img align="middle" src="docs/latex/chapter-4/graphics/example4_1_11.png" width="600" />
</p>

<center><b>图4-1-9</b> 编译后的幻灯片效果</center>


在各类公式环境（如`equation`、`align`、`gather`）中，可以外使用一系列字符大小命令进行调整，例如用`\begingroup \endgroup`限定字符区域。

> 参考[Increase Equation Size](https://latex.org/forum/viewtopic.php?f=44&t=19788)。

【**例12**】在`\begingroup \endgroup`中使用字符大小命令`\small`和`\Large`对公式大小进行调整。

```tex
\documentclass[12pt]{article}
\usepackage{amsmath}
\begin{document}

%% Small size
\begingroup
\small
\begin{align}
x+y=2 \\
2x+y=3
\end{align}
\endgroup

%% Large size
\begingroup
\Large
\begin{align}
x+y=2 \\
2x+y=3
\end{align}
\endgroup

\end{document}
```
编译上述代码，得到幻灯片如图4-1-10所示。

<p align="center">
<img align="middle" src="docs/latex/chapter-4/graphics/example4_1_12.png" width="600" />
</p>

<center><b>图4.1.10</b> 编译后的幻灯片效果</center>

#### 其他格式调整

在`equation`、`align`等公式环境中，我们也可以通过数组`array`环境对数学公式进行对齐，例如，

【**例13**】使用`\begin{array} \end{array}`编译一个方程组，并添加半边花括号，如

$$\begin{equation}
\left\{\begin{array}{l}
x+y=2 \\
2x+y=3
\end{array}\right.
\end{equation}$$

```tex
\documentclass[12pt]{article}
\usepackage{amsmath}
\begin{document}

\begin{equation}
\left\{\begin{array}{l}
x+y=2 \\
2x+y=3
\end{array}\right.
\end{equation}

\begin{align}
\left\{\begin{array}{l}
x+y=2 \\
2x+y=3
\end{array}\right.
\end{align}

\end{document}
```

编译上述代码，得到幻灯片如图4-1-11所示。

<p align="center">
<img align="middle" src="docs/latex/chapter-4/graphics/example4_1_13.png" width="600" />
</p>

<center><b>图4-1-11</b> 编译后的幻灯片效果</center>

其中，对齐的方式有`l`（左侧对齐）、`c`（居中对齐）和`r`（右侧对齐）。

【**例14**】使用`\begin{array} \end{array}`编译公式，并让公式居中对齐。

```tex
\documentclass[12pt]{article}
\usepackage{amsmath, mathtools}

\begin{document}

\begin{equation}
\begin{array}{c@{\qquad}c}
A = B + C
\qquad\Rightarrow
& D = E - F, \\ \\
G = H
\qquad\Rightarrow
& K = P + Q + M.
\end{array}
\end{equation}

\end{document}
```

编译上述代码，得到幻灯片如图4-1-12所示。

<p align="center">
<img align="middle" src="docs/latex/chapter-4/graphics/example4_1_14.png" width="600" />
</p>

<center><b>图4-1-12</b> 编译后的幻灯片效果</center>

当公式过长时，还有一些工具包提供的环境可以让公式进行自动跨行，以工具包`breqn`为例，在使用时，用`\begin{dmath} \end{dmath}`即可。

### 练习题

> 打开LaTeX在线系统[https://www.overleaf.com](https://www.overleaf.com/project)或本地安装好的LaTeX编辑器，创建名为LaTeX_practice的项目，并同时新建一个以`.tex`为拓展名的源文件，完成以下几道练习题。


[1] 使用`\displaystyle`命令书写表达式$\max_{0\leq x\leq n-1}\prod_{i=1}^{c}f_{i}(x)$。

```tex
\documentclass[12pt]{article}
\begin{document}

${\max_{0\leq x\leq n-1}\prod_{i=1}^{c}f_{i}(x)}$.

\end{document}
```

[2] 在`align`环境中使用`\nonumber`命令只对如下方程组的第二个方程进行编号。

```tex
\documentclass[12pt]{article}
\usepackage{amsmath}

\begin{document}

%% 使用\nonumber命令去除第一个和第三个方程的编号
\begin{align}
(a+b)^2&=a^2+2ab+b^2 \\
(a-b)^2&=a^2-2ab+b^2 \\
(a+b)(a-b)&=a^2-b^2
\end{align}

\end{document}
```

[3] 使用`\begin{flalign} \end{flalign}`编译一个方程组。

> 【背景知识】在LaTeX的`amsmath`工具包中，使用`align`环境编译的数学公式会自动居中对齐。实际上，`amsmath`工具包还有一种使数学公式自动居左对齐的数学公式环境`flalign`。（参考[Left-Justified "align"](https://latex.org/forum/viewtopic.php?f=46&t=22839)）

```tex
\documentclass[12pt]{article}
\usepackage{amsmath}
\begin{document}

%% 使用flalign环境
\begin{}
&x+y=2& \\
&2x+y=3
\end{}

\end{document}
```

[4] 使用`\begin{array} \end{array}`编译如下表达式：

$$\begin{equation}
f(x)=\left\{
\begin{array}{c l}	
    x, & x>0, \\
    -x, & x<0.
\end{array}\right.
\end{equation}$$

```tex
\documentclass[12pt]{article}
\usepackage{amsmath}
\begin{document}

%% 提示：使用equation和array环境
\begin{equation}
f(x)=\left\{
\begin{}{c l}	
    x, & x>0, \\
    -x, & x<0.
\end{}\right.
\end{equation}

\end{document}
```

[5] 使用`\begin{subequations} ... \end{subequations}`生成子公式，并进行自动编号。

> 参考[How to properly label two aligned equations on the same line?](https://latex.org/forum/viewtopic.php?f=46&t=31577)

```tex
\documentclass[12pt]{article}
\usepackage{amsmath}

\begin{document}
\noindent
Here are two funny equations:
\begin{subequations}
\begin{equation}
\label{eq-a}
a = b
\end{equation}
\begin{equation}
\label{eq-b}
c = d
\end{equation}
\end{subequations}
Equation \eqref{eq-a} is not the same as equation \eqref{eq-b}. 
\end{document}
```

【回放】[**导言**](https://nbviewer.jupyter.org/github/xinychen/latex-cookbook/blob/main/chapter-4/section0.ipynb)

【继续】[**4.2 常用数学符号**](https://nbviewer.jupyter.org/github/xinychen/latex-cookbook/blob/main/chapter-4/section2.ipynb)

### License

<div class="alert alert-block alert-danger">
<b>This work is released under the MIT license.</b>
</div>
