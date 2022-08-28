## 7.2 节点介绍

节点是`TikZ`中的一个常用功能。在绘制节点时，通常需要声明其位置和形状，部分节点可以在其中添加文字，同时也可以为节点赋予一个名称，用于后续参考。在本节中，我们将详细介绍节点的相关功能及其应用。


### 7.2.1 节点基本介绍

【**例7-16**】绘制节点，方法一。
```tex
\documentclass[12pt]{article}
\usepackage{tikz}
\begin{document}

\begin{tikzpicture}

    \path (0,2) node [shape=circle,draw=blue!50,fill=blue!20,thick] {}
          (0,1) node [shape=circle,draw=blue!50,fill=blue!20,thick] {$C$}
          (0,0) node [shape=circle,draw=blue!50,fill=blue!20,thick] {}
          (1,1) node [shape=rectangle,draw=black!50,fill=black!20] {}
          (-1,1) node [shape=rectangle,draw=black!50,fill=black!20] {};
    
\end{tikzpicture}

\end{document}
```

等价于

【**例7-17**】绘制节点，方法二。
```tex
\documentclass[12pt]{article}
\usepackage{tikz}
\begin{document}

\begin{tikzpicture}

    \node [shape=circle,draw=blue!50,fill=blue!20,thick] at (0,2)  {};
    \node [shape=circle,draw=blue!50,fill=blue!20,thick] at (0,1) {$C$};
    \node [shape=circle,draw=blue!50,fill=blue!20,thick] at (0,0)  {};
    \node [shape=rectangle,draw=black!50,fill=black!20] at (1,1) {};
    \node [shape=rectangle,draw=black!50,fill=black!20] at (-1,1) {};
    
\end{tikzpicture}

\end{document}
```

编译上述代码，得到图形如图7.2.1所示。
<p align="center"> 
<img align="middle" src="latex/chapter-7/graphics/example_sec7_2_1.png" width="200" />
</p>

<center><b>图7.2.1</b> 编译后的图形效果</center>

这里需要注意的是，在`[shape=circle,draw=blue!50,fill=blue!20]`中，`shape`指令声明节点形状，`draw`指令声明是否显现该形状的边框，并用`draw=`来声明边框颜色，`fill`命令指明该节点是否要填充，并用`fill=`来声明填充颜色。若要在节点中显示文字，需在后面`{}`中填写对应的文字即可。


### 7.2.2 节点样式

当某一种形状及颜色的节点需要在不同位置多次出现时，上述代码显得不够优美。我们可以通过一段代码提前声明该节点的样式，并反复调用这段代码即可。

【**例7-18**】绘制节点，方法三。
```tex
\documentclass[12pt]{article}
\usepackage{tikz}
\begin{document}

\tikzstyle{aaa}=[circle,draw=blue!50,fill=blue!20,thick]
\tikzstyle{bbb}=[rectangle,draw=black!50,fill=black!20]
\begin{tikzpicture}

    \path (0,2) node [aaa] {}
          (0,1) node [aaa] {$C$}
          (0,0) node [aaa] {}
          (1,1) node [bbb] {}
          (-1,1) node [bbb] {};
    
\end{tikzpicture}

\end{document}
```
编译上述代码，得到图形与图7.2.1所示相同。



### 7.2.3 节点命名

为了将节点相互连接起来，我们需要指明连接哪两个节点。因此，每个节点需要我们声明一个名称。声明名称有两种方式，一种是采用`name=`的方式，另一种是在`\node`后用括号声明，如`\node (name) ...`。

【**例7-19**】绘制节点，并声明节点名称，方法一。
```tex
\documentclass[12pt]{article}
\usepackage{tikz}
\begin{document}

\tikzstyle{aaa}=[circle,draw=blue!50,fill=blue!20,thick]
\tikzstyle{bbb}=[rectangle,draw=black!50,fill=black!20]
\begin{tikzpicture}

    \path (0,2) node [aaa,name=a1] {}
          (0,1) node [aaa,name=a2] {$C$}
          (0,0) node [aaa,name=a3] {}
          (1,1) node [bbb,name=b1] {}
          (-1,1) node [bbb,name=b2] {};
          
\end{tikzpicture}

\end{document}
```

