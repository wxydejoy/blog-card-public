## 5.3 调整表格样式

调整表格样式同样是表格制作中重要的部分。

### 5.3.1	调整表格宽高

#### 调整表格宽度

不同出版商对文章表格宽高的要求不一样，在上一节中，我们介绍了使用`array`宏包提供的列类型参数可以在设置单元格对齐方式的同时对列宽进行调整。此外，也可以在导言区使用`\setlength{\tabcolsep}{文本和列分隔线的间距}`命令修改表格列宽，默认情况下，单元格内容与列分隔线的间距为6pt。

【**例1**】使用`\setlength{\tabcolsep}{12pt}`命令将表格单元格文本和列分隔线的间距设为12pt。

```tex
\documentclass[12pt]{article}

\setlength{\tabcolsep}{12pt}

\begin{document}
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

\end{document}
```

编译上述代码，得到表格如图5-3-1所示。

<p align="center">
<img align="middle" src="latex/chapter-5/graphics/newexm5_3_1.png" width="350" />
</p>

<center><b>图5-3-1</b> 编译后的文档内容</center>

在LaTeX中，对于宽度设置，可使用`tabularx`宏包整体调整表格的宽度，也可以在`\begin{tabularx}`命令后的参数设置中，设置每一列的宽度。

【**例2**】使用tabularx宏包调整表格宽度。

```tex
\documentclass[12pt]{article}

\usepackage{tabularx} 

\begin{document}

\begin{table}
    \centering
    \begin{tabularx}{\textwidth}{|p{3cm}|p{3cm}|p{3cm}|p{3cm}|}
    \hline
    Column1 & Column2 & Column3 & Column4\\
    \hline
    A1 & A2 & A3 & A4\\
    \hline
    B1 & B2 & B3 & B4\\
    \hline
    C1 & C2 & C3 & C4\\
    \hline
    \end{tabularx}
    \label{table1}
\end{table}

\end{document}
```
编译上述代码，得到表格如图5-3-2所示。

<p align="center">
<img align="middle" src="latex/chapter-5/graphics/newexm5_3_2.png" width="350" />
</p>

<center><b>图5-3-2</b> 编译后的文档内容</center>

#### 调整表格高度

如果需要调整表格整体行高，可以在导言区使用\renewcommand{\arraystretch}{行高倍数}命令，从而根据设置的行高倍数在默认值的基础上对行高进行扩大或缩小。

【例3】使用array宏包中的\renewcommand\arraystretch{2}命令整体调整行高为两倍行距。

```tex
\documentclass[12pt]{article}

\renewcommand{\arraystretch}{2}

\begin{document}

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

\end{document}
```

编译上述代码，得到表格如图5-3-3所示。

<p align="center">
<img align="middle" src="latex/chapter-5/graphics/newexm5_3_3.png" width="350" />
</p>

<center><b>图5-3-3</b> 编译后的文档内容</center>


在LaTeX中，也可以使用`\rule{}{}`命令调整每行行高。

【例4】使用`\rule{}{}`命令调整第二行行高。

```tex
\documentclass[12pt]{article}

\usepackage{tabularx} 

\begin{document}

\begin{table}
    \centering
    \begin{tabularx}{\textwidth}{|p{3cm}|p{3cm}|p{3cm}|p{3cm}|}
    \hline
    Column1 & Column2 & Column3 & Column4\\
    \rule{0pt}{30pt}
\hline
    A1 & A2 & A3 & A4\\
    \hline
    B1 & B2 & B3 & B4\\
    \hline
    C1 & C2 & C3 & C4\\
    \hline
    \end{tabularx}
    \label{table1}
\end{table}

\end{document}
```
编译上述代码，得到表格如图5-3-4所示。

<p align="center">
<img align="middle" src="latex/chapter-5/graphics/newexm5_3_4.png" width="350" />
</p>

<center><b>图5-3-4</b> 编译后的文档内容</center>



### 5.3.2 表格行列合并

合并行列是表格中重要的格式调整内容，如果需要合并单元格，合并同行不同列时，使用`\multicolumn`命令；合并同列不同行时，首先应在导言区声明`\usepackage{multirow}`以导入`multirow`宏包，并使用`\multirow`命令；合并多行多列需要`\multicolumn`命令和`\multirow`命令组合使用。

#### 合并不同列的单元格

