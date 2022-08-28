## 7.3 高级功能

在本节中，我们将介绍除直线以外的复杂功能，如:非规则曲线、复杂函数绘图、区域填充、填写标签等等。


### 7.3.1 矩形、圆形、曲线

我们可以通过`\draw (x,y) rectangle (w,h);`的方式绘制一个矩形，其左下角坐标位于点($x$,$y$)处，长度为$w$，高度为$h$。类似地，我们也可以通过`\draw (x,y) circle [radius=r];`的方式绘制一个圆形，其圆心落在点($x$,$y$)处，半径为$r$。除此之外，我们可以通过`\draw (x,y) arc [radius=r, start angle=a1, end angle=a2]`的方式绘制一条弧线，它从点($x$,$y$)处开始绘制，该弧线曲率半径为$r$，其起始角度为所对应曲率圆的$a_1$处，终止角度为所对应曲率圆的$a_2$处。

【**例7-27**】按上述介绍，绘制矩形、圆形以曲线。

```tex
\documentclass[12pt]{article}
\usepackage{tikz}
\begin{document}

\begin{tikzpicture}

    \draw [red] (0,0) rectangle (1.5,1);
    \draw [blue, ultra thick] (3,0.5) circle [radius=0.5];
    \draw [green] (6,0) arc [radius=1.5, start angle=45, end angle= 100];

\end{tikzpicture}

\end{document}
```
编译上述代码，得到图形如图7.3.1所示。

<p align="center">
<img align="middle" src="latex/chapter-7/graphics/example_sec7_3_1.png" width="350" />
</p>

<center><b>图7.3.1</b> 编译后的图形效果</center>


### 7.3.2 平滑过渡曲线

在绘图时，一种不突兀地连接两条直线的方式是采用平滑过渡圆角/曲线。在本节中，我们将介绍两种平滑过渡曲线的绘制方法：绘制带圆角的曲线和绘制过渡曲线。

【**例7-28**】绘制带圆角的坐标系。

```tex
\documentclass[12pt]{article}
\usepackage{tikz}
\begin{document}

\begin{tikzpicture}

    \draw [<->, rounded corners, thick, purple] (0,2) -- (0,0) -- (3,0);

\end{tikzpicture}

\end{document}
```
编译上述代码，得到图形如图7.3.2所示。

<p align="center">
<img align="middle" src="latex/chapter-7/graphics/example_sec7_3_2.png" width="200" />
</p>

<center><b>图7.3.2</b> 编译后的图形效果</center>

【**例7-29**】绘制过渡曲线。

```tex
\documentclass[12pt]{article}
\usepackage{tikz}
\begin{document}

\begin{tikzpicture}
    
    \draw[<-, thick] (0,2) -- (0,0.5);
    \draw[thick,red] (0,0.5) to [out=270,in=180] (0.5,0);
    \draw[->, thick] (0.5,0) -- (3,0);

\end{tikzpicture}

\end{document}
```
编译上述代码，得到图形如图7.3.3所示。

<p align="center">
<img align="middle" src="latex/chapter-7/graphics/example_sec7_3_3.png" width="200" />
</p>

<center><b>图7.3.3</b> 编译后的图形效果</center>

【**例7-30**】利用多段过渡曲线绘制S曲线。

```tex
\documentclass[12pt]{article}
\usepackage{tikz}
\begin{document}

\begin{tikzpicture}

    \draw [<->,thick, blue] (0,0) to [out=90,in=180] (1,1) to [out=0,in=180] (3,0) to [out=0,in=-90] (4,1) ;

\end{tikzpicture}

\end{document}
```
编译上述代码，得到图形如图7.3.4所示。

<p align="center">
<img align="middle" src="latex/chapter-7/graphics/example_sec7_3_4.png" width="200" />
</p>

<center><b>图7.3.4</b> 编译后的图形效果</center>

### 7.3.3 根据函数绘制曲线
`TikZ`宏包的强大之处在于，它还提供了可供绘制函数的数学引擎。在此我们先给出一个示例，再详细讲解如何利用该宏包绘制函数所对应的曲线。

【**例7-31**】利用函数绘制正弦曲线。

```tex
\documentclass[12pt]{article}
\usepackage{tikz}
\begin{document}

\begin{tikzpicture}[xscale=0.01,yscale=1]

    \draw [<->] (0,1) -- (0,0) -- (370,0);
    \draw[green, thick, domain=0:360] plot (\x, {sin(\x)}); % 这里需要注意带上{}
    
\end{tikzpicture}

\end{document}
```
编译上述代码，得到图形如图7.3.5所示。

