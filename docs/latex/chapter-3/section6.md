## 3.6 创建列表

在内容表达上，列表是一种非常有效的方式，它将某一论述内容分成若干个条目进行罗列，能达到简明扼要、醒目直观的表达效果。在论文写作中，列表不失为一种让内容清晰明了的论述方式。

按层次分，列表有单层列表和多层列表，多层列表无外乎是最外层列表中嵌套了一层甚至更多层列表。按类型分，列表主要有三种类型，即无序列表、排序列表和阐述性列表，其中，无序列表和排序列表是相对常用的列表类型，LaTeX针对这三种列表提供了一些基本环境：

- 无序列表的使用方法为：

```tex
\begin{itemize}

\item Item 1 % 条目1
\item Item 2 % 条目2

\end{itemize}
```

- 排序列表的使用方法为：

```tex
\begin{enumerate}

\item Item 1 % 条目1
\item Item 2 % 条目2

\end{enumerate}
```

- 阐述性列表的使用方法为：

```tex
\begin{description}

\item Item 1 % 条目1
\item Item 2 % 条目2

\end{description}
```

在这三种列表中，我们创建的每一项列表内容都需要紧随`\item`命令之后。当然，有时候，我们也可以根据需要选择合适的列表类型、调整列表符号甚至行间距等。



### 3.6.1 无序列表

LaTeX中的无序列表环境一般用特定符号（如圆点、星号）作为列表中每个条目的起始标志，以示有别于常规文本。可以忽略主次或者先后顺序关系的条目排列都可以使用无序列表环境来编写，无序列表时很多文档最常用的列表类型，也被称为常规列表。

【**例1**】使用无需列表环境创建一个简单的无序列表。

```tex
\documentclass[12pt]{article}
\begin{document}
\begin{itemize}

\item Python % 条目1
\item LaTeX  % 条目2
\item GitHub % 条目3

\end{itemize}
\end{document}
```
编译上述代码，得到列表如图3-6-1所示。

<p align="center">
<img align="middle" src="docs/latex/chapter-3/graphics/example3_6_1.png" width="300" />
</p>

<center><b>图3-6-1</b> 编译后列表</center>


在无序列表环境中，每个条目都是以条目命令`\item`开头的，一般默认的起始符号是textbullet，即大圆点符号，当然，也可以根据需要调整起始符号。

【**例2**】在无需列表环境中使用星号作为条目的起始符号。

```tex
\documentclass[12pt]{article}
\begin{document}
\begin{itemize}

\item Python    % 条目1，起始符号为大圆点
\item LaTeX     % 条目2，起始符号为大圆点
\item[*] GitHub % 条目3，起始符号为星号

\end{itemize}
\end{document}
```
编译上述代码，得到列表如图3-6-2所示。

<p align="center">
<img align="middle" src="docs/latex/chapter-3/graphics/example3_6_2.png" width="300" />
</p>

<center><b>图3-6-2</b> 编译后列表</center>


如果想要将所有条目的符号都进行调整，并统一为某一个特定符号，则可以使用`\renewcommand`命令进行自定义。

【**例3**】自定义条目的起始符号为黑色方块（black square）。

```tex
\documentclass[12pt]{article}
\usepackage{amssymb}
\begin{document}

\begin{itemize}
 \renewcommand{\labelitemi}{\scriptsize$\blacksquare$}
    \item Python % 条目1
    \item LaTeX  % 条目2
    \item GitHub % 条目3
\end{itemize}

\end{document}
```
编译上述代码，得到列表如图3-6-3所示。

<p align="center">
<img align="middle" src="docs/latex/chapter-3/graphics/example3_6_3.png" width="300" />
</p>

<center><b>图3-6-3</b> 编译后列表</center>


其中，命令`\labelitemi`是由三部分组成，即`label`（标签）、`item`（条目）、`i`（一级），有时候，如果需要创建多级列表，则可以类似这里使用命令`\labelitemii`（对应于二级列表）甚至`\labelitemiii`（对应于三级列表）。




### 3.6.2 排序列表

排序列表也被称为编号列表。在排序列表中，每个条目之前都有一个标号，它是由标志和序号两部分组成：序号自上而下，从1开始升序排列；标志可以是括号或小圆点等符号。相互之间有密切的关联，通常是按过程顺序或是重要程度排列的条目都可以采用排序列表环境编写。排序列表环境`enumerate`以序号作为列表的起始标志，每个条目命令item将在每个条目之前自动加上一个标号条目命令`item`生成的默认标号样式为阿拉伯数字加小圆点。

【**例4**】创建一个简单的排序列表。

