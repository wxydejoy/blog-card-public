## 5.2 调整表格内容

在表格进行了初步的建立以后，首先需要对表格里面的内容进行调整，主要包括表格字体大小、表格表注、插入斜线、文本对齐、数字位数对齐等。


### 5.2.1 调整字体大小

在文本编辑中我们知道：调整字体大小的方式有全局的，也有局部的，全局的方式是文档类型中指定字体大小，例如12pt，而局部的方式则是通过一系列命令，例如`\large、Large、huge、\fontsize`等。使用LaTeX新建表格时，我们也可以对表格内字体大小做调整。

【**例1**】使用\Large命令调整表格字体大小。

```tex
\documentclass[12pt]{article}
\usepackage{booktabs}
\begin{document}
% 正常字体大小

\begin{table}
    \centering
    \begin{tabular}{|l|l|l|l|}
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
\end{table}
% Large字体大小
\begin{table}
    \Large
    \centering
    \begin{tabular}{|l|l|l|l|}
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
\end{table}

\end{document}
```

编译上述代码，得到表格如图5-2-1所示。

<p align="center">
<img align="middle" src="latex/chapter-5/graphics/newexm5_2_1.png" width="350" />
</p>

<center><b>图5-2-1</b> 编译后的文档内容</center>


【**例2**】使用\fontsize命令通过具体设置来调整表格字体大小。

```tex
\documentclass[12pt]{article}

\usepackage{booktabs}

\begin{document}

\begin{table}
    \fontsize{0.5cm}{0.8cm}\selectfont
    \centering
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
 \end{table}

\begin{table}
    \fontsize{0.5cm}{0.8cm}\selectfont
    \centering
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
 \end{table}
 
\end{document}
```
编译上述代码，得到表格如图5-2-2所示。

<p align="center">
<img align="middle" src="latex/chapter-5/graphics/newexm5_2_2.png" width="350" />
</p>

<center><b>图5-2-2</b> 编译后的文档内容</center>

### 5.2.2 插入表格注释

表格中的文本应当尽可能地保持简洁明了。因此，在保持简明的基础上，可以采用注释的方式以添加必要的细节对文本内容进行说明补充。通常，在以表格为载体的内容中，为了保持表格内容的完整性和独立性，我们往往不采用脚注`\footnote{}`的形式，而是将注释添加在表格底部（称之为表注）。

在LaTeX中添加表注的方式有多种，其中比较常用的一种是使用`threeparttable`宏包及其相关命令，可以在表格底部生成与表格内容同宽的表注，并且当注释内容过长时可以实现自动换行，相比于其它方式更协调一致。

具体是在tabular环境外嵌套一层`threeparttable`环境，并在`tabular`环境之后将表注内容添加在`tablenotes`环境中，由此得到的表注将会显示在表格底部。如果需要将表格内容与表注建立关联关系，可以在表格内容的相应位置使用`\tnote{索引标记}`添加表注的索引标记，并且在`tablenotes`环境中使用`item[索引标记]`命令创建这项表注。


【**例3**】使用threeparttable宏包添加表注。

```tex
\documentclass[12pt]{article}

\usepackage{booktabs}
\usepackage{threeparttable}

\begin{document}

\begin{table}
    \centering
    \begin{threeparttable}
        	\begin{tabular}{|c|c|c|c|}
    		\hline
    		Column1\tnote{*} & Column2 & Column3 & Column4\\
    		\hline
    		A1^{2} & A2 & A3 & A4\\
    		\hline
    		B1^{3} & B2 & B3 & B4\\
    		\hline
    		C1 & C2 & C3 & C4\\
    		\hline
    \end{tabular}
        \begin{tablenotes}
            \footnotesize
            \item[1] This is a remark example.
            \item[2] This is another remark example and with a very long content, but the contents will be wrapped.
            \item[*] This is 1.
        \end{tablenotes}
    \end{threeparttable}
\end{table}

\end{document}
```
编译上述代码，得到表格如图5-2-3所示。

<p align="center">
<img align="middle" src="latex/chapter-5/graphics/newexm5_2_3.png" width="350" />
</p>

<center><b>图5-2-3</b> 编译后的文档内容</center>

### 5.2.3 插入各类斜线

