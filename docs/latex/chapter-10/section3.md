## 10.3 海报制作

参加过各类学术会议或研讨会的读者可能会知道：在各类学术交流中，除了制作幻灯片用于汇报，还有一种非常重要的展现成果方式就是海报 (poster)。制作海报的方式有很多种，这里将介绍如何使用LaTeX制作海报。

在2010年的时候，LaTeX技术问答社区TeX StackExchange中有一个非常有趣的问题 (网址为[https://tex.stackexchange.com/questions/341](https://tex.stackexchange.com/questions/341))，问题的内容是“如何使用LaTeX制作在学术会议中展示研究成果的海报？有没有一些现成的文档类型可供使用？”，关于这个问题的讨论和回答非常精彩，问题的回答里面提到了各种工具，其中，最引人注意的是`tikzposter`和`beamerposter`这两种工具。时至今日，`tikzposter`和`beamerposter`这两种工具已经成为制作海报最为常用的文档类型。从名字上看，它们分别与用于绘制图形的tikz宏包和用于制作幻灯片的beamer文档类型密不可分，在这两种工具中，我们可以使用到一些简单好用的命令和样式。

### 10.3.1 `tikzposter`工具

`tikzposter`是一个文档类，用于生成 PDF 格式的科学海报。与其他文档类类似，`tikzposter`也包含前导代码和主体代码两个部分，前导代码主要用于海报基本信息的设定及宏包的调用，主题代码用来设计海报内容。

【**例1**】创建一个`tikzposter`类的简单文档，并在前导代码中填写一些基本信息。

```tex
\documentclass[25pt, a0paper, portrait]{tikzposter}

\title{TikzPoster Example}
\author{author}
\date{\today}
\institute{LaTeX Cookbook Institute}
\usetheme{Board}

\begin{document}

\maketitle

\end{document}

```

编译效果如图10.3.1所示。

<p align="center">
<img align="middle" src="latex/chapter-10/graphics/example10_3_1.png" width="750" />
</p>

<center><b>图10.3.1</b> 编译后效果</center>

与其他文档类型类似，例1中第一个命令`\documentclass[...]{tikzposter}` 声明这个文档是一个`tikzposter`，大括号内的附加参数分别设置字体大小、纸张大小和方向；`title` , `author`, `date` 及 `institute`用来填写海报题目、作者、日期及单位等信息； ` \usetheme{Board}`设置海报主题。

【**例2**】在例1代码中加入主体代码，制作一个简单简历。

```tex

\documentclass[25pt, a0paper, portrait]{tikzposter}
\title{TikzPoster Example}
\author{author}
\date{\today}
\institute{LaTeX Cookbook Institute}

\usepackage{blindtext}
\usepackage{comment}

\usetheme{Board}

\begin{document}

\maketitle

\block{~}
{
    \blindtext
}

\begin{columns}
    \column{0.4}
    \block{More text}{Text and more text}
    
    \column{0.6}
    \block{Something else}{Here, \blindtext \vspace{4cm}}
    \note[
        targetoffsetx=-9cm, 
        targetoffsety=-6.5cm, 
        width=0.5\linewidth
        ]
        {e-mail \texttt{welcome@overleaf.com}}
\end{columns}

\begin{columns}
    \column{0.5}
    \block{A figure}
    {
        \begin{tikzfigure}
            \includegraphics[width=0.4\textwidth]{images/R-C.jpg}
        \end{tikzfigure}
    }
    \column{0.5}
    \block{Description of the figure}{\blindtext}
\end{columns}

\end{document}

```

编译效果如图10.3.2所示。

<p align="center">
<img align="middle" src="latex/chapter-10/graphics/example10_3_2.png" width="750" />
</p>

<center><b>图10.3.2</b> 编译后效果</center>

### 10.3.2 `beamerposter`工具

`beamerposter`是建立在`beamer`类上的宏包，可以用于生成和设计科学海报。`beamerposter`同样包含前导代码和主题代码两个部分，前导代码主要用于海报基本信息的设定及宏包的调用基本与`beamer`类相同，主题代码用来设计海报内容。

【**例3**】创建一个调用`beamerposter`宏包的`beamer`类简单文档，并在前导代码中填写一些基本信息。

```tex
\documentclass{beamer}
\usepackage{times}
\usepackage{amsmath,amsthm, amssymb}
\boldmath
\usetheme{RedLion}
\usepackage[orientation=portrait,size=a0,scale=1.4]{beamerposter}

\title[Beamer Poster]{Beamer Poster example}
\author[welcome@overleaf.com]{author}
\institute[Overleaf University]{LaTeX Cookbook Institute}
\date{\today}
  
\logo{\includegraphics[height=7.5cm]{overleaf-logo}}


\begin{document}

This is a Beamer poster example 
    
\end{document}
```
编译效果如图10.3.3所示。

<p align="center">
<img align="middle" src="latex/chapter-10/graphics/example10_3_3.png" width="750" />
</p>

<center><b>图10.3.3</b> 编译后效果</center>

【**例4**】在例3代码中加入主体代码，制作一个简单简历。

```tex

\documentclass{beamer}
\usepackage{times}
\usepackage{amsmath,amsthm, amssymb}
\boldmath
\usetheme{RedLion}
\usepackage[orientation=portrait,size=a0,scale=1.4]{beamerposter}

\title[Beamer Poster]{Beamer Poster example}
\author[welcome@overleaf.com]{author}
\institute[Overleaf University]{LaTeX Cookbook Institute}
\date{\today}
  
\logo{\includegraphics[height=7.5cm]{overleaf-logo}}


\begin{document}
\begin{frame}{} 
    \vfill
    \begin{block}{\large Fontsizes}
      \centering
      {\tiny tiny}\par
      {\scriptsize scriptsize}\par
      {\footnotesize footnotesize}\par
      {\normalsize normalsize}\par
      {\large large}\par
      {\Large Large}\par
      {\LARGE LARGE}\par
      {\veryHuge VeryHuge}\par
      {\VeryHuge VeryHuge}\par
      {\VERYHuge VERYHuge}\par
    \end{block}
    \vfill
    \vfill
    \begin{block}{\large Fontsizes}
      \centering
      {\tiny tiny}\par
      {\scriptsize scriptsize}\par
      {\footnotesize footnotesize}\par
      {\normalsize normalsize}\par
      {\large large}\par
      {\Large Large}\par
      {\LARGE LARGE}\par
      {\veryHuge VeryHuge}\par
      {\VeryHuge VeryHuge}\par
      {\VERYHuge VERYHuge}\par
    \end{block}
    \vfill
    \begin{columns}[t]
      \begin{column}{.30\linewidth}
        \begin{block}{Introduction}
          \begin{itemize}
          \item some items
          \item some items
          \item some items
          \item some items
          \end{itemize}
        \end{block}
      \end{column}
      \begin{column}{.48\linewidth}
        \begin{block}{Introduction}
          \begin{itemize}
          \item some items and $\alpha=\gamma, \sum_{i}$
          \item some items
          \item some items
          \item some items
          \end{itemize}
          $$\alpha=\gamma, \sum_{i}$$
        \end{block}

        \begin{block}{Introduction}
          \begin{itemize}
          \item some items
          \item some items
          \item some items
          \item some items
          \end{itemize}
        \end{block}

        \begin{block}{Introduction}
          \begin{itemize}
          \item some items and $\alpha=\gamma, \sum_{i}$
          \item some items
          \item some items
          \item some items
          \end{itemize}
          $$\alpha=\gamma, \sum_{i}$$
        \end{block}
      \end{column}
    \end{columns}
  \end{frame}
    
\end{document}

```

<p align="center">
<img align="middle" src="latex/chapter-10/graphics/example10_3_4.png" width="750" />
</p>

<center><b>图10.3.4</b> 编译后效果</center>

### 参考资料

- [How to create posters using LaTeX](https://tex.stackexchange.com/questions/341)

【回放】[**10.2 算法伪代码**](https://nbviewer.jupyter.org/github/xinychen/latex-cookbook/blob/main/chapter-10/section2.ipynb)

【继续】[**10.4 简历制作**](https://nbviewer.jupyter.org/github/xinychen/latex-cookbook/blob/main/chapter-10/section4.ipynb)

### License

<div class="alert alert-block alert-danger">
<b>This work is released under the MIT license.</b>
</div>