合并不同列的单元格时，应在`tabular`环境中使用`\multicolumn{合并列数}{合并后的列类型参数}{单元格内容}`语句定义合并单元格。此时，合并后的单元格的列类型将由`multicolumn`给出，而非`\begin{tabular}`中预设的列类型参数。

【**例5**】在`tabular`环境中使用`\multicolumn`命令合并不同列的单元格。

```tex
\documentclass[12pt]{article}


\begin{document}

\begin{tabular}{|l|l|l|l|}
    \hline
    Column1 & Column2 & Column3 & Column4 \\
    \hline
    \multicolumn{2}{|c|}{A1 and A2} & A3 & A4 \\
    \hline
    B1 & B2 & B3 & B4 \\
    \hline
    C1 & C2 & C3 & C4 \\
    \hline
\end{tabular}

\end{document}
```

编译上述代码，得到表格如图5-3-5所示。


<p align="center">
<img align="middle" src="latex/chapter-5/graphics/newexm5_3_5.png" width="350" />
</p>

<center><b>图5-3-5</b> 编译后的文档内容</center>

#### 合并不同行的单元格

合并不同行的单元格时使用的语句为`\multirow{合并行数}{合并后的宽度}{单元格内容}`。如果把`{合并后的宽度}`参数设置为`{*}`，那么LaTeX会根据文本内容自动设置单元格宽度。在绘制行分隔线时，使用`\hline`命令会创建一条横跨表格左右两端的横线，显然不适用于合并单元格后的行。此时应用`\cline{起始列号-终止列号}`命令，通过指定行分隔线的起始列和终止列，从而定制跨越了部分列的行分隔线。

【**例6**】在`tabular`环境中使用`\multirow`命令合并不同列的单元格，并使用`\cline`命令定制行分隔线的起始点。

```tex
\documentclass[12pt]{article}

\usepackage{multirow}
\begin{document}

\begin{tabular}{|l|l|l|l|}
    \hline
    Column1 & Column2 & Column3 & Column4 \\
    \hline
    \multirow{2}{*}{A1 and B1} & A2 & A3 & A4 \\
    \cline{2-4} % 创建一条从第2列到第4列的行分隔线
    & B2 & B3 & B4 \\
    \hline
    C1 & C2 & C3 & C4 \\
    \hline
\end{tabular}

\end{document}
```
编译上述代码，得到表格如图5-3-6所示。


<p align="center">
<img align="middle" src="latex/chapter-5/graphics/newexm5_3_6.png" width="350" />
</p>

<center><b>图5-3-6</b> 编译后的文档内容</center>

从上例可以看出，合并多行的单元格时，除了第一个单元格处使用\multirow命令定义单元格，其余被合并的单元格处均留空。

#### 合并多行多列的单元格

通过嵌套使用`\multicolumn`和`\multirow`命令可以实现对多行多列单元格的合并操作，具体语句为`\multicolumn{合并列数}{合并后的列类型参数}{\multirow{合并行数}{合并后的宽度}{单元格内容}}`。

【**例7**】在`tabular`环境中嵌套使用`\multicolumn`和`\multirow`命令合并多行多列的单元格。

```tex
\documentclass[12pt]{article}

\usepackage{multirow}

\begin{document}

\begin{tabular}{|l|l|l|l|}
    \hline
    Column1 & Column2 & Column3 & Column4 \\
    \hline
    \multicolumn{2}{|c|}{\multirow{2}{*}{A1, A2, B1 and B2}} & A3 & A4 \\ % 合并多行多列的单元格
    \cline{3-4} % 创建一条从第3列到第4列的行分隔线
    \multicolumn{2}{|c|}{} & B3 & B4 \\
    \hline
    C1 & C2 & C3 & C4 \\
    \hline
\end{tabular}

\end{document}
```

编译上述代码，得到表格如图5-3-7所示。

<p align="center">
<img align="middle" src="latex/chapter-5/graphics/newexm5_3_7.png" width="350" />
</p>

<center><b>图5-3-7</b> 编译后的文档内容</center>

从上例可以看出，在同时合并涉及多行多列的单元格时，除了第一行使用`\multicolumn`和`\multirow`嵌套命令定义单元格，其余被合并的行处均使用内容为空的`\multicolumn`命令。


### 5.3.3 插入彩色表格

