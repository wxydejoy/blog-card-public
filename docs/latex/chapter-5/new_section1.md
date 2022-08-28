## 5.1 基本介绍

表格是展现数据的一种常用方式。LaTeX提供了多种表格环境用于制作各类表格，例如，`tabular`、`tabular*`、`tabularx`、`tabulary`、`table`和`longtable`等。其中比较常用的方法是将`tabular`环境嵌入到`table`环境中，可以创建包含表格内容、表格标题、引用标签等属性的完整表格。


### 5.1.1 `tabular`环境：创建表格内容

通过创建`tabular`环境可以定义表格内容、对齐方式、外观样式等，使用方式与前面章节中介绍的使用`array`环境制作数表（即矩阵）的方式类似。例如：

$$\left[\begin{array}{c|c|c} a & b & c \\ \hline d & e & f \\ \hline g & h & i \\ \end{array}\right]$$

的创建代码为`\left[\begin{array}{c|c|c} a & b & c \\ \hline d & e & f \\ \hline g & h & i \\ \end{array}\right]`。

不妨将上述代码中的`array`环境改写为`tabular`环境，并去掉`left[`和`\right]`命令，得到如下所示的代码语句：

```tex
\documentclass[12pt]{article}
\begin{document}

\begin{tabular}{c|c|c}
a & b & c \\
\hline
d & e & f \\
\hline
g & h & i \\
\end{tabular}

\end{document}
```

编译上述代码，可以得到类似的结果：

<p align="center">
<img align="middle" src="docs/latex/chapter-5/graphics/eg5_1.png" width="100">
</p>

<center><b>图5-1-1</b> 编译后的幻灯片效果</center>

这里制作出来的表格是文本模式下的，跟array环境制作的数学模式略有不同，不同之处在于，`array`环境制作的数表是属于数学公式，而使用`tabular`环境制作得到的表格则属于文本内容，但两者的用法及命令格式极其相似。在`tabular`环境下：

- 在`\begin{tabular}`命令后的`{}`内设置表格的列类型参数，包括：

    - 设置每列的单元格对齐方式。对齐方式选项包括`l`、`c`和`r`，即left、center和right的首字母，分别对应左对齐、居中对齐和右对齐，每个字母对应一列；
    
    - 创建表格列分隔线。表格列分隔线以`|`符号表示，`|`符号的个数表示列分隔线中线的个数，如`|`表示使用单线分隔列，`||`表示使用双线分隔列，以此类推。分割线符号可以设置在列对齐方式选项的左侧或右侧，分别表示创建列的左分隔线和右分隔线。
    
- 使用`\\`符号表示一行内容的结束；

- 使用`&`符号划分行内的单元格；

- 使用`\hline`命令创建行分隔线。

在tabular环境中，行分割线亦也可以通过\usepackage{booktabs}调用booktabs宏包，并分别使用\toprule，\midrule和\bottomrule命令来添加不同粗细的横线。其中，在调用booktabs的情况下，可以通过\cmidrule[thickness]{a-b}来实现自定义横线，[thickness]控制横线的粗细，{a-b}指定横线需要横跨的列序号。具体内容可以参阅参考http://texdoc.net/pkg/booktabs.

下面给出一个示例让读者对`tabular`环境的使用方式能有更深刻的印象。

【**例1**】使用`tabular`环境制作一个简单的表格，并使用`\begin{tabular}{l|cccr}`命令调整列对齐方式。

```tex
\documentclass[12pt]{article}
\begin{document}

\begin{tabular}{|l|c|c|c|}
   \hline
    Column1 & Column2 & Column3 & Column4\\
   \hline
    A1 & A2 & A3 & A4\\
   \hline
    B1 & B2 & B3 & B4\\
   \hline
    C1 & C2 & C3 & C4\\
   \hline
\end{tabular}

\end{document}
```

编译上述代码，得到表格如图5-1-2所示。

<p align="center">
<img align="middle" src="docs/latex/chapter-5/graphics/newexm5_1_1.png" width="350" />
</p>

<center><b>图5-1-2</b> 编译后的文档内容</center>


### 5.1.2 `table`环境：自动编号与浮动表格