有时候，在论文写作过程中，需要在第一个单元格内声明表格行列所表示的内容分别是什么，因此要用到斜线。在LaTeX中，我们可以通过调用`diagbox`宏包及其提供的`\diagbox[参数]{单元格内容1}…{单元格内容n}`命令将一个单元格划分为n个部分（即插入(n-1)条斜线），并且可以在[]中设置不同参数，从而对斜线宽度、高度、方向等属性进行调整，主要包括：

- width：设置斜线宽度；
- height：设置斜线高度；
- font：设置单元格字体大小和字体类型；
- linewidth：设置线宽；
- linecolor：设置线的颜色（需结合xcolor或其他宏包使用）；
- dir：设置斜线方向，包括NW（默认）、NE、SW和SE，分别表示西北方向、东北方向、西南方向、东南方向。当仅插入一个斜线时，dir=NW与dir=SE、dir=NE与dir=SW效果相同，分别表示插入反斜线和斜线。

【**例4**】使用\usepackage{diagbox}宏包中的\diagbox命令在表格中插入斜线。

```tex
\documentclass[12pt]{article}

\usepackage{booktabs}
\usepackage{diagbox} 

\begin{document}

Table~\ref{table1} shows the Example of ABC.

\begin{table}[h]
    \centering
    \caption{Example of ABC}
     	\begin{tabular}{|c|c|c|c|}
    		\hline
    		\diagbox[width=5em]{$A$}{$B$} & Column2 & Column3 & Column4\\
    		\hline
    		A1^{2} & A2 & A3 & A4\\
    		\hline
    		B1^{3} & B2 & B3 & B4\\
    		\hline
    		C1 & C2 & C3 & C4\\
    		\hline
    		\end{tabular}
    \label{table1}
\end{table}

\end{document}
```
编译上述代码，得到表格如图5-2-4所示。

<p align="center">
<img align="middle" src="latex/chapter-5/graphics/newexm5_2_4.png" width="350" />
</p>

<center><b>图5-2-4</b> 编译后的文档内容</center>

当然，有时也需要在第一个单元格插入两条斜线来声明表格内容，同样可以使用\usepackage{diagbox}宏包来插入。当插入两个斜线时， \diagbox[设置dir参数]{A}{B}{C}，使用NW、NE、SW和SE的效果分别如图5-2-5所示：

<p align="center">
<img align="middle" src="latex/chapter-5/graphics/newexm5_2_5.png" width="350" />
</p>

<center><b>图5-2-5</b> 编译后的文档内容</center>

【**例5**】使用\usepackage{diagbox}宏包中的\diagbox命令在表格中插入斜线。

```tex
\documentclass[12pt]{article}

\usepackage{booktabs}
\usepackage{diagbox} 

\begin{document}

Table~\ref{table1} shows the the Example of ABC.

\begin{table}[h]
    \centering
    \caption{Example of ABC}
   		\begin{tabular}{|c|c|c|c|}
    		\hline
    		\diagbox[width=5em]{$A$}{$B$}{$C$} & Column2 & Column3 & Column4\\
    		\hline
    		A1^{2} & A2 & A3 & A4\\
    		\hline
    		B1^{3} & B2 & B3 & B4\\
    		\hline
    		C1 & C2 & C3 & C4\\
    		\hline
    		\end{tabular}
    \label{table1}
\end{table}

\end{document}
```

编译上述代码，得到表格如图5-2-6所示。

<p align="center">
<img align="middle" src="latex/chapter-5/graphics/newexm5_2_6.png" width="350" />
</p>

<center><b>图5-2-6</b> 编译后的文档内容</center>

### 5.2.4 文本对齐换行

#### 自动对齐换行

使用列类型参数l、c或r可以对每列的单元格设置左对齐、横向居中对齐和右对齐，但由此创建的单元格不仅无法设置顶部对齐、纵向居中对齐、以及底部对齐方式，而且单元格内容不论长短都被拉长为一行，显得不够灵活。下面介绍几种方式用于实现单元格自动对齐与换行。

##### 使用array宏包实现单元格自动对齐与换行

首先在导言区使用`\usepackage{array}`语句声明调用array宏包，该宏包提供了以下6个列类型参数分别对应不同的对齐方式：

- `p{列宽}`：单元格内容将根据设置的列宽自动换行，并且对齐方式为顶部对齐；
- `m{列宽}`：单元格内容将根据设置的列宽自动换行，并且对齐方式为纵向居中对齐；
- `b{列宽}`：单元格内容将根据设置的列宽自动换行，并且对齐方式为底部对齐；
- `>{\raggedright\arraybackslash}`：将一列的单元格内容设置为左对齐；
- `>{\centering\arraybackslash}`：将一列的单元格内容设置为横向居中对齐；
- `>{\raggedleft\arraybackslash}`：将一列的单元格内容设置为右对齐。