【**例7-20**】绘制节点，并声明节点名称，方法二。
```tex
\documentclass[12pt]{article}
\usepackage{tikz}
\begin{document}

\tikzstyle{aaa}=[circle,draw=blue!50,fill=blue!20,thick]
\tikzstyle{bbb}=[rectangle,draw=black!50,fill=black!20]
\begin{tikzpicture}

    \node (a1) [aaa] at (0,2)  {};
    \node (a2) [aaa] at (0,1) {$C$};
    \node (a3) [aaa] at (0,0)  {};
    \node (b1) [bbb] at (1,1) {};
    \node (b2) [bbb] at (-1,1) {};
    
\end{tikzpicture}

\end{document}
```


### 7.2.4 基于相对位置绘制节点
给每个节点命名后，我们便可以通过`above of`（上）、`below of`（下）、`left of`（左）、`right of`（右）等命令来声明新节点与某个节点的相对位置来绘制图形。

【**例7-21**】利用相对位置绘制节点。
```tex
\documentclass[12pt]{article}
\usepackage{tikz}
\begin{document}

\tikzstyle{aaa}=[circle,draw=blue!50,fill=blue!20,thick]
\tikzstyle{bbb}=[rectangle,draw=black!50,fill=black!20]
\begin{tikzpicture}

    \node (a1) [aaa]                {};
    \node (a2) [aaa]  [below of=a1] {$C$};
    \node (a3) [aaa]  [below of=a2] {};
    \node (b1) [bbb]  [right of=a2] {};
    \node (b2) [bbb]  [left  of=a2] {};
    
\end{tikzpicture}

\end{document}
```
编译上述代码，得到图形与图7.2.1所示相同。

### 7.2.5 连接节点

有了节点名称了，我们就可以对节点进行连接。我们拿连接A与B节点为例，在连接时，我们通常需要声明A节点的哪个位置与B节点的哪个位置连接。位置声明通常采用`east`（右）、`west`（左）、`north`（上）、`south`（下）、`center`（中心）等命令。

【**例7-22**】利用相对位置连接节点。
```tex
\documentclass[12pt]{article}
\usepackage{tikz}
\begin{document}

\tikzstyle{aaa}=[circle,draw=blue!50,fill=blue!20,thick]
\tikzstyle{bbb}=[rectangle,draw=black!50,fill=black!20]
\begin{tikzpicture}

    \node (a1) [aaa]                {$a_1$};
    \node (a2) [aaa]  [below of=a1] {$C$};
    \node (a3) [aaa]  [below of=a2] {$a_3$};
    \node (b1) [bbb]  [right of=a2] {$b_1$};
    \node (b2) [bbb]  [left  of=a2] {$b_2$};
    \draw [->] (a2.west) -- (b2.east);
    \draw [->] (a2.east) -- (b1.west);
    \draw [->] (a2.north) -- (a1.south);
    \draw [->] (a2.south) -- (a3.north);
    
\end{tikzpicture}

\end{document}
```
该代码等价于

【**例7-23**】利用相对位置连接节点，不声明节点的连接位置。
```tex
\documentclass[12pt]{article}
\usepackage{tikz}
\begin{document}

\tikzstyle{aaa}=[circle,draw=blue!50,fill=blue!20,thick]
\tikzstyle{bbb}=[rectangle,draw=black!50,fill=black!20]
\begin{tikzpicture}

    \node (a1) [aaa]                {$a_1$};
    \node (a2) [aaa]  [below of=a1] {$C$};
    \node (a3) [aaa]  [below of=a2] {$a_3$};
    \node (b1) [bbb]  [right of=a2] {$b_1$};
    \node (b2) [bbb]  [left  of=a2] {$b_2$};
    \draw [->] (a2) -- (b2);
    \draw [->] (a2) -- (b1);
    \draw [->] (a2) -- (a1);
    \draw [->] (a2) -- (a3);
    
\end{tikzpicture}

\end{document}
```

