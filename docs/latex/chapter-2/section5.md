## 2.5 简单文档的制作

LaTeX不但适合制作篇幅较大的文档，在制作篇幅较小的文档比如手稿、作业等时也十分方便。在LaTeX的各类文档中，最为常用的文档类型为article (文章)，以下将介绍如何制作一个简单文档。


### 2.5.1 添加标题、日期、作者信息

添加标题、日期、作者信息一般是在`\begin{document}`之前，格式如下：

```tex
% 输入空格表示空的
\title{标题}
\author{作者名字}
\date{日期}
```
如果要显示添加的相关信息，需要在`\begin{document}`之后使用`\maketitle `命令。

【**例1**】以文档类型article为例，在创建的简单文档中添加添加标题、日期、作者等信息。
```tex
\documentclass[a4paper, 12pt]{article}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{palatino} 
\title{LaTeX cook-book}% 标题
\author{Author}% 作者
\date{2021/12/31}% 日期

\begin{document}
\maketitle % 显示命令
Hello, LaTeXers! This is our first LaTeX document.

\end{document}
```

编译上述代码，得到文档如图2-5-1所示。

<p align="center">
<img align="middle" src="latex/chapter-2/graphics/example2_4_1.png" width="450" />
</p>

<center><b>图2-5-1</b> 编译后的文档</center>



### 2.5.2 开始创建文档

在LaTeX中，以`\begin{document}`命令为分界线，该命令之前的代码都统称为前导代码，这些代码能设置全局参数。位于`\begin{document}`和`\end{document}`之间的代码被视为主体代码，我们所创作文档的具体内容也都是放在这两个命令之间。

####  设置章节

文档的章节是文档逻辑关系的重要体现，无论是中文论文还是英文论文都会有严谨的格式，章、节、段分明。在LaTeX中，不同的文档类设置章节的命令有些许差别，`\chapter`命令只在book、report两个文档类中有定义，article类型中设置章节可以通过`\section{name}`及`\subsection{name}`等简单的命令进行实现。

【**例2**】在例1的基础上使用`\section{name}`及`\subsection{name}`创建二级标题。
```tex
\documentclass[a4paper, 12pt]{article}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{palatino} 
\title{LaTeX cook-book}
\author{Author}
\date{2021/12/31}

\begin{document}
\maketitle 
\section{Introduction}% 一级标题
\subsection{Hellow LaTeXers}% 二级标题

Hello, LaTeXers! This is our first LaTeX document.

\end{document}
```

编译上述代码，得到文档如图2-5-2所示。

<p align="center">
<img align="middle" src="latex/chapter-2/graphics/example2_4_2.png" width="450" />
</p>

<center><b>图2-5-2</b> 编译后的文档</center>

####  新增段落

段落是文章的基础，在LaTeX中，可以直接
在文档中间键入文本作为段落，也可以使用`\paragraph{name}`和 `\subparagraph{name}`插入带标题的段落和亚段落。

【**例3**】在例2的基础上，使用`\paragraph{name}`和 `\subparagraph{name}`插入带标题的段落。
```tex
\documentclass[a4paper, 12pt]{article}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{palatino} 
\title{LaTeX cook-book}
\author{Xinyu Chen}
\date{2021/07/06}

\begin{document}
\maketitle 
\section{Introduction}% 一级标题
\subsection{Hellow LaTeXers}% 二级标题
\paragraph{PA}
Hello, LaTeXers! This is our first LaTeX document.
\subparagraph{Pa1}
This document is our starting point for learning LaTeX and writing with it. It would not be difficult.
\end{document}
```

编译上述代码，得到文档如图2-5-3所示。

<p align="center">
<img align="middle" src="latex/chapter-2/graphics/example2_4_3.png" width="450" />
</p>

<center><b>图2-5-3</b> 编译后的文档</center>


####  生成目录

