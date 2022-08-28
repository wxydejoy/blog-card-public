## 3.7 创建页眉、页脚及脚注

在大多数文档中，我们往往需要页眉、页脚及脚注来展示文档的附加信息，例如时间、图形、页码、日期、公司微标、页眉示意图文档标题、文件名或作者姓名等信息。在LaTeX中，我们常用`Fancyhdr`工具包进行页眉、页脚的设置。

【**例1**】使用`Fancyhdr`工具包进行页眉、页脚的设置。

```tex
\documentclass{article}
\usepackage{fancyhdr}
\pagestyle{fancy}
\lhead{}
\chead{}

\rhead{\bfseries latex-cookbook} %页眉内容
\lfoot{From: Xinyu Chen} %页脚内容
\cfoot{To: Jieling Jin} %页脚内容
\rfoot{\thepage} %在页脚处给出页码
\renewcommand{\headrulewidth}{0.4pt}
\renewcommand{\footrulewidth}{0.4pt}

\begin{document}
This is latex-cookbook!
\end{document}
```

编译上述代码后，得到文档如图3-7-1所示。

<p align="center">
<table>
<tr>
<td><img align="middle" src="latex/chapter-3/graphics/example3_7_1_1.png" width="500"></td>
</tr>
</table>
</p>

<center><b>图3-7-1</b> 编译后文档</center>

如果想某一页不需要页眉页脚，可以在该页正文内容开始时使用`\thispagestyle{empty}`命令，去除该页页眉页脚。

【**例2**】使用`\thispagestyle{empty}{empty}`命令去掉第二页页眉页脚。

```tex
\documentclass{article}
\usepackage{fancyhdr}
\pagestyle{fancy}
\lhead{}
\chead{}

\rhead{\bfseries latex-cookbook}
\lfoot{From: Xinyu Chen}
\cfoot{To: Jieling Jin}
\rfoot{\thepage}
\renewcommand{\headrulewidth}{0.4pt}
\renewcommand{\footrulewidth}{0.4pt}

\begin{document}
This is latex-cookbook!
\newpage
\thispagestyle{empty}
This is latex-cookbook!
\end{document}
```
编译上述代码后，得到文档如图3-7-2所示。

<p align="center">
<table>
<tr>
<td><img align="middle" src="latex/chapter-3/graphics/example3_7_2_1.png" width="300"></td>
<td><img align="middle" src="latex/chapter-3/graphics/example3_7_2_2.png" width="300"></td>
</tr>
</table>
</p>

<center><b>图3-7-2</b> 编译后文档</center>

脚注也是一篇文档中的重要内容，一般用来解释文档中的名词或相关出处。在LaTeX中，我们常用`\footnote{}`命令来添加脚注。

【**例3**】使用`\footnote{}`命令来添加脚注。

```tex
\documentclass{article}

\begin{document}

Xinyu Chen\footnote{Xinyu Chen is a PhD from the University of Montreal.} and Jieling Jin\footnote{Jieling Jin is a PhD from the Central South University.} are the two authors of latex-cookbook.

\end{document}
```

编译上述代码后，得到文档如图3-7-3所示。

<p align="center">
<table>
<tr>
<td><img align="middle" src="latex/chapter-3/graphics/example3_7_3.png" width="500"></td>
</tr>
</table>
</p>

<center><b>图3-7-3</b> 编译后文档</center>

在论文撰写过程中，我们有时会需要在表格中添加脚注，但是在table环境中，`\footnote `命令不起作用，这时我们可以使用`minipage`环境来化解。

【**例4**】使用`minipage`环境来给表格添加脚注。

```tex
\documentclass{article}
\begin{document}
\begin{center}
    \begin{minipage}{.5\textwidth}
    \begin{tabular}{l|l}
        \textsc{Chapter} & \textsc{Author} \\ \hline
        \textit{Introduction} & Xinyu Chen\footnote{Xinyu Chen is a PhD from the University of Montreal.}  \\
        \textit{Methods} & Jieling Jin \footnote{Jieling Jin is a PhD from the Central South University.} \\
        \textit{Case Study} & Xinyu Chen \\
        \textit{Conclusion} & Jieling Jin
        \end{tabular}
    \end{minipage}
    \end{center}
\end{document}
```

编译后效果如图3-7-4所示。

<p align="center">
<img align="middle" src="latex/chapter-3/graphics/example3_7_4.png" width="600" />
</p>

<center><b>图3-7-4</b> 编译后效果</center>

【回放】[**3.6 创建列表**](https://nbviewer.jupyter.org/github/xinychen/latex-cookbook/blob/main/chapter-3/section6.ipynb)

### License

<div class="alert alert-block alert-danger">
<b>This work is released under the MIT license.</b>
</div>