<p align="center">
<img align="middle" src="latex/chapter-7/graphics/example_sec7_3_5.png" width="350" />
</p>

<center><b>图7.3.5</b> 编译后的图形效果</center>

在上述例子中，`domain`指令声明了横坐标`x`的范围。在本示例中，我们利用`sin`函数绘制了一段正弦曲线。

除了本示例中的正弦曲线`sin`函数，我们还可以调用大量其他函数，在此列举一部分作为示例：
阶乘函数：`factorial(\x)`、
平方根函数：`sqrt(\x)`、
幂函数：`pow(\x,y)`（该函数为$x^y$）、
指数函数：`exp(\x)`、
对数函数：`ln(\x)`、`log10(\x)`、`log2(\x)`、
绝对值函数：`abs(\x)`、
取余函数：`mod(\x,y)`（即求$x$被$y$除后的余数）、
圆整函数：`round(\x)`、`floor(\x)`、`ceil(\x)`、
三角函数：`sin(\x)`、`cos(\x)`、`tan(\x)`等等。`sin(\x)`、`cos(\x)`、`tan(\x)`
值得注意的是，在三角函数中，通常默认自变量$x$以度（°）为单位。若要采用弧度制，则需要将函数分别改写为`sin(\x r)`、`cos(\x r)`、`tan(\x r)`。
除了这部分常用函数之外，我们通常还会使用两个常数：`e`（$e=2.718281828$）和`pi`（$pi= 3.141592654$）。

通过组合以上基本函数，我们可以实现更复杂的函数功能。

【**例7-32**】通过组合基本函数实现复杂函数的绘图。

```tex
\documentclass[12pt]{article}
\usepackage{tikz}
\begin{document}

\begin{tikzpicture}[yscale=1.5]

    \draw [thick, ->] (0,0) -- (6.5,0);
    \draw [thick, ->] (0,-1.1) -- (0,1.1);
    \draw [green,domain=0:2*pi] plot (\x, {(sin(\x r)* ln(\x+1))/2});
    \draw [red,domain=0:pi] plot (\x, {sin(\x r)});
    \draw [blue, domain=pi:2*pi] plot (\x, {cos(\x r)*exp(\x/exp(2*pi))});

\end{tikzpicture}
\end{document}
```
编译上述代码，得到图形如图7.3.6所示。

<p align="center">
<img align="middle" src="latex/chapter-7/graphics/example_sec7_3_6.png" width="350" />
</p>

<center><b>图7.3.6</b> 编译后的图形效果</center>

### 7.3.4 简单图形的区域填充
我们可以在简单图形的基础上进行区域填充。

【**例7-33**】简单形状的区域填充。

```tex
\documentclass[12pt]{article}
\usepackage{tikz}
\begin{document}

\begin{tikzpicture}[yscale=1.5]

    \draw [fill=red,ultra thick] (0,0) rectangle (1,1);
    \draw [fill=red,ultra thick,red] (2,0) rectangle (3,1); % 这里的第二个red声明了区域周围边框线的颜色
    \draw [blue, fill=blue] (4,0) -- (5,1) -- (4.75,0.15) -- (4,0);
    \draw [fill] (7,0.5) circle [radius=0.1];
    \draw [fill=orange] (9,0) rectangle (11,1);
    \draw [fill=white] (9.25,0.25) rectangle (10,1.5);


\end{tikzpicture}
\end{document}
```
编译上述代码，得到图形如图7.3.7所示。

<p align="center">
<img align="middle" src="latex/chapter-7/graphics/example_sec7_3_7.png" width="500" />
</p>

<center><b>图7.3.7</b> 编译后的图形效果</center>

如上例中的注释所提，我们可以通过声明图形边框线的颜色来对边框线进行个性化更改。若并不希望出现边框线，我们可以采用`path`命令替换`\draw`命令。

【**例7-34**】简单形状的区域填充。

```tex
\documentclass[12pt]{article}
\usepackage{tikz}
\begin{document}

\begin{tikzpicture}[yscale=1.5]

    \path [fill=red,thick] (0,0) rectangle (1.5,1);
    \draw [fill=red,thick] (2,0) rectangle (3.5,1);

\end{tikzpicture}
\end{document}
```
编译上述代码，得到图形如图7.3.8所示。

<p align="center">
<img align="middle" src="latex/chapter-7/graphics/example_sec7_3_8.png" width="200" />
</p>

<center><b>图7.3.8</b> 编译后的图形效果</center>