在LaTeX中，我们通过一行简单的命令便可以生成文档的目录，即`\tableofcontents`。命令放在哪里，就会在哪里自动创建一个目录。默认情况下，该命令会根据用户定义的篇章节标题生成文档目录。目录中包含`\subsubsection`及其更高层次的结构标题，而段落和子段信息则不会出现在文档目录中。注意，如果有带`*`号的章节命令，则该章节标题也不会出现在目录中。如果想让文档正文内容与目录不在同一页，可在`\tableofcontents`命令后使用`\newpage`命令或者`clearpage`命令。

【**例4**】使用`\tableofcontents`为一个简单文档创建目录。

```tex
\documentclass[12pt]{article}

\begin{document}

\tableofcontents

\section{LaTeX1}
\subsection{1.1}
The text of 1.1
\subsection{1.2}
The text of 1.2
\subsection{1.3}
The text of 1.3

\section{LaTeX2}
\subsection{2.1}
The text of 2.1
\subsection{2.2}
The text of 2.2
\subsection{2.3}
The text of 2.3

\section*{LaTeX3}

\end{document}
```

编译上述代码，得到文档如图2-5-4所示。

<p align="center">
<table>
<tr>
<td><img align="middle" src="latex/chapter-2/graphics/example2_4_4_1.png" width="300"></td>
<td><img align="middle" src="latex/chapter-2/graphics/example2_4_4_2.png" width="300"></td>
</tr>
</table>
</p>

<center><b>图2-5-4</b> 编译后的文档</center>

类似对章节编号深度的设置，我们通过调用计数器命令\mintinline{tex}{\setcounter}也可以指定目录层次深度。例如：

- `\setcounter{tocdepth}{0}` %目录层次仅包括\part
- `\setcounter{tocdepth}{1}` % 目录层次深入到\section
- `\setcounter{tocdepth}{2}` % 目录层次深入到\subsection
- `\setcounter{tocdepth}{3}` % 目录层次深入到\subsubsection，默认值

除此之外，我们还可以在章节前面添加`\addtocontents{toc}{\setcounter{tocdepth}{}}`命令对每个章节设置不同深度的目录。另外还有一些其他的目录格式调整命令，如果我们想让创建的目录在文档中独占一页，只需要在目录生成命令前后添加`\newpage`；如果我们需要让目录页面不带有全文格式，只需要在生成目录命令后面加上`\thispagestyle{empty}`命令；如果我们想设置目录页之后设置页码为1，则需要在生成目录命令后面加上`\setcounter{page}{1}`命令。

如果我们想要创建图目录或表目录，分别使用`\listoffigures`、`\listoftables`命令即可，与创建章节目录的过程类似，这两个命令会根据文档中图表的标题产生图表目录，但不同之处在于，图目录或表目录中所有标题均属于同一层次。


### 练习题

> 打开LaTeX在线系统[https://www.overleaf.com](https://www.overleaf.com/project)或本地安装好的LaTeX编辑器，创建名为LaTeX_practice的项目，并同时新建一个以`.tex`为拓展名的源文件，完成以下几道练习题。


[1] 使用`mathpazo`工具包中提供的默认字体创建一个简单文档。

> `mathpazo`工具包提供的字体是在Palatino字体基础上定义出来的。

```tex
\documentclass[a4paper, 12pt]{article}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
% 请在此处申明使用mathpazo工具包

\begin{document}

Hello, LaTeXers! This is our first LaTeX document.

\end{document}
```

【回放】[**2.4 一些基本命令**](https://nbviewer.jupyter.org/github/xinychen/latex-cookbook/blob/main/chapter-2/section4.ipynb)

【继续】[**2.6 制作中文文档**](https://nbviewer.jupyter.org/github/xinychen/latex-cookbook/blob/main/chapter-2/section6.ipynb)

### License

<div class="alert alert-block alert-danger">
<b>This work is released under the MIT license.</b>
</div>