有时，根据表达需要，表格中的内容需要突出显示，彩色表格即为突出显示的一种重要方式。通过对表格的单元格、行或列填充颜色，可以创建不同的彩色表格。为此，首先应在导言区使用`\usepackage[table]{xcolor}`声明语句，通过调用`xcolor`宏包提供的相关命令可以实现颜色填充。填充单元格时，使用`\cellcolor{单元格填充颜色}`单元格内容命令定义单元格内容即可。

【**例8**】在导言区使用`\usepackage[table]{xcolor}`命令调用设置了`table`选项的`xcolor`宏包，并使用`\cellcolor`命令定义具有颜色填充效果的单元格。

```tex
\documentclass[12pt]{article}

\usepackage[table]{xcolor} % 调用设置了table选项的xcolor宏包

\begin{document}

\begin{tabular}{|l|l|l|l|}
    \hline
    Column1 & Column2 & Column3 & Column4\\
    \hline
    \cellcolor{red!80}A1 & A2 & A3 & A4\\ % 使用\cellcolor命令设置单元格填充颜色
    \hline
    \cellcolor{red!50}B1 & B2 & B3 & B4\\
    \hline
    \cellcolor{red!20}C1 & C2 & C3 & C4\\
    \hline
\end{tabular}

\end{document}
```
编译上述代码，得到表格如图5-3-8所示。

<p align="center">
<img align="middle" src="latex/chapter-5/graphics/newexm5_3_8.png" width="350" />
</p>

<center><b>图5-3-8</b> 编译后的文档内容</center>

为了达到更好的可视化效果，有时候需要为表格的奇数行和偶数行交替设置不同的填充颜色，那么只需要在tabular环境前使用\rowcolors{开始填充的行编号}{第一个行填充颜色}{第二个行填充颜色}命令即可：

```tex
\documentclass[12pt]{article}

\usepackage[table]{xcolor} % 调用设置了table选项的xcolor宏包

\begin{document}

\rowcolors{2}{red!50}{red!20} % 设置表格交替填充行颜色

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

\end{document}
```
编译上述代码，得到表格如图5-3-9所示。

<p align="center">
<img align="middle" src="latex/chapter-5/graphics/newexm5_3_9.png" width="350" />
</p>

<center><b>图5-3-9</b> 编译后的文档内容</center>

当然，我们也可以设置列填充颜色，只需要在列类型参数中加上>{\columncolor{列填充颜色}}即可：

```tex
\documentclass[12pt]{article}

\usepackage[table]{xcolor} % 调用设置了table选项的xcolor宏包

\begin{document}

\begin{tabular}{|>{\columncolor{red!50}}l|>{\columncolor{red!20}}l|>{\columncolor{red!50}}l|>{\columncolor{red!20}}l|} % 设置列填充颜色
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
编译上述代码，得到表格如图5-3-10所示。

<p align="center">
<img align="middle" src="latex/chapter-5/graphics/newexm5_3_10.png" width="350" />
</p>

<center><b>图5-3-10</b> 编译后的文档内容</center>


### 5.3.4 修改表格线型

#### 线宽全局设置

通过在导言区使用`\setlength{\arrayrulewidth}{线宽}`命令，可以修改表格线宽，默认为0.4pt。然而当线宽设置过大时，可能导致表格线交叉处不连续的情况。对此，在导言区调用`xcolor`宏包、并设置`table`选项可以解决。

【**例9**】在导言区使用`\usepackage[table]{xcolor}`命令调用设置了`table`选项的`xcolor`宏包，并使用`\setlength{\arrayrulewidth}{线宽}`命令设置表格线宽。

```tex
\documentclass[12pt]{article}

\usepackage[table]{xcolor} % 调用设置了table选项的xcolor宏包
\setlength{\arrayrulewidth}{2pt} % 修改表格线宽

\begin{document}

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

\end{document}
```
编译上述代码，得到表格如图5-3-11所示。
 
<p align="center">
<img align="middle" src="latex/chapter-5/graphics/newexm5_3_11.png" width="350" />
</p>

<center><b>图5-3-11</b> 编译后的文档内容</center>

#### 创建三线表格

在表格制作中，关于水平线，最常用的是`\hline`，这是可以画出最常用的默认粗细的分割线。实际上，我们有时候会用到不同粗细的分割线，比如三线表格：`booktabs`宏包提供了更美观的行分隔线创建命令，常用于创建三线表格。其中，`\toprule`命令常用于创建表格顶线、`\bottomrule`命令常用于创建表格底线、`\midrule`命令常用于创建表格标题栏和表格内容的分隔线、以及`\cmidrule{起始列号-终止列号}`命令用于创建标题栏内部的分隔线并设置分隔线的跨越范围。
(https://tex.stackexchange.com/questions/156122/booktabs-what-is-the-difference-between-toprule-and-hline)

【**例10**】调用`booktabs`宏包及其相关命令创建三线表。

```tex
\documentclass[12pt]{article}