默认情况下，如果单独使用p、m或b参数，默认为左对齐。我们可以对上述参数进行组合使用，从而获得不同的对齐效果。需要注意的是，此时应使用`\tabularnewline`取代`\\`符号作为表格一行的结束。

【**例6**】调用`array`宏包及其提供的列类型参数实现单元格自动对齐与分行。
```tex
\documentclass[12pt]{article}

\usepackage{array}

\begin{document}

\begin{table}[h]
\centering
    \caption{Title of a table.}
    \label{first label}
    \begin{tabular}{|>{\raggedright\arraybackslash}m{2.3cm}|>{\centering\arraybackslash}m{2.3cm}|>{\centering}m{2.3cm}|>{\raggedleft\arraybackslash}m{2.3cm}|}
        \hline
        Column1 & Column2 Column2 & Column3 Column3 Column3 & Column4 Column4 Column4 Column4 \tabularnewline
        \hline
        Value1 & Value2 Value2 & Value3 Value3 Value3 & Value4 Value4 Value4 Value4 \tabularnewline
        \hline
        Value1 & Value2 Value2 & Value3 Value3 Value3 & Value4 Value4 Value4 Value4 \tabularnewline
        \hline
    \end{tabular}
\end{table}

\end{document}
```

编译上述代码，得到表格如图5-2-7所示。

<p align="center">
<img align="middle" src="latex/chapter-5/graphics/newexm5_2_7.png" width="350" />
</p>

<center><b>图5-2-7</b> 编译后的文档内容</center>

##### 使用tabularx宏包实现自动换行

首先在导言区声明调用`tabularx`宏包，然后使用`\begin{tabularx} \end{tabularx}`环境取代`\begin{tabular} \end{tabular}`环境创建表格内容，`tabularx`环境的使用方式与`tabular`类似，不同之处主要在于：`\begin{tabularx}{表格宽度}{列类型}`中应设置表格宽度；在`tabularx`环境中，对于需要自动换行的列，其列类型应设置为大写的X。X参数可以与`>{\raggedright\arraybackslash}、>{\centering\arraybackslash}或>{\raggedleft\arraybackslash}`进行组合使用，从而修改单元格的对齐方式。


【**例7**】调用tabularx宏包并设置列类型参数X从而实现单元格内容自动换行。

```tex
\documentclass[12pt]{article}

\usepackage{array}
\usepackage{tabularx} % 调用tabularx宏包

\begin{document}

\begin{table}[h]
\centering
    \caption{Title of a table.}
    \label{first label}
    \begin{tabularx}{\linewidth}{|X|X|X|>{\centering\arraybackslash}X|} % 将需要自动换行的列的列类型参数设为X
        \hline
        Column1 & Column2 & Column3 & Column4 \\
        \hline
        This is Value1. This is Value1. & This is Value2. This is Value2. & This is Value3. This is Value3. & This is Value4. This is Value4. \\
        \hline
        This is Value1. This is Value1. This is Value1. & This is Value2. This is Value2. This is Value2. & This is Value3. This is Value3. This is Value3. & This is Value4. This is Value4. This is Value4. \\
        \hline
    \end{tabularx}
\end{table}

\end{document}
```
编译上述代码，得到表格如图5-2-8所示。

<p align="center">
<img align="middle" src="latex/chapter-5/graphics/newexm5_2_8.png" width="350" />
</p>

<center><b>图5-2-8</b> 编译后的文档内容</center>

##### 使用tabulary宏包实现自动换行

类似地，调用`tabulary`宏包并使用`\begin{tabulary}{表格宽度}{列类型} \end{tabulary}`环境创建表格。对于需要自动换行的列，只需将列类型改为大写字母即可，即，大写L表示左对齐并自动换行、大写C表示居中对齐并自动换行、大写R表示右对齐并自动换行。

【**例8**】调用tabulary宏包并设置大写列类型参数（L、C和R）从而实现单元格内容自动换行。

