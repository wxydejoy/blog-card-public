## 6.2 插入非浮动图片

通过`figure`环境插入图片虽然能够实现自动编号和创建图片标题，但创建结果为浮动图片，图片的显示位置与在代码中的位置未必一致。然而有时我们想要以非浮动体的形式插入图片，使得图片显示位置与代码中的位置一致，同时能够实现自动编号和创建标题，要实现这一效果，我们可以使用`minipage`环境或`center`环境替代`figure`环境插入图片，同时使用`caption`宏包提供的`\captionof{figure}{图片标题名称}`命令创建图片标题。

使用`minipage`环境插入图片的方式与`figure`环境类似，不同之处主要在于使用`minipage`环境插入的图片与上下文中的文本内容紧挨着，为了避免这种情况，`minipage`环境前后可以使用`\vspace{纵向距离}`调整图片与文本的纵向空间距离。

【**例6-2-1**】使用`minipage`环境语句取代`figure`环境语句插入非浮动图片，使用`\captionof`命令创建图片标题，并使用`\vspace`命令调整图片与文本的纵向距离。

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

编译后的插图效果如图6.2.1所示。

<p align="center">
<img align="middle" src="latex/chapter-6/graphics/eg_3.png" width="450" />
</p>

<center><b>图6.2.1</b> 编译后的插图效果</center>

使用`center`环境语句插入图片时可以自动将图片居中放置。

【**例6-2-2**】使用`center`环境语句取代`figure`环境语句插入非浮动图片，并使用`\captionof`命令创建图片标题。

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

编译后的插图效果如图6.2.2所示。

<p align="center">
<img align="middle" src="latex/chapter-6/graphics/eg_4.png" width="450" />
</p>

<center><b>图6.2.2</b> 编译后的插图效果</center>

在论文写作中，有时需要将多个图片放在同一行进行排列以便于比较。在`figure`环境中，使用`minnipage`环境即可实现图片并排显示，并连续编号。

【**例6-2-3**】使用`figure`环境嵌套`minnipage`环境实现多图并排显示。

```tex
\documentclass[11pt]{article}
\usepackage{graphicx}

\begin{document}

The two figures are displayed side by side.

\begin{figure}[htbp]
\centering
\begin{minipage}[t]{0.48\textwidth} 
\centering
\includegraphics[width=6cm]{graphics/butterfly.jpg}
\caption{Butterfly-1}
\end{minipage}%
\begin{minipage}[t]{0.48\textwidth}
\centering
\includegraphics[width=6cm]{graphics/butterfly.jpg}
\caption{Butterfly-2}
\end{minipage}
\end{figure}

\end{document}
```

编译后的插图效果如图6.2.3所示。

<p align="center">
<img align="middle" src="latex/chapter-6/graphics/example6_2_1.png" width="450" />
</p>

<center><b>图6.2.3</b> 编译后的插图效果</center>

### 参考资料

[1] https://tex.stackexchange.com/questions/157222

【回放】[**6.1 插入浮动图片**](https://nbviewer.jupyter.org/github/xinychen/latex-cookbook/blob/main/chapter-6/section1.ipynb)

【继续】[**6.3 插入图表目录**](https://nbviewer.jupyter.org/github/xinychen/latex-cookbook/blob/main/chapter-6/section3.ipynb)

### License

<div class="alert alert-block alert-danger">
<b>This work is released under the MIT license.</b>
</div>
