## 7.1 基本介绍

`TikZ`宏包是在LaTeX中创建图形元素的最复杂和最强大的工具。在本节中，我们将通过一些简单的示例来介绍如何在`tikzpicture`环境中创建基本的图形元素，如：线、点、曲线、圆、矩形等。

### 7.1.1 使用`tikzpicture`环境创建图形元素

首先，我们需要通过`\usepackage{tikz}`命令调用`TikZ`宏包。在绘制图形之前，需要声明`tikzpicture`环境。在此我们先给出两个用`TikZ`绘图的例子，其后再进一步详细介绍具体的绘图命令。

【**例7-1**】使用`tikzpicture`环境制作一个简单的图形。

```tex
\documentclass[12pt]{article}
\usepackage{tikz}
\begin{document}

\begin{tikzpicture}

  \draw[red,fill=red] (0,0) .. controls (0,0.75) and (-1.5,1.00) .. (-1.5,2)  arc (180:0:0.75)  -- cycle;
  \draw[red,fill=red] (0,0) .. controls (0,0.75) and ( 1.5,1.00) .. ( 1.5,2)  arc (0:180:0.75) -- cycle;
  
\end{tikzpicture}

\end{document}
```
编译上述代码，得到图形如图7.1.1所示。

<p align="center">
<img align="middle" src="latex/chapter-7/graphics/example_sec7_1_1.png" width="200" />
</p>

<center><b>图7.1.1</b> 编译后的图形效果</center>


【**例7-2**】使用`tikz`宏包中的`tikzpicture`环境创建一个张量网络图。

```tex
\documentclass[border=0.3cm, 11pt]{standalone}
\usepackage{tikz}
\usepackage{amsmath, amssymb, amsfonts}
\usepackage{color}

\begin{document}
\begin{tikzpicture}

\node[circle, line width = 0.4mm, draw = black, fill = red!45, inner sep = 0pt, minimum size = 0.4cm] (w) at (0, 0) {};
\node at (0, 0.5) {\small{$\boldsymbol{W}$}};

\node[circle, line width = 0.4mm, draw = black, fill = red!45, inner sep = 0pt, minimum size = 0.4cm] (g) at (1.5, 0) {};
\node at (1.5, 0.5) {\small{$\boldsymbol{\mathcal{G}}$}};

\node[circle, line width = 0.4mm, draw = black, fill = red!45, inner sep = 0pt, minimum size = 0.4cm] (v) at (3, 0) {};
\node at (3, 0.5) {\small{$\boldsymbol{V}$}};

\path [draw, line width = 0.4mm, -] (w) edge (g);
\node at (0.75, 0.25) {\small{$R$}};
\path [draw, line width = 0.4mm, -] (g) edge (v);
\node at (2.25, 0.25) {\small{$K$}};

\draw [line width = 0.4mm] (w) -- (0, -0.8);
\node at (-0.25, -0.4) {\small{$N$}};
\draw [line width = 0.4mm] (g) -- (1.5, -0.8);
\node at (1.5-0.25, -0.4) {\small{$N$}};
\draw [line width = 0.4mm] (v) -- (3, -0.8);
\node at (3-0.25, -0.4) {\small{$d$}};

\end{tikzpicture}
\end{document}
```

编译上述代码，得到图形如图7.1.2所示。

<p align="center"> 
<img align="middle" src="latex/chapter-7/graphics/example_sec7_1_2.png" width="350" />
</p>

<center><b>图7.1.2</b> 编译后的图形效果</center>


### 7.1.2 绘制直线

我们在这两个示例中可以感受到`TikZ`功能的强大之处。但是，这些复杂的图形都是由最基本的点、线和面所构成。在本小节中，我们将从绘制一条直线开始，入门这个强大的LaTeX绘图工具。首先，画一条直线需要给出起始点坐标和终止点坐标，我们可以简单地通过如下代码
```tex
\begin{tikzpicture}

    \draw (x1,y1) -- (x2,y2); % 这里(x1,y1)和(x2,y2)在编译时均需替换成具体坐标数值。
    
\end{tikzpicture}
```
来实现绘制一条从$(x_1,y_1)$到$(x_2,y_2)$的直线的功能。值得注意的是，在默认情况下，坐标系均以`cm`为单位。

