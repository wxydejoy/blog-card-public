## 2.4 全局格式设置

在前导代码中对文档进行全局格式设置至关重要，它会决定编译文档的排版样式与编译效果。这里将以article类型文档为例，介绍如何调用宏包对纸张方向、页边距等进行调整。

#### 纸张方向

article类型文档的纸张方向默认为portrait（纵向），也可以设置成landscape（横向）。在文档中可以调用`lscape`宏包中的`\begin{landscape} \end{landscape}`环境将默认的纵向文档调整为横向。

【**例1**】创建一个两页的简单文档，将第一页的纸张方向设置为纵向，并使用`lscape`宏包中的`\begin{landscape} \end{landscape}`环境将第二页设置为横向。

```tex
\documentclass[12pt, b5paper]{article}
\usepackage{lscape}

\begin{document}

Hello, LaTeXers! This is our first LaTeX document.

\begin{landscape}

Hello, LaTeXers! This is our first LaTeX document.

\end{landscape}

\end{document}
```

编译上述代码，得到文档如图2-4-1所示。

<p align="center">
<table>
<tr>
<td><img align="middle" src="docs/latex/chapter-2/graphics/example2_4_1_1.png" width="300"></td>
<td><img align="middle" src="docs/latex/chapter-2/graphics/example2_4_1_2.png" width="300"></td>
</tr>
</table>
</p>

<center><b>图2-4-1</b> 编译后的文档</center>


> 参考[How to change certain pages into landscape/portrait mode](https://tex.stackexchange.com/q/337/227605)。

#### 页边距

article类型文档的页边距可以通过调用`geometry`宏包进行调整。

【**例2**】创建一个简单文档，并调整页边距为25mm。

```tex
\documentclass[11pt]{article}
\usepackage[margin = 25mm]{geometry}

\begin{document}

Hello, LaTeXers! This is our first LaTeX document.

\end{document}
```
编译上述代码，得到文档如图2-4-2所示。

<p align="center">
<img align="middle" src="docs/latex/chapter-2/graphics/example2_4_21.png" width="300" />
</p>

<center><b>图2-4-2</b> 编译后的文档</center>


#### 章节标题的字体格式

article类型文档的章节标题的字体格式可以通过调用`sectsty`宏包进行调整。

【**例3**】使用`sectsty`宏包调整文档标题字体格式

```tex
\documentclass{article}
\usepackage{sectsty}
\sectionfont{\fontfamily{phv}\fontseries{b}\fontsize{11pt}{20pt}\selectfont} %一级标题字体格式设置
\subsectionfont{\fontfamily{phv}\fontseries{b}\fontsize{11pt}{20pt}\selectfont} %二级标题字体格式设置
\subsubsectionfont{\fontfamily{phv}\fontseries{b}\fontsize{11pt}{20pt}\selectfont} %三级标题字体格式设置
\title{LaTeX cook-book}

\begin{document}

\maketitle
\section{Introduction}
\subsection{Introduction1}
\subsubsection{Introduction2}
Hello, LaTeXers! This is our first LaTeX document.

\end{document}
```

编译上述代码，得到文档如图2-4-3所示。

<p align="center">
<img align="middle" src="docs/latex/chapter-2/graphics/example2_4_31.png" width="300" />
</p>

<center><b>图2-4-3</b> 编译后的文档</center>

#### 图、表、公式格式全局设置

当我们需要批量设置图、表及公式的格式时，可以通过调用`caption`宏包进行全局设置。

> 其他全局设置可参考[Changing/Defining Fonts for an Entire Document](https://latex.org/forum/viewtopic.php?f=44&t=3994)。

#### 自定义命令全局设置

有时，我们需要也可以使用一些自定义命令来更改全局设置。例如在更改整个文档的字体格式时，我们也可以使用`\renewcommand{\sfdefault}{\fontencoding{T1}\fontfamily{phv}\selectfont}、\renewcommand{\familydefault}{\sfdefault}`等命令；在更改目录标题时,我们可以使用`\renewcommand{\contentsname}{new name of Contents}`。




【回放】[**2.3 文档类型**](https://nbviewer.jupyter.org/github/xinychen/latex-cookbook/blob/main/chapter-2/section3.ipynb)

【继续】[**2.5 制作简单文档**](https://nbviewer.jupyter.org/github/xinychen/latex-cookbook/blob/main/chapter-2/section5.ipynb)

### License

<div class="alert alert-block alert-danger">
<b>This work is released under the MIT license.</b>
</div>
