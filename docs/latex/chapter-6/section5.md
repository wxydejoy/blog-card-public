## 6.5 插入子图

有时候需要将一组图片以子图的方式呈现，达到对比或者互补的效果。在LaTeX中，插入子图比较常用的方式是使用`subfigure`环境。

### （1）基本介绍

子图一般在`subfigure`环境中创建，多个子图环境嵌套在`figure`环境中从而形成同一组子图。`subfigure`环境与`figure`环境的使用方式基本类似，可以为每个子图分别创建标题和索引标签，方便说明和引用。

【**例6-2**】在导言区使用`\usepackage{subcaption}`语句，在代码主体区域使用`figure`环境嵌套三个`subfigure`环境从而创建三个子图，并为各子图分别创建索引和标题。

```tex
\documentclass[12pt]{article}
\usepackage{graphicx}
\usepackage{subcaption}
\begin{document}

Figure \ref{fig:fig1} contains sub-figure \ref{subfig:subfig1}, sub-figure \ref{subfig:subfig2} and sub-figure \ref{subfig:subfig3}.
    
\begin{figure}[h!]
\centering
    % 插入第一张子图
    \begin{subfigure}{.3\linewidth}
        \centering
        \includegraphics[width=.5\linewidth]{redflower.png}
        \caption{A red flower.}
        \label{subfig:subfig1}
    \end{subfigure}
    % 插入第二张子图
    \begin{subfigure}{.3\linewidth}
        \centering
        \includegraphics[width=.5\linewidth]{yellowFlower.png}
        \caption{A yellow flower.}
        \label{subfig:subfig2}
    \end{subfigure}
    % 插入第三张子图
    \begin{subfigure}{.3\linewidth}
        \centering
        \includegraphics[width=.5\linewidth]{blueFlower.png}
        \caption{A blue flower.}
        \label{subfig:subfig3}
    \end{subfigure}
\caption{Three flowers with different colors.}
\label{fig:fig1}
\end{figure}

\end{document}
```

编译后的图片如图6.1.2所示。

<p align="center">
<img align="middle" src="latex/chapter-6/graphics/eg_9.png" width="450" />
</p>

<center><b>图6.1.2</b> 编译后的插图效果</center>

在上例中，每个子图都用到了两次宽度设置选项，分别具有不同含义：

- `\begin{subfigure}{.3\linewidth}`表示将该子图环境的宽度设置为页面宽度的0.4倍；

- `\includegraphics[width=.5\linewidth]`表示将该图片的宽度设置为当前子图环境宽度的0.5倍。

### （2）调整子图间距

通过调整子图的横向和纵向间距，可以创建更协调美观的图片。

具体而言，存在以下三类命令可用于调整图片的横向间距：

- `\hfill`：对于位于相同行的子图，通过在相邻的`subfigure`环境间使用该命令，可以实现多个子图横向等距分布的效果；

> 通过调整子图环境的宽度，可以让子图位于相同行。

- `\hspace{横向距离}`：定制任意长度的横向图片距离。当该值设为负值时，可以产生图片重叠的效果；

- `\quad`、`\qquad`等：设置不同预设长度的横向图片距离。

【**例6-2**】使用`\hfill`命令实现子图横向等距分布，以及使用`\hspace{}`命令实现子图重叠效果。