【**例7-3**】尝试绘制一条直线。

```tex
\documentclass[12pt]{article}
\usepackage{tikz}
\begin{document}

\begin{tikzpicture}

    \draw (-2,0) -- (2,0);
    
\end{tikzpicture}

\end{document}
```

编译上述代码，得到图形如图7.1.3所示。
<p align="center"> 
<img align="middle" src="latex/chapter-7/graphics/example_sec7_1_3.png" width="200" />
</p>

<center><b>图7.1.3</b> 编译后的图形效果</center>


进一步地，我们可以通过设定一系列的坐标点，来实现多条线段的连续绘制。

【**例7-4**】多条线段连续绘制。

```tex
\documentclass[12pt]{article}
\usepackage{tikz}
\begin{document}

\begin{tikzpicture}

    \draw (-2,0) -- (2,0) -- (2,2) -- (-2,2) -- (-2,0);
    
\end{tikzpicture}

\end{document}
```

编译上述代码，得到图形如图7.1.4所示。
<p align="center"> 
<img align="middle" src="latex/chapter-7/graphics/example_sec7_1_4.png" width="200" />
</p>

<center><b>图7.1.4</b> 编译后的图形效果</center>

也可以通过增加多行命令，实现多段线条的分开绘制。

【**例7-5**】多段线条分开绘制。
```tex
\documentclass[12pt]{article}
\usepackage{tikz}
\begin{document}

\begin{tikzpicture}

    \draw (-2,0) -- (2,0) -- (2,2) -- (-2,2) -- (-2,0);
    \draw (0,4) -- (0,-2);
    \draw (3,-2) -- (3,4) -- (7,4) -- (7,-2) -- (3,-2);
    \draw (4,3) -- (6,3); \draw (4,1) -- (6,1); \draw (4,-1) -- (6,-1);
    \draw (5,3) -- (5,-1); \draw (5.75,0.25) -- (6.25,-0.25);
    
\end{tikzpicture}

\end{document}
```

编译上述代码，得到图形如图7.1.5所示。
<p align="center"> 
<img align="middle" src="latex/chapter-7/graphics/example_sec7_1_5.png" width="200" />
</p>

<center><b>图7.1.5</b> 编译后的图形效果</center>

值得注意的是，在`tikzpicture`环境中，像`Matlab`语言一样，我们需要采用`;`符号来标记一个指令的结束。这样的指令结束标记让我们不但可以在多行完成一条指令，同时也可以在一行内实现多条指令。

# 7.1.3 图形缩放

在上小节中，我们绘制图形需要给出精确的坐标点。但是在绘制好之后，如果需要调整图形大小，我们可以采用`scale`的方式对图形进行缩放。

【**例7-6**】整体缩放。
```tex
\documentclass[12pt]{article}
\usepackage{tikz}
\begin{document}

\begin{tikzpicture}[scale=0.5]

    \draw (-2,0) -- (2,0) -- (2,2) -- (-2,2) -- (-2,0);
    \draw (0,4) -- (0,-2);
    \draw (3,-2) -- (3,4) -- (7,4) -- (7,-2) -- (3,-2);
    \draw (4,3) -- (6,3); \draw (4,1) -- (6,1); \draw (4,-1) -- (6,-1);
    \draw (5,3) -- (5,-1); \draw (5.75,0.25) -- (6.25,-0.25);

\end{tikzpicture}

\end{document}
```

编译上述代码，得到图形如图7.1.6所示。
<p align="center"> 
<img align="middle" src="latex/chapter-7/graphics/example_sec7_1_6.png" width="100" />
</p>

<center><b>图7.1.6</b> 编译后的图形效果</center>

