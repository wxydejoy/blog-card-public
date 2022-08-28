## 4.2 常用数学符号

常用数学符号包括运算符号、标记符号、各类括号、空心符号及一些特殊函数。

### 4.2.1 运算符号

在初等数学中，最基本的运算规则是加减乘除。在LaTeX中，加法符号和减法符号就是+和-；而乘法符号有两种，第一种是`\times`，对应于符号$\times$，第二种是`\cdot`，对应于符号$\cdot$，除法符号的命令为`\div`。

【**例1**】书写加减乘除$3+5$、$3-5$、$3\times 5$、$3\cdot 5$、$3\div 5$和$3/5$。

```tex
\documentclass[12pt]{article}
\begin{document}

$$3+5$$        % 加法
$$3-5$$        % 减法
$$3\times 5$$  % 乘法
$$3\cdot 5$$   % 乘法
$$3\div 5$$    % 除法
$$3/5$$        % 除法

\end{document}
```

在加减的基础上，命令`\pm`（由plus和minus首字母构成）和`\mp`（由minus和plus首字母构成）分别对应着符号$\pm$和$\mp$。与加减乘除同样常用的运算符号还有大于号、小于号等。

【**例2**】书写$x<y$、$x>y$、$x\leq y$、$x\geq y$、$x\ll y$和$x\gg y$。

```tex
\documentclass[12pt]{article}
\begin{document}

$$x<y$$      % 小于
$$x>y$$      % 大于
$$x\leq y$$  % 小于或等于
$$x\geq y$$  % 大于或等于
$$x\ll y$$   % 远小于
$$x\gg y$$   % 远大于

\end{document}
```

对于集合而言，还有一些基本运算符号如$\cap$（`\cap`）、$\cup$（`\cup`）、$\supset$（`\supset`）、$\subset$（`\subset`）、$\supseteq$（`\supseteq`）、$\in$（`\in`）。除此之外，与“属于”命令`\in`相反的“不属于”命令为`\notin`，编译效果为$\notin$。

### 4.2.2 标记符号

在数学公式的编辑中，还有一些基本数学符号及表达式也非常重要，例如分式、上标、下标。LaTeX中用于书写分数和分式的基本命令为`\frac{分子}{分母}`，根据场景需要，也可以选用`\dfrac{分子}{分母}`和`\tfrac{分子}{分母}`。

【**例3**】书写分数$\frac{3}{5}$与分式$\frac{x}{y}$、$\frac{x+3}{y+5}$。

```tex
\documentclass[12pt]{article}
\begin{document}

$$\frac{3}{5}$$      % 分数
$$\frac{x}{y}$$      % 分式1
$$\frac{x+3}{y+5}$$  % 分式2

\end{document}
```

上标和下标在各类数学表达式中是非常常见的。

【**例4**】书写带上标的$x^{3}$、$x^{5}$、$x^{x+5}$和$x^{x^{3}+5}$。

```tex
\documentclass[12pt]{article}
\begin{document}

$$x^{3}$$
$$x^{5}$$
$$x^{x+5}$$
$$x^{x^{3}+5}$$

\end{document}
```

【**例5**】书写带下标的$x_{3}$、$x_{5}$、$x_{x+5}$、$x_{x_{3}+5}$和$x_{1},x_{2},\ldots,x_{n}$。

```tex
\documentclass[12pt]{article}
\begin{document}

$$x_{3}$$
$$x_{5}$$
$$x_{x+5}$$
$$x_{x_{3}+5}$$
$$x_{1},x_{2},\ldots,x_{n}$$

\end{document}
```

与上标和下标对应的还有各种“帽子”符号，即字母上面加符号。

【**例6**】书写$\hat{x}$、$\bar{x}$、$\tilde{x}$、$\vec{x}$和$\dot{x}$。

```tex
\documentclass[12pt]{article}
\begin{document}

$$\hat{x}$$
$$\bar{x}$$
$$\tilde{x}$$
$$\vec{x}$$
$$\dot{x}$$

\end{document}
```

与`\bar`作用相同的命令是`\overline`，不过`\overline`编译出来的“帽子”会比`\bar`宽一点，例如`\overline{xy}`可以编译出$\overline{xy}$，相比之下，`\bar{xy}`的编译效果为$\bar{xy}$。如果想要编译出比`\tilde`更宽一点的波浪线“帽子”，可以使用`\widetilde`，例如`\widetilde{xy}`可以编译出$\widetilde{xy}$，相比之下，`\tilde{xy}`的编译效果为$\tilde{xy}$。

