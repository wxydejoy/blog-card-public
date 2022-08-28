## 9.7 插入表格

在Beamer幻灯片中插入表格的规则与常规文档一致，可以使用`tabular`环境创建表格内容，或者在`tabular`环境外额外嵌套一层`table`环境以创建标题、索引标签等元素，当然对于合并单元格、创建三线表、创建彩色表格等操作也是类似的（详见本书第5章）。

【**例9-49**】在`beamer`文档类型中使用`table`环境和`tabular`环境制作一个简单表格。

```tex
\documentclass{beamer}

\begin{document}

\begin{frame}

The created table\ref{tab:table_a} is shown as follows.
\begin{table}[bt]
\caption{A table in Beamer}
\label{tab:table_a}
    \begin{tabular}{|l|c|c|} \hline
    \textbf{Code Structure} & \textbf{Component} & \textbf{Others} \\
    \hline
    preamble & figures & title \\
    body & tables & footline \\
    & equations & list \\
    & normal texts & block \\
    \hline
    \end{tabular}
\end{table}

\end{frame}

\end{document}
```

编译上述代码，得到幻灯片如图9.7.1所示。

<p align="center">
<img align="middle" src="docs/latex/chapter-9/graphics/eg1.png" width="450" />
</p>

<center><b>图9.7.1</b> 编译后的幻灯片效果</center>

在Beamer中，我们可以使用前面介绍的动画效果命令（如`\uncover{}`）为表格添加动画，让表格中的各单元格内容分步呈现。

【**例9-50**】在`beamer`文档类型中使用`\begin{table} \end{table}`环境制作一个简单表格，同时使用`\uncover{}`设置动画格式。

```tex
\documentclass{beamer}

\begin{document}

\begin{frame}

\begin{table}[bt]
\begin{tabular}{|l|c|c|} \hline
\textbf{Code Structure} & \textbf{Component} & \textbf{Others} \\
\hline
\uncover<1->{preamble} & \uncover<2->{figures} & \uncover<3->{title} \\
\uncover<1->{body} & \uncover<2->{tables} & \uncover<3->{footline} \\
& \uncover<2->{equations} & \uncover<3->{list} \\
& \uncover<2->{normal texts} & \uncover<3->{block} \\
\hline
\end{tabular}
\end{table}

\end{frame}

\end{document}
```

编译上述代码，得到幻灯片如图9.7.2所示。

<p align="center">
<table>
<tr>
<td><img align="middle" src="docs/latex/chapter-9/graphics/example14_1.png" width="450"></td>
<td><img align="middle" src="docs/latex/chapter-9/graphics/example14_2.png" width="450"></td>
</tr>
<tr>
<td><img align="middle" src="docs/latex/chapter-9/graphics/example14_3.png" width="450"></td>
</tr>
</table>
</p>

<center><b>图9.7.2</b> 编译后的幻灯片效果</center>


【回放】[**9.6 添加参考文献**](https://nbviewer.jupyter.org/github/xinychen/latex-cookbook/blob/main/chapter-9/section6.ipynb)

【继续】[**9.8 插入与调整图片**](https://nbviewer.jupyter.org/github/xinychen/latex-cookbook/blob/main/chapter-9/section8.ipynb)

### License

<div class="alert alert-block alert-danger">
<b>This work is released under the MIT license.</b>
</div>