```tex
\documentclass[12pt]{article}
\begin{document}

\begin{enumerate}

\item Python % 条目1
\item LaTeX  % 条目2
\item GitHub % 条目3

\end{enumerate}

\end{document}
```
编译上述代码，得到列表如图3-6-4所示。

<p align="center">
<img align="middle" src="docs/latex/chapter-3/graphics/example3_6_4.png" width="300" />
</p>

<center><b>图3-6-4</b> 编译后列表</center>


排序列表同样可以进行相互嵌套，最多可以达到四层，为了便于区分，不仅每层列表的条目段落都有不同程度的左缩进，二期每层列表中条目的标号也各不相同，其中序号的计数形式与条目所在的层次有关，标志所用的符号除第2层是圆括号外，其他各层都是小圆点。

【**例5**】创建一个简单的嵌套4层的排序列表。

```tex
\documentclass[12pt]{article}
\begin{document}

\begin{enumerate}
\item pencil
\item calculator
\item ruler
\item notebook
    \begin{enumerate}
    \item notes
        \begin{enumerate}
        \item note A
            \begin{enumerate}
            \item note a
            \end{enumerate}
        \item note B
        \end{enumerate}
    \item homework
    \item assessments
    \end{enumerate}
\end{enumerate}

\end{document}
```
编译上述代码，得到列表如图3-6-5所示。

<p align="center">
<img align="middle" src="docs/latex/chapter-3/graphics/example3_6_5.png" width="300" />
</p>

<center><b>图3-6-5</b> 编译后列表</center>



### 3.6.3 阐述性列表

相比无序列表和排序列表，阐述性列表的使用频率较低，它常用于对一组专业术语进行解释说明。阐述性列表环境为`description`。在`description`环境命令中，每个词条都是需要分别进行阐述的词语，每个阐述可以是一个或多个文本段落。这种形式很像词典，因此诸如名词解释说明之类的列表就可以采用解说列表环境来编写。在阐述性列表环境中，被解释的词条的格式是用`descriptionlabel`定义的。

【**例6**】创建一个简单的阐述性列表。

```tex
\documentclass[12pt]{article}
\begin{document}

\begin{description}

\item [CNN] Convolutional Neural Networks
\item [RNN] Recurrent Neural Network
\item [CRNN] Convolutional Recurrent Neural Network

\end{description}

\end{document}
```

编译上述代码，得到列表如图3-6-6所示。

<p align="center">
<img align="middle" src="docs/latex/chapter-3/graphics/example3_6_6.png" width="300" />
</p>

<center><b>图3-6-6</b> 编译后列表</center>





### 3.6.4 自定义列表格式

使用系统默认的LaTeX列表环境排版的列表与上下文之间以及列表条目之间都附加有一段垂直空白，明显有别于列表环境之外的文本格式，通常列表中的条目内容都很简短，这样会造成很多空白，使得列表看起来很稀疏，与前后文本之间的协调性较差。因此，我们需要自定义列表格式。使用 `enumitem`宏包可以调整`enumerate`或`itemize`的上下左右缩进间距。

#### 垂直间距

- `topsep`       列表环境与上文之间的距离
- `parsep`       条目里面段落之间的距离
- `itemsep`       条目之间的距离
- `partopsep`     条目与下面段落的距离

####  水平间距
- `leftmargin`       列表环境左边的空白长度
- `rightmargin`       列表环境右边的空白长度
- `labelsep`       标号与列表环境左侧的距离
- `itemindent`       条目的缩进距离
- `labelwidth`       标号的宽度
- `listparindent`       条目下面段落的缩进距离

【**例7**】使用`enumitem`宏包可以调整无序列表间距。

```tex
\documentclass[12pt]{article}
\usepackage{enumitem}
\begin{document}


Default spacing:

\begin{itemize}

\item Python % 条目1
\item LaTeX  % 条目2
\item GitHub % 条目3

\end{itemize}

Custom Spacing:

\begin{itemize}[itemsep= 15 pt,topsep = 20 pt]

\item Python % 条目1
\item LaTeX  % 条目2
\item GitHub % 条目3

\end{itemize}

\end{document}
```

编译上述代码，得到列表如图3-6-7所示。

<p align="center">
<img align="middle" src="docs/latex/chapter-3/graphics/example3_6_7.png" width="300" />
</p>

<center><b>图3-6-7</b> 编译后列表</center>


【回放】[**3.5 编辑文字**](https://nbviewer.jupyter.org/github/xinychen/latex-cookbook/blob/main/chapter-3/section5.ipynb)

【继续】[**3.7 创建页眉、页脚及脚注**](https://nbviewer.jupyter.org/github/xinychen/latex-cookbook/blob/main/chapter-3/section7.ipynb)

### License

<div class="alert alert-block alert-danger">
<b>This work is released under the MIT license.</b>
</div>