\usepackage{booktabs}

\begin{document}

\begin{tabular}{cccc}
    \toprule
    \multicolumn{2}{c}{\textbf{Type1}} & \\
    \cmidrule{1-2}
    Column1 & Column2 & Column3 & Column4\\
    \midrule
    A1 & A2 & A3 & A4\\
    B1 & B2 & B3 & B4\\
    C1 & C2 & C3 & C4\\
    \bottomrule
\end{tabular}

\end{document}
```

编译上述代码，得到表格如图5-3-12所示。
 
<p align="center">
<img align="middle" src="latex/chapter-5/graphics/newexm5_3_12.png" width="350" />
</p>

<center><b>图5-3-12</b> 编译后的文档内容</center>


### 表格位置设置

表格在制作好后，最后需要对表格的位置进行设置。调整表格的位置与后面调整图片的位置具有着相似的方法。对于表格的位置调整，这里主要介绍`tabular`, `table` 和 `wraptable`三种环境完成设置。其中`tabular`环境的默认位置方式是左对齐；而`table`环境可以通过设置自动调整表格的位置，可以让表格自己出现在文档合适的地方；而`wraptable`环境可以让表格的周围环绕文字，从而避免表格两旁的空白空间浪费。

【**例11**】在环境`tabular`默认情况下对文本插入表格。

```tex
\documentclass[12pt]{article}

\usepackage{xcolor}
\usepackage{colortbl,booktabs} 

\begin{document}