> 参考[Tilde over the letter](https://latex.org/forum/viewtopic.php?f=48&t=11388)

根号同样是数学表达式中的常见符号，在LaTeX中，根号的命令为`\sqrt{}`，使用默认设置，生成的表达式为二次方根，如果想要设置为三次方根，则需要调整默认设置，即`\sqrt[3]{}`，以此类推，可以设置四次方根等。

【**例7**】书写根式$\sqrt{3}$、$\sqrt[3]{5}$、$\sqrt{x+y}$、$\sqrt{x^{3}+y^{5}}$、$\sqrt{1+\sqrt{x}}$。

```tex
\documentclass[12pt]{article}
\begin{document}

$$\sqrt{3}$$
$$\sqrt[3]{5}$$
$$\sqrt{x+y}$$
$$\sqrt{x^{3}+y^{5}}$$
$$\sqrt{1+\sqrt{x}}$$

\end{document}
```

【**例8**】书写分式和根式组合的表达式$\frac{\sqrt{x+3}}{\sqrt{y+5}}$。

```tex
\documentclass[12pt]{article}
\begin{document}

$$\frac{\sqrt{x+3}}{\sqrt{y+5}}$$

\end{document}
```




### 4.2.3 各类括号

在数学表达式中，括号的用处和种类都非常多，例如最常见的小括号、中括号、大括号（即花括号）。

【**例9**】书写数学表达式$x\left(\frac{1}{y}+1\right)$、$x\left[\frac{1}{y}+1\right]$和$x\left\{\frac{1}{y}+1\right\}$。

```tex
\documentclass[12pt]{article}
\begin{document}

$$x\left(\frac{1}{y}+1\right)$$
$$x\left[\frac{1}{y}+1\right]$$
$$x\left\{\frac{1}{y}+1\right\}$$

\end{document}
```
有时候，由于公式过长等原因，我们也可以在需要分行处插入`\\`将括号内的公式切分成多行。

> 参考[Bracket size proble: Split multi-line equations](https://latex.org/forum/viewtopic.php?f=46&t=4823)

【**例10**】运用双斜杠`\\`将括号内的公式切分成多行.

\begin{equation}
\begin{aligned}
\Bigl(a+\frac{b}{2}+\frac{c}{3}++\frac{d}{4}+\frac{e}{5}++\frac{f}{6}++\frac{g}{7}++\frac{h}{8} \\
      +\frac{i}{9}+\frac{j}{10}+\frac{k}{11}++\frac{l}{12}+\frac{m}{13}++\frac{n}{14}++\frac{o}{15}+\cdots\Bigr)
\end{aligned}
\end{equation}

```tex
\documentclass[12pt]{article}
\usepackage{amsmath}

\begin{document}

\begin{equation}
\begin{aligned}
\Bigl(a+\frac{b}{2}+\frac{c}{3}++\frac{d}{4}+\frac{e}{5}++\frac{f}{6}++\frac{g}{7}++\frac{h}{8} \\
      +\frac{i}{9}+\frac{j}{10}+\frac{k}{11}++\frac{l}{12}+\frac{m}{13}++\frac{n}{14}++\frac{o}{15}+\cdots\Bigr)
\end{aligned}
\end{equation}

\end{document}
```

在这里，我们可以使用一系列命令代替最常用的`\left`和`\right`组合，如`\bigl`和`\bigr`组合、`\Bigl`和`\Bigr`组合、`\biggl`和`\biggr`组合、`\Biggl`和`\Biggr`组合来控制括号大小。

【**例11**】运用`\bigl`和`\bigr`组合、`\Bigl`和`\Bigr`组合、`\biggl`和`\biggr`组合、`\Biggl`和`\Biggr`组合来控制括号大小.

```tex
\documentclass[12pt]{article}
\usepackage{amsmath}

\begin{document}

\begin{equation}

\left(x+y=z \right)
\bigl(x+y=z \bigr)
\Bigl(x+y=z \Bigr)
\biggl(x+y=z \biggr)
\Biggl(x+y=z \Biggr)

\end{equation}

\end{document}
```

编译上述代码，得到幻灯片如图4-2-1所示。

<p align="center">
<img align="middle" src="latex/chapter-4/graphics/example4_2_11.png" width="600" />
</p>

<center><b>图4-2-1</b> 编译后的幻灯片效果</center>

在数学公式编辑中，除了以上常见的括号，也有一些广义的“括号”。

【**例12**】书写数学表达式$x\left|\frac{1}{y}+1\right|$、$x\left\|\frac{1}{y}+1\right\|$、$\left<\frac{1}{x},\frac{1}{y}\right>$和$\langle\frac{1}{x},\frac{1}{y}\rangle$。

```tex
\documentclass[12pt]{article}
\begin{document}

$$x\left|\frac{1}{y}+1\right|$$
$$x\left\|\frac{1}{y}+1\right\|$$
$$\left<\frac{1}{x},\frac{1}{y}\right>$$
$$\langle\frac{1}{x},\frac{1}{y}\rangle$$

\end{document}
```

在这里，使用半边括号，也能书写出导数的表达式。

【**例13**】书写导数$\left.\frac{dy}{dx}\right|_{x=1}$。

```tex
\documentclass[12pt]{article}
\begin{document}

$$\left.\frac{dy}{dx}\right|_{x=1}$$

\end{document}
```



### 4.2.4 空心符号

在数学表达式中，我们有时候会用到一些约定俗成的空心符号表示集合，这包括：

- 空心R符号$\mathbb{R}$表示由所有实数构成的集合。
- 空心Z符号$\mathbb{Z}$表示由所有整数构成的集合。
- 空心N符号$\mathbb{N}$表示由所有非负整数构成的集合，如果要表示正整数，使用符号$\mathbb{N}_{+}$即可。
- 空心C符号$\mathbb{C}$表示由所有复数构成的集合。

需要注意的是，要想让LaTeX成功编译出这些空心符号，我们需要调用特定的工具包，即`\usepackage{amsfonts}`，一般而言，为了保证公式的编译不出现意外，还会用到其他工具包，即`\usepackage{amsfonts, amssymb, amsmath}`。当然，除了这些，还有许多其他符号，这里不再一一赘述。

【**例14**】书写表达式$X\in\mathbb{R}^{m\times n}$。

```tex
\documentclass[12pt]{article}
\usepackage{amsfonts}

\begin{document}

$$X\in\mathbb{R}^{m\times n}$$

\end{document}
```

【**例15**】使用工具包`bbold`中的`\mathbb`命令书写空心的1、2、3、4、5.

> 参考[The Identity Matrix](https://latex.org/forum/viewtopic.php?f=46&t=20753)

```tex
\documentclass[12pt]{article}
\usepackage{bbold}

\begin{document}

$$\mathbb{1},\mathbb{2},\mathbb{3},\mathbb{4},\mathbb{5}$$

\end{document}
```

编译上述代码，得到幻灯片如图4-2-2所示。

<p align="center">
<img align="middle" src="latex/chapter-4/graphics/example4_2_15.png" width="600" />
</p>

<center><b>图4-2-2</b> 编译后的幻灯片效果</center>

### 4.2.5 特殊函数

上标很多时候是用来表示变量的幂，例如`x^{2}`表示$x$的平方，由此可以用上标书写出指数函数如$y=x^{2}$等。与指数函数对应的一类常用函数被称为对数函数，是指数函数的反函数，LaTeX提供了一些跟对数函数相关的命令，包括`\log`、`\ln`，在命令`\log`中，我们可以自行设置底数，而命令`\ln`则表示底数为自然数的对数。

【**例16**】书写对数函数$y=\log_{2}x$和$y=\ln x$。

```tex
\documentclass[12pt]{article}
\begin{document}

$$y=\log_{2}x$$
$$y=\ln x$$

\end{document}
```

有时候，为了简化数学表达式，我们可能会采用求和或者连乘的写法，在LaTeX中，求和符号对应的命令为`\sum_{下标}^{上标}`，连乘符号对应的命令为`\prod_{下标}^{上标}`。

【**例17**】书写求和公式$$\sum_{i=1}^{n}x_{i}$$和连乘公式$$\prod_{i=1}^{n}x_{i}$$

```tex
\documentclass[12pt]{article}
\begin{document}

$$\sum_{i=1}^{n}x_{i}$$
$$\prod_{i=1}^{n}x_{i}$$

\end{document}
```

另外，在初等数学的几何中，我们学过了正弦、余弦等，这些在LaTeX都有定义好的命令可供直接使用。

【**例18**】书写正弦函数$y=\sin x$、反正弦函数$y=\arcsin x$、余弦函数$y=\cos x$、反余弦函数$y=\arccos x$、正切函数$y=\tan x$和反正切函数$y=\arctan x$。

```tex
\documentclass[12pt]{article}
\begin{document}

$$y=\sin x$$
$$y=\arcsin x$$
$$y=\cos x$$
$$y=\arccos x$$
$$y=\tan x$$
$$y=\arctan x$$

\end{document}
```


### 练习题

> 打开LaTeX在线系统[https://www.overleaf.com](https://www.overleaf.com/project)或本地安装好的LaTeX编辑器，创建名为LaTeX_practice的项目，并同时新建一个以`.tex`为拓展名的源文件，完成以下几道练习题。

[1] 使用工具包`bbm`中的`\mathbbm`命令书写空心的1和2。

> 参考[Blackboard bold numbers; trouble with \mathbb](https://latex.org/forum/viewtopic.php?f=48&t=17427)

```tex
\documentclass[12pt]{article}
% 请在此处申明使用bbm工具包

\begin{document}

$$\mathbbm{1},\mathbbm{2}$$

\end{document}
```


【回放】[**4.1 基本介绍**](https://nbviewer.jupyter.org/github/xinychen/latex-cookbook/blob/main/chapter-4/section1.ipynb)

【继续】[**4.3 希腊字母**](https://nbviewer.jupyter.org/github/xinychen/latex-cookbook/blob/main/chapter-4/section3.ipynb)

### License

<div class="alert alert-block alert-danger">
<b>This work is released under the MIT license.</b>
</div>