```tex
\documentclass[12pt]{article}

\usepackage{array}
\usepackage{tabulary} % 调用tabulary宏包

\begin{document}

\begin{table}[h]
\centering
    \caption{Title of a table.}
    \label{first label}
    \begin{tabulary}{\linewidth}{|L|C|C|R|} % 将需要自动换行的列的列类型参数改为大写
        \hline
        Column1 & Column2 & Column3 & Column4 \\
        \hline
        This is Value1. This is Value1. & This is Value2. This is Value2. & This is Value3. This is Value3. & This is Value4. This is Value4. \\
        \hline
        This is Value1. This is Value1. This is Value1. & This is Value2. This is Value2. This is Value2. & This is Value3. This is Value3. This is Value3. & This is Value4. This is Value4. This is Value4. \\
        \hline
    \end{tabulary}
\end{table}

\end{document}
```
编译上述代码，得到表格如图5-2-9所示。

<p align="center">
<img align="middle" src="latex/chapter-5/graphics/newexm5_2_9.png" width="350" />
</p>

<center><b>图5-2-9</b> 编译后的文档内容</center>

#### 人工强制换行

有时候我们需要自己手动指定换行符，而不是依靠p来实现自动换行。在这种情况下，可以使用命令 `\parbox`来完成：

【**例9**】用`\parbox`命令来实现单元格中文本指定换行。

```tex
\documentclass{article}

\begin{document}

\begin{center}    
    \begin{tabular}{|c|c|c|c|}
        \hline
        a & b & c & d \\ 
        \hline
        a & b & c & \parbox[t]{5cm}{In probability theory and statistics, the continuous uniform distribution\\ or rectangular distribution is a family of symmetric probability distributions.} \\ 
        \hline
    \end{tabular} 
\end{center}

\end{document}
```

编译上述代码，得到表格如图5-2-10所示。

<p align="center">
<img align="middle" src="latex/chapter-5/graphics/newexm5_2_10.png" width="350" />
</p>

<center><b>图5-2-10</b> 编译后的文档内容</center>

### 5.2.5 数字位数对齐

为了更好地描述数据，在表格中常常将数据在小数点处进行对齐，在LaTeX中我们可以通过使用`dcolumn`包实现这一目的。这个包提供了一个名为`D`的列类型，可以方便实现基于小数点的数字对齐以及基于其它符号的对齐，使用方式为`D{输入符号}{输出符号}{符号后的数字位数}`。对于基于小数点的数字对齐，输入符号一般为“.”；有时需要根据特定符号进行数字对齐，比如千分位逗号，这时输入符号即为“,”。例如，`D{.}{\cdot}{2}`表示将某列的数据根据“.”符号对齐，输出时将该符号显示为点乘符号，并且显示2个小数位数。

列类型D可以像其它列类型一样在表格环境的开始命令处直接进行设置，但会导致语句过长，所以一般使用`array`宏包的`\newcolumntype`命令定义一个新的列类型，并为这个列类型赋予一个比较短的名称以方便调用。定义新的列类型的语句为`\newcolumntype{新列类型名称}[新列类型的参数个数]{定义新列类型}`，例如：`\newcolumntype{d}[1]{D{.}{\cdot}{#1}}`表示创建一个名为d的新列类型，该列类型的内容为`D{.}{\cdot}{符号后的数字位数}`，其中数字位数是传给d的参数。

【**例10**】用`dcolumn`包来实现单元格中文本指定换行。

```tex
\documentclass[12pt]{article}

\usepackage{dcolumn}

\newcolumntype{d}[1]{D{.}{\cdot}{#1} }

\begin{document}

    \begin{tabular}{|l |r |c |d{1}| }
        \hline
        Left&Right&Center&\mathrm{Decimal}\\
        \hline
        1&2&3&4\\
        \hline
        11&22&33&44\\
        \hline
        1.1&2.2&3.3&4.4\\
        \hline
    \end{tabular}
    
\end{document}
```
编译上述代码，得到表格如图5-2-11所示。

<p align="center">
<img align="middle" src="latex/chapter-5/graphics/newexm5_2_11.png" width="350" />
</p>

<center><b>图5-2-11</b> 编译后的文档内容</center>

【回放】[**5.1 基本介绍**](https://nbviewer.jupyter.org/github/xinychen/latex-cookbook/blob/main/chapter-5/new_section1.ipynb)

【继续】[**5.3 调整表格样式**](https://nbviewer.jupyter.org/github/xinychen/latex-cookbook/blob/main/chapter-5/new_section3.ipynb)