编译上述代码，得到图形如图7.2.2所示。
<p align="center"> 
<img align="middle" src="latex/chapter-7/graphics/example_sec7_2_2.png" width="200" />
</p>

<center><b>图7.2.2</b> 编译后的图形效果</center>

【**例7-24**】利用`edge`命令连接节点，方法一。
```tex
\documentclass[12pt]{article}
\usepackage{tikz}
\begin{document}

\tikzstyle{aaa}=[circle,draw=blue!50,fill=blue!20,thick]
\tikzstyle{bbb}=[rectangle,draw=black!50,fill=black!20]
\begin{tikzpicture}

    \node (a1) [aaa]                {$a_1$};
    \node (a2) [aaa]  [below of=a1] {$C$}   edge [->] (a1);
    \node (a3) [aaa]  [below of=a2] {$a_3$} edge [<-] (a2);
    \node (b1) [bbb]  [right of=a2] {$b_1$} edge [<-] (a2);
    \node (b2) [bbb]  [left  of=a2] {$b_2$} edge [<-] (a2);
    
\end{tikzpicture}

\end{document}
```

等价于

【**例7-25**】利用`edge`命令连接节点，方法二。
```tex
\documentclass[12pt]{article}
\usepackage{tikz}
\begin{document}

\tikzstyle{aaa}=[circle,draw=blue!50,fill=blue!20,thick]
\tikzstyle{bbb}=[rectangle,draw=black!50,fill=black!20]
\begin{tikzpicture}

    \path (0,2)  node [aaa,name=a1] {$a_1$}
          (0,1)  node [aaa,name=a2] {$C$}   edge [->] (a1)
          (0,0)  node [aaa,name=a3] {$a_3$} edge [<-] (a2)
          (1,1)  node [bbb,name=b1] {$b_1$} edge [<-] (a2)
          (-1,1) node [bbb,name=b2] {$b_2$} edge [<-] (a2);
    
\end{tikzpicture}

\end{document}
```

编译上述代码，得到图形与图7.2.2所示相同。

【**例7-26**】声明每个节点的连接位置，将周围节点边缘连接直中间节点的中心。
```tex
\documentclass[12pt]{article}
\usepackage{tikz}
\begin{document}

\tikzstyle{aaa}=[circle,draw=blue!50,fill=blue!20,thick]
\tikzstyle{bbb}=[rectangle,draw=black!50,fill=black!20]
\begin{tikzpicture}

    \node (a1) [aaa]                {$a_1$};
    \node (a2) [aaa]  [below of=a1] {};
    \node (a3) [aaa]  [below of=a2] {$a_3$};
    \node (b1) [bbb]  [right of=a2] {$b_1$};
    \node (b2) [bbb]  [left  of=a2] {$b_2$};
    \draw [->] (a2.center) -- (b2.east);
    \draw [->] (a2.center) -- (b1.west);
    \draw [->] (a2.center) -- (a1.south);
    \draw [->] (a2.center) -- (a3.north);
    
\end{tikzpicture}

\end{document}
```
编译上述代码，得到图形如图7.2.3所示。
<p align="center"> 
<img align="middle" src="latex/chapter-7/graphics/example_sec7_2_3.png" width="200" />
</p>

<center><b>图7.2.3</b> 编译后的图形效果</center>

【回放】[**7.1 基本介绍**](https://nbviewer.jupyter.org/github/xinychen/latex-cookbook/blob/main/chapter-7/section1.ipynb)

【继续】[**7.3 高级功能**](https://nbviewer.jupyter.org/github/xinychen/latex-cookbook/blob/main/chapter-7/section3.ipynb)

### License

<div class="alert alert-block alert-danger">
<b>This work is released under the MIT license.</b>
</div>
