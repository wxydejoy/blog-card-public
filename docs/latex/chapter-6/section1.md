## 6.1 插入浮动图片

LaTeX中可以支持插入*.pdf、*.jpg、*.jpeg、*.png、*.eps等常见格式的图片，而对于LaTeX不支持的图片文件格式，如SVG格式的矢量图，则需要先转换再插入。一般而言，读者可以通过截图、MS Visio等绘图工具、或者Matlab等编程工具制作并导出目标图片。

在LaTeX中插入图片可以使用`graphicx`宏包，该宏包提供的`\includegraphics[参数]{文件名或文件路径}`命令可以用于插入图片，以及设置参数以调整图片样式，常用参数包括：

- `width`：设置图片宽度；

- `height`：设置图片高；

- `scale`：设置图片的缩放倍数；

- `angle`：设置图片的顺时针旋转角度（负值表示逆时针旋转）等。

一般而言，对于参数`height`和`width`，只需要调整其中一个即可，另一个参数将根据图片比例进行自动缩放。而如果同时调整了参数`height`和`width`（不推荐），可能会改变图片比例，导致图片变形。

【**例6-1-1**】在导言区使用`\usepackage{graphicx}`声明语句，在主体代码中使用`\includegraphics`命令插入图片，并调整图片样式参数。

```tex
\documentclass[12pt]{article}
\usepackage{graphicx}
\begin{document}

The following figure shows a beautiful butterfly.

\includegraphics[width = 0.5\textwidth]{butterfly.JPG} % 插入第一张图片

\vspace{12pt}

Rotate the figure by 90 degrees.

\includegraphics[width = 0.5\textwidth,angle = 90]{butterfly.JPG} % 插入第二张图片

\end{document}
```

编译后的插图效果如图6.1.1所示。

<p align="center">
<img align="middle" src="docs/latex/chapter-6/graphics/eg_2.png" width="350" />
</p>

<center><b>图6.1.1</b> 编译后的插图效果</center>

此外，`graphicx`宏包提供了`figure`环境语句，通过嵌套`\includegraphics`命令可以以浮动体的形式插入图片，从而能够实现自动递增编号、设置位置控制参数、利用`\caption`命令创建标题名称等。

【**例6-1-2**】使用`figure`环境嵌套`\includegraphics`命令插入浮动图片，并使用`\label`命令为图片创建索引标签，然后在文本内容中使用`\ref`命令引用该图片。

```tex
\documentclass[12pt]{article}
\usepackage{graphicx}
\begin{document}

Figure \ref{fig:1} shows a beautiful butterfly.
    
\begin{figure}[htbp]
\centering
    \includegraphics[width = 0.8\textwidth]{butterfly.JPG}
    \caption{A beautiful butterfly.}
    \label{fig:1}
\end{figure}

\end{document}
```
编译后的插图效果如图6.1.2所示。

<p align="center">
<img align="middle" src="docs/latex/chapter-6/graphics/eg_1.png" width="350" />
</p>

<center><b>图6.1.2</b> 编译后的插图效果</center>

如果想要创建取消编号的标题，则应调用`caption`宏包、并使用`\caption*`命令创建标题名称。此时，LaTeX内置的自动编号计数器将暂停，直到遇到下一个`\caption`命令才会继续递增计数，例如：

```tex
% ...
\caption{The first figure.} % 创建标题“Figure 1:  The first figure.”
\caption*{The second figure.} % 创建标题“The second figure.”
\caption{The third figure.} % 创建标题“Figure 2:  The third figure.”
% ...
```


【回放】[**6.0 导言**](https://nbviewer.jupyter.org/github/xinychen/latex-cookbook/blob/main/chapter-6/section0.ipynb)

【继续】[**6.2 插入非浮动图片**](https://nbviewer.jupyter.org/github/xinychen/latex-cookbook/blob/main/chapter-6/section2.ipynb)

### License

<div class="alert alert-block alert-danger">
<b>This work is released under the MIT license.</b>
</div>
