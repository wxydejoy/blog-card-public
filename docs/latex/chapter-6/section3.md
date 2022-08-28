## 6.3 插入图表目录

插入图目录或表目录的命令语句分别为`\listoffigures`和`\listoftables`，可以罗列`\caption`命令创建的图表标题名称，但对于使用`\caption*`命令创建的无编号的标题名称而言，则不会出现在目录中。

在一份专业文档中，目录总是和正文内容在不同页显示，为此可以使用`\newpage`命令进行分页；此外目录页中一般无页码编号，为此可以使用`\thispagestyle{empty}`取消当页页码设置，并在正文页之前使用`\pagenumbering{页码样式}`命令表示重新从1开始设置页码、同时设置页码样式。

默认的图目录名和表目录名分别是“List of Figures”、“List of Tables”，读者可以在导言区通过使用`\renewcommand{\listfigurename}{新图目录名}`命令修改图目录名、使用`\renewcommand{\listtablename}{新表目录名}`命令修改表目录名。

【**例6-2**】使用`\listoffigures`命令和`\listoftables`命令创建图目录和表目录，使用`\renewcommand`命令修改图目录名和表目录名，并使用`\newpage`、`\thispagestyle`和`\pagenumbering`命令对页码进行相应调整。

```tex
\documentclass{article}
\usepackage{graphicx}

\renewcommand{\listfigurename}{Figures}
\renewcommand{\listtablename}{Tables}

\begin{document}

\thispagestyle{empty} % 取消页码编号

\listoffigures
\listoftables

\newpage  % 插入新页
\pagenumbering{arabic}  % 设置页码样式为小写的阿拉伯数字

Here are three created tables...
\begin{table}[h!]
% ...
\caption{The first table.}
\caption{The second table.}
\caption{The third table.}
\end{table}

Here are three inserted figures...
\begin{figure}[h!]
% ...
\caption{The first figure.}
\caption*{The second figure.}
\caption{The third figure.}
% ...
\end{figure}

\end{document}
```

编译后的图表目录如图6.1.2所示。

<p align="center">
<img align="middle" src="docs/latex/chapter-6/graphics/eg_5NEW.png" width="450" />
</p>

<center><b>图6.1.2</b> 编译后的插图效果</center>


【回放】[**6.2 插入非浮动图片**](https://nbviewer.jupyter.org/github/xinychen/latex-cookbook/blob/main/chapter-6/section2.ipynb)

【继续】[**6.4 定制图表标题样式**](https://nbviewer.jupyter.org/github/xinychen/latex-cookbook/blob/main/chapter-6/section4.ipynb)

### License

<div class="alert alert-block alert-danger">
<b>This work is released under the MIT license.</b>
</div>