```tex
\documentclass[12pt]{article}
\usepackage{graphicx}
\usepackage{subcaption}
\usepackage{amssymb}
\usepackage{amsmath}
\begin{document}

% 使用\hfill命令调整子图横向间距

The horizontal space among Sub-figures in figure \ref{fig:fig1} is controlled by $\backslash$\textit{hfill}.

\begin{figure}[h!]
\centering
    % 插入第一张子图
    \begin{subfigure}{.3\linewidth}
        \centering
        \includegraphics[width=.5\linewidth]{redflower.png}
        \caption{A red flower.}
    \end{subfigure}
    \hfill
    % 插入第二张子图
    \begin{subfigure}{.3\linewidth}
        \centering
        \includegraphics[width=.5\linewidth]{yellowFlower.png}
        \caption{A yellow flower.}
    \end{subfigure}
    \hfill
    % 插入第三张子图
    \begin{subfigure}{.3\linewidth}
        \centering
        \includegraphics[width=.5\linewidth]{blueFlower.png}
        \caption{A blue flower.}
    \end{subfigure}
\caption{Three flowers with different colors.}
\label{fig:fig1}
\end{figure}

% 使用\space{}命令调整子图横向间距

The horizontal space among Sub-figures in figure \ref{fig:fig2} is controlled by $\backslash$\textit{space}.

\begin{figure}[h!]
\centering
    % 插入第一张子图
    \begin{subfigure}{.3\linewidth}
        \centering
        \includegraphics[width=.5\linewidth]{redflower.png}
    \end{subfigure}
    \hspace{-5cm}
    % 插入第二张子图
    \begin{subfigure}{.3\linewidth}
        \centering
        \includegraphics[width=.5\linewidth]{yellowFlower.png}
    \end{subfigure}
    \hspace{-5cm}
    % 插入第三张子图
    \begin{subfigure}{.3\linewidth}
        \centering
        \includegraphics[width=.5\linewidth]{blueFlower.png}
    \end{subfigure}
\caption{Three flowers with different colors.}
\label{fig:fig2}
\end{figure}

\end{document}
```

编译后的图片如图6.1.2所示。

<p align="center">
<img align="middle" src="latex/chapter-6/graphics/eg_10NEW.png" width="450" />
</p>

<center><b>图6.1.2</b> 编译后的插图效果</center>

如果想让图片实现纵向等距分布，可以使用`\vfill`命令。

【**例6-2**】使用`\vfill`命令实现子图纵向等距分布。

```tex
\documentclass[12pt]{article}
\usepackage{graphicx}
\usepackage{subcaption}
\begin{document}

\begin{figure}[h!]
\centering
    % 插入第一张子图
    \begin{subfigure}{.3\linewidth}
        \centering
        \includegraphics[width=.5\linewidth]{redflower.png}
        \caption{A red flower.}
    \end{subfigure}
    \vfill
    % 插入第二张子图
    \begin{subfigure}{.3\linewidth}
        \centering
        \includegraphics[width=.5\linewidth]{yellowFlower.png}
        \caption{A yellow flower.}
    \end{subfigure}
    \vfill
    % 插入第三张子图
    \begin{subfigure}{.3\linewidth}
        \centering
        \includegraphics[width=.5\linewidth]{blueFlower.png}
        \caption{A blue flower.}
    \end{subfigure}
\caption{Three flowers with different colors.}
\label{fig:fig1}
\end{figure}

\end{document}
```

编译后的图片如图6.1.2所示。

<p align="center">
<img align="middle" src="latex/chapter-6/graphics/eg_11.png" width="300" />
</p>

<center><b>图6.1.2</b> 编译后的插图效果</center>


【**例**】位置调整

```tex
\documentclass[12pt]{article}
\usepackage{graphicx}
\begin{document}

There is a blue and black butterfly dancing among the colorful flowers. 

\begin{figure}[t!]
\centering
\includegraphics[width = 0.5\textwidth]{graphics/butterfly.JPG}
\caption{There is a beautiful butterfly.}
\label{butterfly}
\end{figure}

\end{document}
```

【**例**】文字环绕
```tex
\documentclass[12pt]{article}
\usepackage{graphicx}
\usepackage{wrapfig}
\begin{document}

There is a blue and black butterfly dancing among the colorful flowers. 

\begin{wrapfigure}{r}{8cm}
\centering
\includegraphics[width =0.35\textwidth]{graphics/butterfly.JPG}
\caption{There is a beautiful butterfly.}
\label{butterfly}
\end{wrapfigure}

In descriptive statistics, a box plot or boxplot is a method for graphically depicting groups of numerical data through their quartiles. Box plots may also have lines extending from the boxes (whiskers) indicating variability outside the upper and lower quartiles, hence the terms box-and-whisker plot and box-and-whisker diagram. Outliers may be plotted as individual points. Box plots are non-parametric: they display variation in samples of a statistical population without making any assumptions of the underlying statistical distribution (though Tukey's boxplot assumes symmetry for the whiskers and normality for their length).

\end{document}
```

【回放】[**6.4 定制图表标题样式**](https://nbviewer.jupyter.org/github/xinychen/latex-cookbook/blob/main/chapter-6/section4.ipynb)

### License

<div class="alert alert-block alert-danger">
<b>This work is released under the MIT license.</b>
</div>
