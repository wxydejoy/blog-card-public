## 3.2 创建章节

在制作文档时，不管是学术论文还是书籍，都需要创建章节来优化文章的层次结构。LaTeX提供了不同层次章节的创建命令，从高到低包括：使用`\part{}`命令创建不同篇、使用`\chapter{}`命令创建不同章、使用`\section{}`命令创建一级节、使用`\subsection{}`命令创建二级节、以及使用`\subsubsection{}`命令创建三级节。各篇章节的标题填写在`{}`中。

对于article类型文档，可以调用上述除了`\chapter{}`命令之外的其他章节命令。而在book、report类型文档中，则可以调用上述所有章节命令。

【**例1**】使用`\section{}`及`\subsection{}`命令创建两级章节。

```tex
\documentclass[12pt]{article}
\begin{document}

\section{Text Editing}
\subsection{Text}
\subsection{List}
\subsection{Section}

\end{document}
```
编译后效果如图3-2-1所示。

<p align="center">
<img align="middle" src="docs/latex/chapter-3/graphics/example3_2_1.png" width="300" />
</p>

<center><b>图3-2-1</b> 编译后效果</center>

在撰写学术论文时，不同出版商所要求的章节标题格式可能是不一样的。因此，我们需要根据不同出版商的需要来调整章节标题的格式。常见的格式调整包括取消自动编号以及改变标题字体样式等

- 自动编号与取消自动编号

    在LaTeX中使用上述命令创建章节时，默认会对各章节进行自动编号。如果用户想要对某章节取消自动编号，只需要在章节命令后加上星号即可，如`\section*{}`命令。

- 设置章节自动编号深度

    用户也可以通过在导言区使用`\setcounter{secnumdepth}{}`计数器命令设置章节自动编号深度，从而达到批量取消自动编号的效果。在{}中填写编号深度值，编号深度值从0开始设置，表示章节自动编号深入层次：

    - `\setcounter{secnumdepth}{0}`表示自动编号章节层次仅包括`\part`和`chapter`；
    
    - `\setcounter{secnumdepth}{1}`表示自动编号层次深入到`\section`级；
    
    - `\setcounter{secnumdepth}{2}`表示自动编号层次深入到`\subsection`级；
    
    - `\setcounter{secnumdepth}{3}`表示自动编号层次深入到`\subsubsection`级，默认值。

【**例2**】使用`\setcounter{secnumdepth}{}`命令设置自动编号层次到`\section`级。

```tex
\documentclass[12pt]{article}
\setcounter{secnumdepth}{1}

\begin{document}

\section{First Section}
\subsection{Subsection title1}
\subsection{Subsection title2}
\subsection{Subsection title3}
\section{Second Section}
\subsection{Subsection title4}
\subsection{Subsection title5}
\subsection{Subsection title6}
\section{Third section}
\subsection{Subsection title7}
\subsection{Subsection title8}
\subsection{Subsection title9}

\end{document}
```
编译后效果如图3-2-2所示。

<p align="center">
<img align="middle" src="docs/latex/chapter-3/graphics/example3_2_2.png" width="300" />
</p>

<center><b>图3-2-2</b> 编译后效果</center>

- 改变字体样式

    对于改变字体样式，我们需要使用`titlesec`宏包，使用该宏包中的命令`\titleformat*{}{}`来改变字体样式。

【**例3**】使用`\section*{}`删除章节标题，并使用`titlesec`宏包改变章节标题字体样式。

```tex
\documentclass[12pt]{article}
\usepackage{titlesec}
\titleformat*{\subsection}{\Large\sectionef}

\begin{document}

\section*{Text Editing}
\subsection{Text}
\subsection{List}
\subsection{Section}

\end{document}
```
编译后效果如图3-2-3所示。

<p align="center">
<img align="middle" src="docs/latex/chapter-3/graphics/example3_2_3.png" width="300" />
</p>

<center><b>图3-2-3</b> 编译后效果</center>


当然，有时我们也会遇到一些出版商要求我们将标题居中显示，在LaTeX的`article`文档类型中，我们可以调用`sectsty`宏包，并用到`\sectionfont{\centering}`使标题居中。

【**例4**】调用`sectsty`宏包，并使用`\sectionfont{\centering}`命令将标题居中。

```tex
\documentclass[12pt]{article}
\usepackage{sectsty}
\sectionfont{\centering}

\begin{document}

\section{Text Editing}
\subsection{Text}
\subsection{List}
\subsection{Section}

\end{document}
```
编译后效果如图3-2-4所示。

<p align="center">
<img align="middle" src="docs/latex/chapter-3/graphics/example3_2_4.png" width="500" />
</p>

<center><b>图3-2-4</b> 编译后效果</center>

【回放】[**3.1 创建标题部分、摘要及关键词**](https://nbviewer.jupyter.org/github/xinychen/latex-cookbook/blob/main/chapter-3/section1.ipynb)

【继续】[**3.3 生成目录**](https://nbviewer.jupyter.org/github/xinychen/latex-cookbook/blob/main/chapter-3/section3.ipynb)

### License

<div class="alert alert-block alert-danger">
<b>This work is released under the MIT license.</b>
</div>