使用`table`环境嵌套`tabular`环境，能够为创建的表格进行自动递增编号。此外，可以使用`\caption{}`命令设置表格标题、使用`\label{}`命令为表格建立索引标签、使用`\centering`命令将表格置于文档中间，如下所示：

```tex
\begin{table}
\centering
    \caption{Title of a table.}
    \label{Label of the table}
    \begin{tabular}
    % 表格内容
    \end{tabular}
\end{table}
```

下例中将 例1 创建的表格嵌入到`table`环境中，创建了一个位置居中、并且具有标题、索引、自动编号的表格。

【**例2**】使用`table`和`tabular`环境制作一个简单的表格。

```tex
\documentclass[12pt]{article}

\begin{document}

Table~\ref{table1} shows the example of ABC.

\begin{table}
    \centering
    \caption{Example of ABC}
    		\begin{tabular}{|c|c|c|c|}
    		\hline
    		Column1 & Column2 & Column3 & Column4\\
    		\hline
    		A1 & A2 & A3 & A4\\
    		\hline
    		B1 & B2 & B3 & B4\\
    		\hline
    		C1 & C2 & C3 & C4\\
    		\hline
    \end{tabular}    
\label{table1}% 索引标签
\end{table}

\end{document}

```

编译上述代码，得到表格如 图5-1-3 所示。

<p align="center">
<img align="middle" src="docs/latex/chapter-5/graphics/newexm5_1_3.png" width="350">
</p>

<center><b>图5-1-3</b> 编译后的幻灯片效果</center>

事实上，在`\begin{table} \end{table}`环境中创建的表格属于浮动元素:

> 浮动元素（floating）是指不能跨页分割的元素，比如图片和表格。一般而言，浮动元素的显示位置未必是代码的位置，比如，当页面空间不足时，LaTeX会根据内置的算法尝试将浮动元素放置到后面的页面中，避免出现内容跨页分割或者页面大量留白的情况，从而创建更协调也更专业的文档。

通过在`\begin{table}[]`的`[]`中设置位置控制参数，可以为浮动表格指定期望放置位置，各参数值及其含义如下：

- `h`：英文单词here的首写字母，表示代码当前位置；

- `t`：英文单词top的首写字母，表示页面顶部位置；

- `b`：英文单词bottom的首写字母，表示页面底部位置；

- `p`：英文单词page的首写字母，表示后面的页面；

- `!`：`!`参数一般与其它位置参数配合使用，表示当空间足够时，强制将表格放在指定位置。如`!h`表示将表格强制放到当前页面，但当页面空间不足时，也可能被放置到后续页面中；

- `H`：表示将表格强制放在代码当前位置，具有比`!h`更严格的效果，使用时需要先在导言区使用`\usepackage{float}`声明语句调用float宏包。

根据需要，浮动元素的位置控制参数一般可以设置为`h`、`b`、`t`、`p`、`!`和`H`的任意无序组合。该参数的缺省值为`tbp`，此时LaTeX会尝试将表格放在页面的顶端或者底端，否则会将表格放在下一页。

【**例3**】在`table`环境中将表格的位置控制参数设置为`htbp`。

```tex
\documentclass[12pt]{article}
\begin{document}

Table~\ref{table1} shows the Example of ABC.

\begin{table}[htbp] % 位置参数
    \centering
    \caption{Example of ABC..}
       	\begin{tabular}{|c|c|c|c|}
    		\hline
    		Column1 & Column2 & Column3 & Column4\\
    		\hline
    		A1 & A2 & A3 & A4\\
    		\hline
    		B1 & B2 & B3 & B4\\
    		\hline
    		C1 & C2 & C3 & C4\\
    		\hline
    \end{tabular}      
\label{table1}
\end{table}

\end{document}

```

编译上述代码，得到表格如图5-1-4所示。

<p align="center">
<img align="middle" src="docs/latex/chapter-5/graphics/newexm5_1_4.png" width="450" />
</p>

<center><b>图5-1-4</b> 编译后的文档内容</center>

【回放】[**5.0 导言**](https://nbviewer.jupyter.org/github/xinychen/latex-cookbook/blob/main/chapter-5/new_section0.ipynb)

【继续】[**5.2 调整表格内容**](https://nbviewer.jupyter.org/github/xinychen/latex-cookbook/blob/main/chapter-5/new_section2.ipynb)