In descriptive statistics, a box plot or boxplot is a method for graphically depicting groups of numerical data through their quartiles. Box plots may also have lines extending from the boxes (whiskers) indicating variability outside the upper and lower quartiles, hence the terms box-and-whisker plot and box-and-whisker diagram. Outliers may be plotted as individual points. 
Box plots are non-parametric: they display variation in samples of a statistical population without making any assumptions of the underlying statistical distribution (though Tukey's boxplot assumes symmetry for the whiskers and normality for their length).

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

The spacings between the different parts of the box indicate the degree of dispersion (spread) and skewness in the data, and show outliers. 
In addition to the points themselves, they allow one to visually estimate various L-estimators, notably the interquartile range, midhinge, range, mid-range, and trimean. Box plots can be drawn either horizontally or vertically. Box plots received their name from the box in the middle, and from the plot that they are.

\end{document}
```

编译上述代码，得到表格如图5-3-13<所示。

<p align="center">
<img align="middle" src="latex/chapter-5/graphics/newexm5_3_13.png" width="350" />
</p>

<center><b>图5-3-13</b> 编译后的文档内容</center>


使用环境`table`可以方便的对表格的位置进行调整，是通过命令`\begin{table}[]`对中括号中的参数进行设置。其中参数的选择包括： `h` 是将浮动元素的位置设定为 `here`（这里），一般位于其在文档中出现的位置； `t` 是将浮动元素的位置设定为页面的上方`（top）`； `b` 是将浮动元素的位置设定为页面的底部`（bottom）`； `p `是将浮动元素仅放置在一个特殊的页面； `!` 是可以重新设置LaTeX的一个内部参数； `H` 是将浮动元素精确地放置在它在文本中所出现的位置。

【**例12**】在环境`table`下将表格设置于页面上方。

```tex
\documentclass[12pt]{article}

\usepackage{xcolor}
\usepackage{colortbl,booktabs}

\begin{document}

In descriptive statistics, a box plot or boxplot is a method for graphically depicting groups of numerical data through their quartiles. Box plots may also have lines extending from the boxes (whiskers) indicating variability outside the upper and lower quartiles, hence the terms box-and-whisker plot and box-and-whisker diagram. Outliers may be plotted as individual points. Box plots are non-parametric: they display variation in samples of a statistical population without making any assumptions of the underlying statistical distribution (though Tukey's boxplot assumes symmetry for the whiskers and normality for their length).

\begin{table}[t]
\centering
\begin{tabular}{lcccc}
    \hline
     & $x=1$ & $x=2$ & $x=3$ & $x=4$ \\
    \hline
    $y=x$ &\multicolumn{1}{c}{1}  & 2 & 3 & 4 \\
    $y=x^{2}$ & 1 & \multicolumn{1}{c}{4} & 9 & 16 \\
    $y=x^{3}$ & 1 & 8 & \multicolumn{1}{c}{27} & 64 \\
    \hline
\end{tabular}
\end{table}

The spacings between the different parts of the box indicate the degree of dispersion (spread) and skewness in the data, and show outliers. In addition to the points themselves, they allow one to visually estimate various L-estimators, notably the interquartile range, midhinge, range, mid-range, and trimean. Box plots can be drawn either horizontally or vertically. Box plots received their name from the box in the middle, and from the plot that they are.

\end{document}
```
编译上述代码，得到表格如图5-3-14所示。
 
<p align="center">
<img align="middle" src="latex/chapter-5/graphics/newexm5_3_14.png" width="350" />
</p>

<center><b>图5-3-14</b> 编译后的文档内容</center>

【**例13**】在环境`table`下将表格自动设置为`here`，并且空间不够时在上方。

```tex
\documentclass[12pt]{article}

\usepackage{xcolor}
\usepackage{colortbl,booktabs} 

\begin{document}

In descriptive statistics, a box plot or boxplot is a method for graphically depicting groups of numerical data through their quartiles. Box plots may also have lines extending from the boxes (whiskers) indicating variability outside the upper and lower quartiles, hence the terms box-and-whisker plot and box-and-whisker diagram. Outliers may be plotted as individual points. Box plots are non-parametric: they display variation in samples of a statistical population without making any assumptions of the underlying statistical distribution (though Tukey's boxplot assumes symmetry for the whiskers and normality for their length).

\begin{table}[ht]
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

The spacings between the different parts of the box indicate the degree of dispersion (spread) and skewness in the data, and show outliers. In addition to the points themselves, they allow one to visually estimate various L-estimators, notably the interquartile range, midhinge, range, mid-range, and trimean. Box plots can be drawn either horizontally or vertically. Box plots received their name from the box in the middle, and from the plot that they are.

\end{document}
```

编译上述代码，得到表格如图5-3-15所示。
    
<p align="center">
<img align="middle" src="latex/chapter-5/graphics/newexm5_3_15.png" width="350" />
</p>

<center><b>图5-3-15</b> 编译后的文档内容</center>

当表格的两边有大量空白时，为了避免空间浪费，可以使用wrapfig包来实现表格周围环绕文字的位置设定。

【**例14**】环境`wraptable`下将表格设置为周围环绕文字，图和文字距离为8cm。

```tex
\documentclass[12pt]{article}
\usepackage{xcolor}
\usepackage{colortbl,booktabs}
\usepackage{wrapfig}
\begin{document}
In descriptive statistics, a box plot or boxplot is a method for graphically depicting groups of numerical data through their quartiles. Box plots may also have lines extending from the boxes (whiskers) indicating variability outside the upper and lower quartiles, hence the terms box-and-whisker plot and box-and-whisker diagram. Outliers may be plotted as individual points. Box plots are non-parametric: they display variation in samples of a statistical population without making any assumptions of the underlying statistical distribution (though Tukey's boxplot assumes symmetry for the whiskers and normality for their length).

\begin{wraptable}{r}{8cm}
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
\end{wraptable}

The spacings between the different parts of the box indicate the degree of dispersion (spread) and skewness in the data, and show outliers. In addition to the points themselves, they allow one to visually estimate various L-estimators, notably the interquartile range, midhinge, range, mid-range, and trimean. Box plots can be drawn either horizontally or vertically. Box plots received their name from the box in the middle, and from the plot that they are.
\end{document}
```
编译上述代码，得到表格如图5-3-16所示。

<p align="center">
<img align="middle" src="latex/chapter-5/graphics/newexm5_3_16.png" width="350" />
</p>

<center><b>图5-3-16</b> 编译后的文档内容</center>

### 其他样式调整

#### 创建跨页表格

当表格太长时，使用tabular环境创建的表格会被裁剪掉页面放不下的部分。如果想让表格在行数太多时实现自动分页，可以通过调用longtable宏包并使用`longtable`环境创建表格。

在`longtable`环境中创建表格的方式与使用`table`和`tabular`嵌套环境类似，我们也能使用`\caption、\label`命令分别创建表格标题和索引标签。不同之处主要在于，`longtable`环境中可以设置跨页表格在每一页的重复表头和表尾，按照使用顺序，包括以下四个命令：

- `\endfirsthead`：`\begin{longtable}`和`\endfirsthead`之间的内容只会出现在表格第一页的表头部分；
- `\endhead`：`\endfirsthead`和`\endhead`之间的内容将会出现在表格除第一页之外的表头部分；
- `\endfoot`：`endhead`和`\endfoot`之间的内容将会出现在除表格最后一页之外的表尾部分；
- `\endlastfoot`：`\endfoot`和`\endlastfoot`之间的内容只会出现在表格最后一页的表尾部分。

以上四个命令需要放置在`longtable`环境的开始处。

【**例15**】调用`longtable`宏包及环境创建跨页表格。

```tex
\documentclass[12pt]{article}

\usepackage{longtable}

\begin{document}

\begin{longtable}[c]{cccc}
    % 创建表格第一页的表头部分
    \caption{Title of a table}\\
    \hline
    Column1 & Column2 & Column3 & Column4\\
    \hline
    \endfirsthead
    % 创建表格除第一页之外的表头部分
    \caption{Title of a table - Continued}\\
    \hline
    Column1 & Column2 & Column3 & Column4\\
    \hline
    \endhead
    % 创建表格除最后一页之外的表尾部分
    \hline
    \endfoot
    % 创建表格最后一页的表尾部分
    \multicolumn{4}{c}{\textbf{End of table.}}\\
    \hline
    \endlastfoot
    % 表格内容
    A1 & A2 & A3 & A4\\
    B1 & B2 & B3 & B4\\
    C1 & C2 & C3 & C4\\
    A1 & A2 & A3 & A4\\
    B1 & B2 & B3 & B4\\
    C1 & C2 & C3 & C4\\
    ... % 省略中间部分
    A1 & A2 & A3 & A4\\
    B1 & B2 & B3 & B4\\
    C1 & C2 & C3 & C4\\
    \hline
\end{longtable}

\end{document}
```

编译上述代码，得到表格如图5-3-17所示，其中左图和右图分别为表格第一页的部分内容以及第二页的所有内容。
 	 
<p align="center">
<table>
<tr>
<td><img align="middle" src="latex/chapter-5/graphics/newexm5_3_16_1.png" width="300"></td>
<td><img align="middle" src="latex/chapter-5/graphics/newexm5_3_16_2.png" width="300"></td>
</tr>
</table>
</p>

<center><b>图5-3-17</b> 编译后的文档</center>

#### 旋转表格方向

当表格列数太多时，横向表格的展现效果较差，这时需要将表格旋转90度，以纵向表格的形式展现。在LaTeX中可以通过调用`rotating`宏包，并使用`sidewaystable`环境取代`table`环境、嵌套`tabular`环境创建纵向表格（表格逆时针旋转90度）。

【例16】调用`rotating`宏包及`sidewaystable`环境创建纵向表格。

```tex
\documentclass[12pt]{article}

\usepackage{rotating}
\usepackage{booktabs}

\begin{document}

\begin{sidewaystable}[h]
\centering
    \caption{Title of a table.}
    \label{first label}
    \begin{tabular}{cccc}
        \toprule
        Column1 & Column2 & Column3 & Column4\\
        \midrule
        A1 & A2 & A3 & A4\\
        B1 & B2 & B3 & B4\\
        C1 & C2 & C3 & C4\\
        \bottomrule
    \end{tabular}
\end{sidewaystable}

\end{document}
```
编译上述代码，得到表格如图5-3-18所示。
 

<p align="center">
<img align="middle" src="latex/chapter-5/graphics/newexm5_3_17.png" width="200" />
</p>

<center><b>图5-3-17</b> 编译后的文档内容</center>

【回放】[**5.2 调整表格内容**](https://nbviewer.jupyter.org/github/xinychen/latex-cookbook/blob/main/chapter-5/new_section2.ipynb)

【继续】[**5.4 调整表格内容**](https://nbviewer.jupyter.org/github/xinychen/latex-cookbook/blob/main/chapter-5/new_section3.ipynb)