【**例7-7**】横向缩放。
```tex
\documentclass[12pt]{article}
\usepackage{tikz}
\begin{document}

\begin{tikzpicture}[xscale=1.5]

    \draw (-2,0) -- (2,0) -- (2,2) -- (-2,2) -- (-2,0);
    \draw (0,4) -- (0,-2);
    \draw (3,-2) -- (3,4) -- (7,4) -- (7,-2) -- (3,-2);
    \draw (4,3) -- (6,3); \draw (4,1) -- (6,1); \draw (4,-1) -- (6,-1);
    \draw (5,3) -- (5,-1); \draw (5.75,0.25) -- (6.25,-0.25);

\end{tikzpicture}

\end{document}
```

编译上述代码，得到图形如图7.1.7所示。
<p align="center"> 
<img align="middle" src="latex/chapter-7/graphics/example_sec7_1_7.png" width="300" />
</p>

<center><b>图7.1.7</b> 编译后的图形效果</center>

【**例7-8**】横纵缩放。
```tex
\documentclass[12pt]{article}
\usepackage{tikz}
\begin{document}

\begin{tikzpicture}[xscale=1.5, yscale = 2]

    \draw (-2,0) -- (2,0) -- (2,2) -- (-2,2) -- (-2,0);
    \draw (0,4) -- (0,-2);
    \draw (3,-2) -- (3,4) -- (7,4) -- (7,-2) -- (3,-2);
    \draw (4,3) -- (6,3); \draw (4,1) -- (6,1); \draw (4,-1) -- (6,-1);
    \draw (5,3) -- (5,-1); \draw (5.75,0.25) -- (6.25,-0.25);

\end{tikzpicture}

\end{document}
```

编译上述代码，得到图形如图7.1.8所示。
<p align="center"> 
<img align="middle" src="latex/chapter-7/graphics/example_sec7_1_8.png" width="300" />
</p>

<center><b>图7.1.8</b> 编译后的图形效果</center>

# 7.1.4 绘制箭头

在绘制直线的基础上，我们往往需要通过绘制箭头来指向性地表达意图。箭头的绘制只需要在直线绘制的基础上，增加`[option]`进行声明即可。

【**例7-9**】绘制箭头。
```tex
\documentclass[12pt]{article}
\usepackage{tikz}
\begin{document}

\begin{tikzpicture}

    \draw [->] (0,0) -- (2,0);
    \draw [<-] (0, -0.5) -- (2,-0.5);
    \draw [|->] (0,-1) -- (2,-1);

\end{tikzpicture}

\end{document}
```

编译上述代码，得到图形如图7.1.9所示。
<p align="center"> 
<img align="middle" src="latex/chapter-7/graphics/example_sec7_1_9.png" width="200" />
</p>

<center><b>图7.1.9</b> 编译后的图形效果</center>

【**例7-10**】利用绘制箭头的例子以及多条线段连续绘制的例子，用一行命令绘制一个直角坐标系。
```tex
\documentclass[12pt]{article}
\usepackage{tikz}
\begin{document}

\begin{tikzpicture}

    \draw [<->] (0,2) -- (0,0) -- (3,0);

\end{tikzpicture}

\end{document}
```

编译上述代码，得到图形如图7.1.10所示。
<p align="center"> 
<img align="middle" src="latex/chapter-7/graphics/example_sec7_1_10.png" width="200" />
</p>

<center><b>图7.1.10</b> 编译后的图形效果</center>


### 7.1.5 调整线条粗细

采用`\draw`命令时，增加的`[option]`声明也可以用来调整线条的粗细。

【**例7-11**】绘制不同粗细的线条。
```tex
\documentclass[12pt]{article}
\usepackage{tikz}
\begin{document}

\begin{tikzpicture}

    \draw [ultra thick] (0,1) -- (2,1);
    \draw [thick] (0,0.5) -- (2,0.5);
    \draw [thin] (0,0) -- (2,0);

\end{tikzpicture}

\end{document}
```

编译上述代码，得到图形如图7.1.11所示。
<p align="center"> 
<img align="middle" src="latex/chapter-7/graphics/example_sec7_1_11.png" width="200" />
</p>

<center><b>图7.1.11</b> 编译后的图形效果</center>

