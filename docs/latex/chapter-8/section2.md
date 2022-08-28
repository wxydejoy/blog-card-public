## 8.2 创建超链接

超链接指按内容链接，可以从一个文本内容指向文本其他内容或其他文件、网址等。超链接可以分为文本内链接、网页链接以及本地文件链接。LaTeX提供了`hyperref`宏包，可用于生成超链接。在使用时，只需在前导代码中申明宏包即可，即`\usepackage{hyperref}`。

### 8.2.1 超链接类型

#### 文本内链接

在篇幅较大的文档中，查阅内容会比较繁琐，因此，往往会在目录中使用超链接来进行文本内容的快速高效浏览。可以使用`hyperref`宏包创建文本内超链接。

【**例8-4**】使用`\usepackage{hyperref}`创建一个简单的目录链接文本内容的例子。

```tex
\documentclass{book}
\usepackage{blindtext}
\usepackage{hyperref} %超链接包

\begin{document}

\frontmatter
\tableofcontents
\clearpage

\addcontentsline{toc}{chapter}{Foreword}
{\huge {\bf Foreword}}

This is foreword.
\clearpage

\mainmatter

\chapter{First Chapter}

This is chapter 1.


\clearpage

\section{First section} \label{second}

This is section 1.1.
\end{document}
```

编译后文档如图8.2.1所示。

<p align="center">
<table>
<tr>
<td><img align="middle" src="latex/chapter-8/graphics/example8_2_1_1.png" width="300"></td>
<td><img align="middle" src="latex/chapter-8/graphics/example8_2_1_2.png" width="300"></td>
<td><img align="middle" src="latex/chapter-8/graphics/example8_2_1_3.png" width="300"></td>
<td><img align="middle" src="latex/chapter-8/graphics/example8_2_1_4.png" width="300"></td>
</tr>
</table>
</p>

<center><b>图8.2.4</b> 编译后的文档</center>

在导入 `hyperref` 时必须非常小心，一般而言，它必须是最后一个要导入的包。

#### 网址链接

众所周知，在文档中插入网址之类的文本同样需要用到超链接，同样的，使用`hyperref`宏包可以创建网页超链接。有时我们需要将超链接命名并隐藏网址，这时我们可以使用`href`命令进行插入；有时，我们插入的网址链接太长，但LaTeX不会自动换行，往往会造成格式混乱的问题，这时，我们可以使用`url`工具包，并在该工具包中声明一个参数即可解决这个问题，相关命令为`\usepackage[hyphens]{url}`。

> 参考[Line breaks in URLs](https://latex.org/forum/viewtopic.php?f=44&t=4022)。

【**例8-5**】在LaTeX中使用`hyperref`及`url`工具包插入网页链接并设置自动换行。

```tex
\documentclass[12pt]{article}
\usepackage[hyphens]{url}
\usepackage{hyperref}

\begin{document}

This is the website of open-source latex-cookbook repository: \href{https://github.com/xinychen/latex-cookbook}{LaTeX-cookbook} or go to the next url: \url{https://github.com/xinychen/latex-cookbook}.

\end{document}
```

编译后文档如图8.2.3所示。

<p align="center">
<table>
<tr>
<td><img align="middle" src="latex/chapter-8/graphics/example8_2_2.png" width="300"></td>

</tr>
</table>
</p>

<center><b>图8.2.2</b> 编译后的文档</center>

#### 本地文件链接

有时，需要将文本与本地文件进行链接，`href`命令也可用于打开本地文件。

【**例8-6**】在LaTeX中使用`href`命令打开本地文件。

```tex
\documentclass[12pt]{article}
\usepackage[hyphens]{url}
\usepackage{hyperref}

\begin{document}

This is the text of open-source latex-cookbook repository: \href{run:./LaTeX-cookbook.dox}{LaTeX-cookbook}.

\end{document}
```

编译后文档如图8.2.3所示。

<p align="center">
<table>
<tr>
<td><img align="middle" src="latex/chapter-8/graphics/example8_2_3.png" width="300"></td>

</tr>
</table>
</p>

<center><b>图8.2.3</b> 编译后的文档</center>

### 8.2.2 超链接格式

当然，有时候为了突出超链接，也可以在工具包`hyperref`中设置特定的颜色，设置的命令为`\hypersetup`，一般放在前导代码中，例如`colorlinks = true, linkcolor=blue, urlcolor = blue, filecolor=magenta`。默认设置以单色样式的空间字体打印链接，`\urlstyle{same}`命令将改变这个样式，并以与文本其余部分相同的样式显示链接。

> 参考[Website address](https://latex.org/forum/viewtopic.php?f=44&t=5115)。

【**例8-7**】在LaTeX中使用`hyperref`工具包插入超链接并设置超链接颜色为蓝色。

```tex
\documentclass{book}
\usepackage{blindtext}
\usepackage{hyperref} %超链接包
\hypersetup{colorlinks = true, %链接将被着色，默认颜色是红色
            linkcolor=blue, % 内部链接显示为蓝色
            urlcolor = cyan, % 网址链接为青色
            filecolor=magenta} % 本地文件链接为洋红色
\urlstyle{same}

\begin{document}

\frontmatter
\tableofcontents
\clearpage

\addcontentsline{toc}{chapter}{Foreword}
{\huge {\bf Foreword}}

This is foreword.
\clearpage

\mainmatter

\chapter{First Chapter}

This is chapter 1.
\clearpage

\section{First section} \label{second}

This is section 1.1.

This is the website of open-source latex-cookbook repository: \href{https://github.com/xinychen/latex-cookbook}{LaTeX-cookbook} or go to the next url: \url{https://github.com/xinychen/latex-cookbook}.

This is the text of open-source latex-cookbook repository: \href{run:./LaTeX-cookbook.dox}{LaTeX-cookbook} 

\end{document}
```

编译后文档如图8.2.4所示。

<p align="center">
<table>
<tr>
<td><img align="middle" src="latex/chapter-8/graphics/example8_2_4_1.png" width="300"></td>
<td><img align="middle" src="latex/chapter-8/graphics/example8_2_4_2.png" width="300"></td>
<td><img align="middle" src="latex/chapter-8/graphics/example8_2_4_3.png" width="300"></td>
<td><img align="middle" src="latex/chapter-8/graphics/example8_2_4_4.png" width="300"></td>
</tr>
</table>
</p>

<center><b>图8.2.4</b> 编译后的文档</center>


【回放】[**8.1 图表和公式的索引**](https://nbviewer.jupyter.org/github/xinychen/latex-cookbook/blob/main/chapter-8/section1.ipynb)

【继续】[**8.3 Bibtex用法**](https://nbviewer.jupyter.org/github/xinychen/latex-cookbook/blob/main/chapter-8/section3.ipynb)

### License

<div class="alert alert-block alert-danger">
<b>This work is released under the MIT license.</b>
</div>