### 7.3.5 在图形中填写标签
在绘图时，在合适的位置加入适当的文字进行说明，对内容的表达具有很重要的作用。在本节中，我们将通过`\node`来实现这一功能。

【**例7-35**】在直角坐标系中插入文字。

```tex
\documentclass[12pt]{article}
\usepackage{tikz}
\begin{document}

\begin{tikzpicture}[yscale=1.5]

    \draw [thick, <->] (0,2) -- (0,0) -- (2,0);
    \node at (1,1) {good};

\end{tikzpicture}
\end{document}
```
编译上述代码，得到图形如图7.3.9所示。

<p align="center">
<img align="middle" src="latex/chapter-7/graphics/example_sec7_3_9.png" width="200" />
</p>

<center><b>图7.3.9</b> 编译后的图形效果</center>

在上例中，我们给出了一个简单的示范，我们将文字"good"的中心位置固定在坐标`(1,1)`点处。当然，我们也可以通过命令，控制文字与所声明坐标的相对位置，如：在坐标上方、下方、左侧、右侧。

【**例7-36**】在(1,1)点下方插入文字。

```tex
\documentclass[12pt]{article}
\usepackage{tikz}
\begin{document}

\begin{tikzpicture}

    \draw [thick, <->] (0,2) -- (0,0) -- (2,0);
    \draw [fill] (1,1) circle [radius=0.025];
    \node [below] at (1,1) {good};

\end{tikzpicture}
\end{document}
```
编译上述代码，得到图形如图7.3.10所示。

<p align="center">
<img align="middle" src="latex/chapter-7/graphics/example_sec7_3_10.png" width="200" />
</p>

<center><b>图7.3.10</b> 编译后的图形效果</center>

【**例7-37**】在(1,1)点上方、下方、左侧、右侧插入文字。

```tex
\documentclass[12pt]{article}
\usepackage{tikz}
\begin{document}

\begin{tikzpicture}

    \draw [thick, <->] (0,2) -- (0,0) -- (2,0);
    \draw [fill] (1,1) circle [radius=0.025];
    \node [below] at (1,1) {below};
    \node [above] at (1,1) {above};
    \node [left] at (1,1) {left};
    \node [right] at (1,1) {right};

\end{tikzpicture}
\end{document}
```
编译上述代码，得到图形如图7.3.11所示。

<p align="center">
<img align="middle" src="latex/chapter-7/graphics/example_sec7_3_11.png" width="200" />
</p>

<center><b>图7.3.11</b> 编译后的图形效果</center>

【**例7-38**】在(1,1)点左上方、左下方、右上方、右下方插入文字。

```tex
\documentclass[12pt]{article}
\usepackage{tikz}
\begin{document}

\begin{tikzpicture}[xscale=2]

    \draw [thick, <->] (0,2) -- (0,0) -- (2,0);
    \draw [fill] (1,1) circle [radius=0.025];
    \node [below right, red] at (1,1) {below right};
    \node [above left, green] at (1,1) {above left};
    \node [below left, purple] at (1,1) {below left};
    \node [above right, magenta] at (1,1) {above right};

\end{tikzpicture}
\end{document}
```
编译上述代码，得到图形如图7.3.12所示。

<p align="center">
<img align="middle" src="latex/chapter-7/graphics/example_sec7_3_12.png" width="200" />
</p>

<center><b>图7.3.12</b> 编译后的图形效果</center>


【**例7-39**】在(1,1)点处插入数学符号$\theta$。

```tex
\documentclass[12pt]{article}
\usepackage{tikz}
\begin{document}

\begin{tikzpicture}

    \draw [thick, <->] (0,2) -- (0,0) -- (2,0);
    \node [below right] at (2,0) {$x$};
    \node [left] at (0,2) {$y$};
    \draw[fill] (1,1) circle [radius=.5pt];
    \node[above right] at (1,1) {$\theta$};
    
\end{tikzpicture}
\end{document}
```
编译上述代码，得到图形如图7.3.13所示。

<p align="center">
<img align="middle" src="latex/chapter-7/graphics/example_sec7_3_13.png" width="200" />
</p>

<center><b>图7.3.13</b> 编译后的图形效果</center>


【回放】[**7.2 节点介绍**](https://nbviewer.jupyter.org/github/xinychen/latex-cookbook/blob/main/chapter-7/section2.ipynb)

【继续】[**7.4 复杂模型实战解析**](https://nbviewer.jupyter.org/github/xinychen/latex-cookbook/blob/main/chapter-7/section4.ipynb)

### License

<div class="alert alert-block alert-danger">
<b>This work is released under the MIT license.</b>
</div>