## 6.1 基本插图方式

使用LaTeX制作文档时，可以使用特定的环境和命令插入各种格式的图形，但需要注意的是，LaTeX只支持一些常见的图形文件格式，例如PDF、JPG、JPEG和PNG。在众多图形格式中，SVG格式的矢量图可以有效避免失真，但 LaTeX不支持SVG格式，因此，有时候，我们会将SVG图片转换成PDF格式或者TikZ中的PGF格式。对于不同类型的图形，在使用前需要做一些基本处理：

- 绘制的图形。例如我们用Python、Matlab等程序语言绘制的图形，通常可以选择保存为PDF格式，并且在插入图形时，PDF格式的图片质量会优于PNG等格式。
- 截图。一般选择保存为PNG格式。另外，在LaTeX中插入这类图片之前，不宜随意改变图形的尺寸。


### 6.1.1 插入浮动图片

####  Graphicx宏包

`graphicx`是LaTeX插图的标准宏包，也是最为常用的。首先，我们需要先在前导代码中申明使用`graphicx`宏包，对应的命令为`\usepackage{graphicx}`，然后就可以在需要插图的位置插入对应的图片，基本命令为`\includegraphics{filename}`。

【**例1**】使用`graphicx`宏包中的`\includegraphics`命令插入图片butterfly.JPG。

```tex
\documentclass[12pt]{article}
\usepackage{graphicx}
\begin{document}

Figure \ref{butterfly} show a beautiful butterfly.

\includegraphics[width = 0.5\textwidth]{graphics/butterfly.JPG}
\caption{A beautiful butterfly.}
\label{butterfly}
\end{document}
```

编译后的插图效果如图6-1-1所示。

<p align="center">
<img align="middle" src="latex/chapter-6/graphics/eg_1.png" width="350" />
</p>

<center><b>图6-1-1</b> 编译后的插图效果</center>

#### figure环境

此外，`graphicx`宏包提供了`figure`环境语句，通过嵌套`\includegraphics`命令可以以浮动体的形式插入图片，从而能够实现自动递增编号、设置位置控制参数、利用`\caption`命令创建标题名称等。

【**例2**】使用`figure`环境插入图片butterfly.JPG。

```tex
\documentclass[12pt]{article}
\usepackage{graphicx}
\begin{document}

Figure \ref{butterfly} show a beautiful butterfly.

\begin{figure}
\centering
\includegraphics[width = 0.5\textwidth]{graphics/butterfly.JPG}
\caption{A beautiful butterfly.}
\label{butterfly}
\end{figure}

\end{document}
```
编译后的插图效果如图6-1-2所示。

<p align="center">
<img align="middle" src="latex/chapter-6/graphics/eg_1.png" width="350" />
</p>

<center><b>图6-1-2</b> 编译后的插图效果</center>

### 6.1.2 插入非浮动图片

通过`figure`环境插入图片虽然能够实现自动编号和创建图片标题，但创建结果为浮动图片，图片的显示位置与在代码中的位置未必一致。然而有时我们想要以非浮动体的形式插入图片，使得图片显示位置与代码中的位置一致，同时能够实现自动编号和创建标题，要实现这一效果，我们可以使用`minipage`环境或`center`环境替代`figure`环境插入图片，同时使用`caption`宏包提供的`\captionof{figure}{图片标题名称}`命令创建图片标题。

#### minipage环境

使用`minipage`环境插入图片的方式与`figure`环境类似，不同之处主要在于使用`minipage`环境插入的图片与上下文中的文本内容紧挨着，为了避免这种情况，`minipage`环境前后可以使用`\vspace{纵向距离}`调整图片与文本的纵向空间距离。

【**例3**】使用`minipage`环境语句取代`figure`环境语句插入非浮动图片，使用`\captionof`命令创建图片标题，并使用`\vspace`命令调整图片与文本的纵向距离。

```tex
\documentclass[12pt]{article}
\usepackage{graphicx}
\usepackage{caption}
\begin{document}

Figure \ref{fig:1} shows a beautiful butterfly.

\vspace{12pt}

\begin{minipage}{\linewidth}
\centering
    \includegraphics[width = 0.6\linewidth]{butterfly.JPG}
    \captionof{figure}{A beautiful butterfly.}
    \label{fig:1}
\end{minipage}

\vspace{12pt}

According to the picture, we know ...

\end{document}
```

编译后的插图效果如图6-1-3所示。

<p align="center">
<img align="middle" src="latex/chapter-6/graphics/eg_3.png" width="450" />
</p>

<center><b>图6-1-3</b> 编译后的插图效果</center>


#### center环境

另外，也可以使用`center`环境语句取代`minipage`环境语句插入非浮动图片。使用`center`环境语句插入图片时可以自动将图片居中放置。

【**例4**】使用`center`环境语句取代`figure`环境语句插入非浮动图片，并使用`\captionof`命令创建图片标题。

```tex
\documentclass[12pt]{article}
\usepackage{graphicx}
\usepackage{caption}
\begin{document}

Figure \ref{fig:1} shows a beautiful butterfly.

\begin{center}
\includegraphics[width = 0.6\linewidth]{butterfly.JPG}
\captionof{figure}{A beautiful butterfly.}
\label{fig:1}
\end{center}

According to the picture, we know ...

\end{document}
```

编译后的插图效果如图6-1-4所示。

<p align="center">
<img align="middle" src="latex/chapter-6/graphics/eg_4.png" width="450" />
</p>

<center><b>图6-1-4</b> 编译后的插图效果</center>

### 参考资料

[1] https://tex.stackexchange.com/questions/157222

【回放】[**6.0 导言**](https://nbviewer.jupyter.org/github/xinychen/latex-cookbook/blob/main/chapter-6/section0.ipynb)

【继续】[**6.2 调整插图样式**](https://nbviewer.jupyter.org/github/xinychen/latex-cookbook/blob/main/chapter-6/new_section2.ipynb)
