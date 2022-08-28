## 8.1 公式和图表的索引

在第4、5、6、7章中，分别介绍了如何制作或插入公式及图表，在文档中，我们往往需要对公式及图表进行引用以辅助文档的叙述、描述结果以及佐证一些结论。而有时为了排版的美观，所插入的公式或图表不一定直接放在引用位置旁边，因此对公式及图表进行索引就显得尤为重要了。


### 8.1.1 公式的索引

LaTeX中，公式的索引分为主要分为两个部分，一部分是给公式添加标签，可以使用`\label{标签名}`命令。根据第4章，可以使用`equation`环境插入带标签的公式；另一部分是在文档中进行引用，可以使用`\ref{标签名}`命令。

【**例8-1**】使用`\label{标签名}`及`\ref{标签名}`在文中对公式进行索引。

```tex
\documentclass[12pt]{article}
\begin{document}

(\ref{eq1}) is a binary equation

(\ref{eq2}) is a binary quadratic equation.

\begin{equation}
x+y=2\label{eq1}
\end{equation}

\begin{equation}
x^{2}+y^{2}=2\label{eq2}
\end{equation}

\end{document}

```
编译上述代码，得到文档如图8.1.1所示。

<p align="center">
<img align="middle" src="latex/chapter-8/graphics/example8_1_1.png" width="450" />
</p>

<center><b>图8.1.1</b> 编译后的文档</center>

### 8.1.2 图形的索引

根据第6章，插入图片需要使用`graphicx`宏包，图形的索引与公式的索引类似。同样分为两部分，一部分是使用`\label{标签名}`命令给添加图形标签，另一部分是使用`\ref{标签名}`在文档中进行引用。

【**例8-2**】使用`\label{标签名}`及`\ref{标签名}`在文中对图形进行索引。

```tex
\documentclass[12pt]{article}
\usepackage{graphicx}
\begin{document}

Figure \ref{butterfly} is a photo of butterfly.

\begin{figure}
\centering
\includegraphics[width = 0.8\textwidth]{graphics/butterfly.JPG}
\caption{There is a beautiful butterfly.}
\label{butterfly}
\end{figure}


\end{document}

```
编译上述代码，得到文档如图8.1.2所示。

<p align="center">
<img align="middle" src="latex/chapter-8/graphics/example8_1_2.png" width="450" />
</p>

<center><b>图8.1.2</b> 编译后的文档</center>

### 8.1.3 表格的索引

表格的索引与公式及图形的索引类似，同样分为两部分，一部分是使用`\label{标签名}`命令给添加表格标签。根据第5章，可以使用`tabular`和`table`两种环境制作带标签的表格；另一部分是使用`\ref{标签名}`在文档中进行引用。

【**例8-3**】使用`\label{标签名}`及`\ref{标签名}`在文中对表格进行索引。

```tex
\documentclass[12pt]{article}
\begin{document}

Table~\ref{table1} shows the values of some basic functions.

\begin{table}
    \centering
    \caption{The values of some basic functions.}
    \begin{tabular}{l|cccc}
        \hline
        & $x=1$ & $x=2$ & $x=3$ & $x=4$ \\
        \hline
        $y=x$ & 1 & 2 & 3 & 4 \\
        $y=x^{2}$ & 1 & 4 & 9 & 16 \\
        $y=x^{3}$ & 1 & 8 & 27 & 64 \\
        \hline
    \end{tabular}
    \label{table1}% 索引标签
\end{table}

\end{document}
```
编译上述代码，得到文档如图8.1.3所示。

<p align="center">
<img align="middle" src="latex/chapter-8/graphics/example8_1_3.png" width="450" />
</p>

<center><b>图8.1.3</b> 编译后的文档</center>


【回放】[**8.0 导言**](https://nbviewer.jupyter.org/github/xinychen/latex-cookbook/blob/main/chapter-8/section0.ipynb)

【继续】[**8.2 创建超链接**](https://nbviewer.jupyter.org/github/xinychen/latex-cookbook/blob/main/chapter-8/section2.ipynb)

### License

<div class="alert alert-block alert-danger">
<b>This work is released under the MIT license.</b>
</div>
