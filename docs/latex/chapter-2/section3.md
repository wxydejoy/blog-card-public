## 2.3 文档类型的介绍

在LaTeX代码结构中，申明文档类型往往是制作文档的第一步，也是最基本的一步。事实上，虽然不同文档类型对应的文档样式略有不同，但制作不同类型的文档时，LaTeX中的绝大多数命令和环境却是通用的。完成对文档内容的创作后，使用文档类型的申明语句可以让我们在不同类型的文档间切换自如。

### 2.3.1 基本介绍

对LaTeX熟悉的读者会知道，LaTeX实际上支持非常多的文档类型，例如，撰写科技论文会用到的`article`（常规文档）类型、制作演示文稿会用到的`beamer`（幻灯片）类型。在众多文档类型中，常见的文档类型包括`article`（常规文档）、`report`（报告）、`book`（书籍）、`beamer`（幻灯片）等，如果使用支持中文编译的ctex文档类型，还会有`ctexart`（中文常规文档）、`ctexrep`（中文报告）、`ctexbook`（中文书籍）等，文档类型会直接决定整个文档的样式和风格。

使用LaTeX制作文档时，申明文档类型是作为前导代码，其一般格式为：

```tex
\documentclass[A]{B}
```

在这一申明语句中，位置A的作用主要是设置控制全文的文档参数，我们可以调整全文的字体大小、纸张大小、分栏设置等，因为各种文档类型都有一整套的默认参数，所以一般情况可以省略掉位置A。在位置B，我们需要键入特定的文档类型，例如，`\documentclass[a4paper, 12pt]{article}`即表示申明一个纸张大小为A4、字体大小为12pt的常规文档。

以下将逐一介绍比较常用的三种文档类型，包括`article`（常规文档）、`report`（报告）、`book`（书籍），其中，`report`和`book`这两种文档类型的文档结构是一致的，可以使用的结构命令有`\part{}`、`\chapter{}`、`\section{}`、`\subsection{}`、`\subsubsection{}`、`\paragraph{}`、`\subparagraph{}`，而`article`文档类型中除了没有`\chapter{}`这一结构命令之外，其他都与`report`和`book`文档类型是一样的。

### 2.3.2 `article`文档类型

`article`是LaTeX制作文档时最为常用的一种文档类型，撰写科技论文往往会用到`article`文档类型。

【**例1**】新建一个文档类型为`article`的简单文档。

```tex
\documentclass[a4paper, 12pt]{article} % 声明文档类型

\title{LaTeX Cookbook}

\begin{document}
\maketitle

\begin{abstract}
This is LaTeX cookbook!
\end{abstract}

\part{LaTeX Tutorial} % part名称

\section{Document Class} % 一级标题

\subsection{Article} % 二级标题

Hello, LaTeXers! This is our first LaTeX document.

\end{document}
```

编译上述代码，得到文档如图2-3-1所示。

<p align="center">
<img align="middle" src="docs/latex/chapter-2/graphics/example3_1.png" width="300" />
</p>

<center><b>图2-3-1</b> 编译后的文档</center>


### 2.3.3 `report`文档类型

`report`主要是面向撰写各类技术报告的文档类型。

【**例2**】新建一个文档类型为`report`的简单文档。

```tex
\documentclass[a4paper, 12pt]{report}

\begin{document}

\part{LaTeX Tutorial}

\chapter{Introduction}

\section{Document Class}

\subsection{Report}

Hello, LaTeXers! This is our first LaTeX document.

\end{document}
```

编译上述代码，得到文档如图2-3-2所示。

<p align="center">
<table>
<tr>
<td><img align="middle" src="docs/latex/chapter-2/graphics/example3_2_1.png" width="300"></td>
<td><img align="middle" src="docs/latex/chapter-2/graphics/example3_2_2.png" width="300"></td>
</tr>
</table>
</p>

<center><b>图2-3-2</b> 编译后的文档</center>

### 2.3.4 `book`文档类型

`book`是用于制作书籍等出版物的文档类型。

【**例3**】新建一个文档类型为book的简单文档。

```tex
\documentclass[a4paper, 12pt]{book}

\begin{document}

\part{LaTeX Tutorial}

\chapter{Introduction}

\section{Document Class}

\subsection{Report}

Hello, LaTeXers! This is our first LaTeX document.

\end{document}
```

编译上述代码，得到文档如图2-3-3所示。

<p align="center">
<table>
<tr>
<td><img align="middle" src="docs/latex/chapter-2/graphics/example3_3_1.png" width="300"></td>
<td><img align="middle" src="docs/latex/chapter-2/graphics/example3_3_2.png" width="300"></td>
<td><img align="middle" src="docs/latex/chapter-2/graphics/example3_3_3.png" width="300"></td>
</tr>
</table>
</p>

<center><b>图2-3-3</b> 编译后的文档</center>

【回放】[**2.2 LaTeX代码结构**](https://nbviewer.jupyter.org/github/xinychen/latex-cookbook/blob/main/chapter-2/section2.ipynb)

【继续】[**2.4 一些基本命令**](https://nbviewer.jupyter.org/github/xinychen/latex-cookbook/blob/main/chapter-2/section4.ipynb)

### License

<div class="alert alert-block alert-danger">
<b>This work is released under the MIT license.</b>
</div>