其中，线条的粗细可以通过不同的指令来控制，从细到粗分别可调用：`ultra thin`，`very thin`，`thin`，`semithick`，`thick`，`very thick`，`ultra thick`。其效果分别如下例所示。

【**例7-12**】绘制上述七种不同粗细的线条。
```tex
\documentclass[12pt]{article}
\usepackage{tikz}
\begin{document}

\begin{tikzpicture}

    \draw [ultra thin] (0,0) -- (2,0);
    \draw [very thin] (0,0.5) -- (2,0.5);
    \draw [thin] (0,1) -- (2,1);
    \draw [semithick] (0,1.5) -- (2,1.5);
    \draw [thick] (0,2) -- (2,2);
    \draw [very thick] (0,2.5) -- (2,2.5);
    \draw [ultra thick] (0,3) -- (2,3);

\end{tikzpicture}

\end{document}
```

编译上述代码，得到图形如图7.1.12所示。
<p align="center"> 
<img align="middle" src="latex/chapter-7/graphics/example_sec7_1_12.png" width="200" />
</p>

<center><b>图7.1.12</b> 编译后的图形效果</center>

除此之外，我们也可以自行定义线条的粗细，如`[line width=5]`、`[line width=0.2cm]`。值得注意的是，当我们直接声明数值而不声明单位时，其默认单位均为`pt`。

【**例7-13**】绘制自定义粗细的线条。
```tex
\documentclass[12pt]{article}
\usepackage{tikz}
\begin{document}

\begin{tikzpicture}

    \draw [line width=3] (0,0) -- (2,0);
    \draw [line width=0.2cm] (0,0.5) -- (2,0.5);

\end{tikzpicture}

\end{document}
```

编译上述代码，得到图形如图7.1.13所示。
<p align="center"> 
<img align="middle" src="latex/chapter-7/graphics/example_sec7_1_13.png" width="200" />
</p>

<center><b>图7.1.13</b> 编译后的图形效果</center>


### 7.1.6 虚线

我们也可以在`[option]`声明中增加对于线条形状的定义。如虚线`dashed`和点线`dotted`。

【**例7-14**】绘制虚线。
```tex
\documentclass[12pt]{article}
\usepackage{tikz}
\begin{document}

\begin{tikzpicture}

    \draw [dashed, ultra thick] (0,1) -- (2,1); %我们可以通过组合多种option来声明线条的多种特征。
    \draw [dashed] (0, 0.5) -- (2,0.5);
    \draw [dotted] (0,0) -- (2,0);
    
\end{tikzpicture}

\end{document}
```

编译上述代码，得到图形如图7.1.14所示。
<p align="center"> 
<img align="middle" src="latex/chapter-7/graphics/example_sec7_1_14.png" width="200" />
</p>

<center><b>图7.1.14</b> 编译后的图形效果</center>


### 7.1.7 颜色

我们也可以在`[option]`声明中增加对于线条颜色的定义。如红色`red`、 绿色`green`、蓝色`blue`等等。

【**例7-15**】绘制不同颜色的直线。
```tex
\documentclass[12pt]{article}
\usepackage{tikz}
\begin{document}

\begin{tikzpicture}

    \draw [red] (0,1) -- (2,1);
    \draw [green] (0, 0.5) -- (2,0.5);
    \draw [blue] (0,0) -- (2,0);
    
\end{tikzpicture}

\end{document}
```

编译上述代码，得到图形如图7.1.15所示。
<p align="center"> 
<img align="middle" src="latex/chapter-7/graphics/example_sec7_1_15.png" width="200" />
</p>

<center><b>图7.1.15</b> 编译后的图形效果</center>


【回放】[**导言**](https://nbviewer.jupyter.org/github/xinychen/latex-cookbook/blob/main/chapter-7/section0.ipynb)

【继续】[**7.2 节点介绍**](https://nbviewer.jupyter.org/github/xinychen/latex-cookbook/blob/main/chapter-7/section2.ipynb)

### License

<div class="alert alert-block alert-danger">
<b>This work is released under the MIT license.</b>
</div>
