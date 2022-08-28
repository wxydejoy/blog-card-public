## 6.4 定制图表标题样式

使用`\caption`命令为浮动图片或者浮动表格创建的标题主要包含四部分：①标题头部、②自动编号、③编号分隔符、以及④标题名称，如下图所示。其中，对标题名称的设置比较简单，下面分别就标题前三部分的调整方式展开介绍。

<p align="center">
<img align="middle" src="docs/latex/chapter-6/graphics/eg_6.png" width="450" />
</p>

<center><b>图6.1.2</b> 图片标题的四个部分示意图</center>

### （1）调整标题头部

默认情况下，图片和表格标题头部分别为“Figure”和“Table”，我们可以分别使用`\renewcommand{\figurename}{新的图片标题头部}`和`\renewcommand{\tablename}{新的表格标题头部}`命令对其进行修改。

【**例6-4-1**】使用`\renewcommand`命令将图表题头部改为`Fig`。

```tex
\documentclass[12pt]{article}
\usepackage{graphicx}
\renewcommand{\figurename}{Fig}
\begin{document}

\begin{figure}
\centering
\includegraphics[width = 0.5\textwidth]{graphics/butterfly.JPG}
\caption{There is a beautiful butterfly.}
\label{butterfly}
\end{figure}

\end{document}
```

编译后的图表标题如图6.4.1所示。

<p align="center">
<img align="middle" src="docs/latex/chapter-6/graphics/exm_6_4_1.png" width="450" />
</p>

<center><b>图6.4.1</b> 编译后的插图效果</center>


### （2）调整编号

创建浮动表格或者浮动图片时，LaTeX会根据内置的计数器对其进行自动递增计数，计数值即为图表标题编号和引用编号，默认为小写的阿拉伯数字。

如果需要取消图表的自动编号，可以使用`caption`宏包提供的`\captionsetup[浮动体类型]{labelformat=empty}`命令，其中浮动体类型可以为figure、subfigure、table、或subtable，分别表示图片、子图、表格、子表。使用该命令后，指定浮动体类型下的所有浮动体将取消自动编号，但其标题和编号仍会显示在图表目录中。

【**例6-4-2**】使用`\caption*`命令取消部分表格的自动编号，同时使用`\captionsetup`命令取消所有图片的自动编号。

```tex
\documentclass{article}
\usepackage{graphicx}
\usepackage{caption}
\begin{document}

\captionsetup[figure]{labelformat=empty} % 取消所有图片的自动编号

Here are three created tables...
\begin{table}[h!]
% ...
\caption{The first table.}
\caption*{The second table.} % 取消该标题的自动编号
\caption{The third table.}
\end{table}

Here are three inserted figures...
\begin{figure}[h!]
% ...
\caption{The first figure.}
\caption{The second figure.}
\caption{The third figure.}
% ...
\end{figure}

\end{document}
```

编译后的图表标题如图6.1.2所示。

<p align="center">
<img align="middle" src="docs/latex/chapter-6/graphics/eg_7.png" width="450" />
</p>

<center><b>图6.4.2</b> 编译后的插图效果</center>

如果想要修改图表编号样式，可以在导言区使用`\renewcommand{浮动体的自动计数器}{计数器样式}`命令。其中，浮动体的自动计数器名称可以为`\thefigure`、`\thesubfigure`、`\thetable`、或`\thesubtable`；定义计数器样式可以使用`\alph{浮动体类型}`、`\Alph{浮动体类型}`、`\Roman{浮动体类型}`、`\arabic{浮动体类型}`等命令。

【**例6-4-3**】使用`\renewcommand`命令调整图表标题头部和编号样式。

```tex
\documentclass{article}
\usepackage{graphicx}

\renewcommand{\figurename}{Fig} % 调整图片头部
\renewcommand{\tablename}{Tab} % 调整新表格头部
\renewcommand{\thefigure}{\Alph{figure}} % 调整图片编号样式为大写字母
\renewcommand{\thetable}{\alph{table}} % 调整表格编号样式为小写字母

\begin{document}

Here are three created tables...
\begin{table}[h!]
% ...
\caption{The first table.}
\caption{The second table.}
\caption{The third table.}
\end{table}

Here are three inserted figures...
\begin{figure}[h!]
% ...
\caption{The first figure.}
\caption{The second figure.}
\caption{The third figure.}
% ...
\end{figure}

\end{document}
```

编译后的图表标题如图6.4.3所示。

<p align="center">
<img align="middle" src="docs/latex/chapter-6/graphics/eg_8.png" width="450" />
</p>

<center><b>图6.4.3</b> 编译后的插图效果</center>

### （3）调整编号分隔符

图表中的编号分隔符默认为英文冒号“:”，如果需要对其进行调整，可以使用`caption`宏包提供的`\captionsetup[浮动体类型]{设置labelsep选项}`命令，通过设置不同的labelsep选项实现，各选项及其含义如下：

- `colon`：默认值，即英文冒号“:”；

- `none`：无编号分隔符；

- `period`：英文句号“.”；

- `space`：一个空格；

- `quad`：一个字符“M”大小的空格；

- `newline`：换行。

【**例6-4-4**】使用`caption`宏包调整图标题编号分隔符为换行。

```tex
\documentclass[12pt]{article}

\usepackage{graphicx}
\usepackage{caption}
\renewcommand{\figurename}{Fig}
\captionsetup[figure]{labelsep=newline}

\begin{document}

\begin{figure}
\centering
\includegraphics[width = 0.5\textwidth]{graphics/butterfly.JPG}
\caption{There is a beautiful butterfly.}
\label{butterfly}
\end{figure}

\end{document}
```

编译后的图表标题如图6.4.4所示。

<p align="center">
<img align="middle" src="docs/latex/chapter-6/graphics/exm_6_4_4.png" width="450" />
</p>

<center><b>图6.4.4</b> 编译后的插图效果</center>


【回放】[**6.3 插入图表目录**](https://nbviewer.jupyter.org/github/xinychen/latex-cookbook/blob/main/chapter-6/section3.ipynb)

【继续】[**6.5 插入子图**](https://nbviewer.jupyter.org/github/xinychen/latex-cookbook/blob/main/chapter-6/section5.ipynb)

### License

<div class="alert alert-block alert-danger">
<b>This work is released under the MIT license.</b>
</div>
