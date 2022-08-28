## 8.3 BibTeX用法

LaTeX主要有两种管理参考文献的方法，第一种方法是在`.tex`文档中嵌入参考文献，参考文献格式需符合特定的文献引用格式；另一种方法则是使用 BibTeX进行文献管理，文件的拓展名为`.bib`。其中，使用外部文件BibTeX管理文献更加便捷高效。

### 8.3.1 创建参考文献

在LaTeX中，插入参考文献的一种直接方式是使用`thebibliography`环境，以列表的形式将参考文献进行整理起来，配以标签，以供正文引用，文档中引用的命令为`\cite{}`。

【**例8-8**】使用`thebibliography`环境在文档中插入参考文献并进行编译。

```tex
\documentclass[12pt]{article}

\begin{document}

Some examples for showing how to use \texttt{thebibliography} environment:
\begin{itemize}
    \item Book reference sample: The \LaTeX\ companion book \cite{latexcompanion}.
    \item Paper reference sample: On the electrodynamics of moving bodies \cite{einstein}.
    \item Open-source reference sample: Knuth: Computers and Typesetting \cite{knuthwebsite}.
\end{itemize}

\begin{thebibliography}{9}
\bibitem{latexcompanion} 
Michel Goossens, Frank Mittelbach, and Alexander Samarin. 
\textit{The \LaTeX\ Companion}. 
Addison-Wesley, Reading, Massachusetts, 1993.

\bibitem{einstein} 
Albert Einstein. 
\textit{Zur Elektrodynamik bewegter K{\"o}rper}. (German) 
[\textit{On the electrodynamics of moving bodies}]. 
Annalen der Physik, 322(10):891–921, 1905.

\bibitem{knuthwebsite} 
Knuth: Computers and Typesetting,
\\\texttt{http://www-cs-faculty.stanford.edu/\~{}uno/abcde.html}
\end{thebibliography}

\end{document}
```

编译上述代码，得到文档如图8.3.1所示。

<p align="center">
<img align="middle" src="docs/latex/chapter-8/graphics/example8_3_1.png" width="450" />
</p>

<center><b>图8.3.1</b> 编译后的文档</center>

【**例8-9**】使用`thebibliography`环境在文档中插入参考文献并进行编译。

```tex
\documentclass[12pt]{article}

\begin{document}

\LaTeX{} \cite{lamport94} is a set of macros built atop \TeX{} \cite{texbook}.

\begin{thebibliography}{9}
\bibitem{texbook}
Donald E. Knuth (1986) \emph{The \TeX{} Book}, Addison-Wesley Professional.

\bibitem{lamport94}
Leslie Lamport (1994) \emph{\LaTeX: a document preparation system}, Addison
Wesley, Massachusetts, 2nd ed.
\end{thebibliography}

\end{document}
```

编译上述代码，得到文档如图8.3.2所示。

<p align="center">
<img align="middle" src="docs/latex/chapter-8/graphics/example8_3_2.png" width="450" />
</p>

<center><b>图8.3.2</b> 编译后的文档</center>

> 参考[Creating and Managing Bibliographies with BibTeX on Overleaf](https://www.overleaf.com/blog/532-creating-and-managing-bibliographies-with-bibtex-on-overleaf)。



### 8.3.2 使用BibTeX文件

BibTeX是LaTeX最为常用的一个文献管理工具，它通常以一个独立的文件出现，其拓展名为`.bib`。它是伴随着LaTeX文档排版系统出现的，1985年兰伯特博士与其合作者开发了这一工具。作为一种特殊的且独立于LaTeX文件`.tex`之外的数据库，它能大大简化LaTeX文档中的文献引用。实际上，BibTeX文件中的文献都是用列表的形式罗列的，且不分先后顺序。通过使用引用命令如`\cite{}`即可在文档中自动生成特定格式的参考文献，其中，文档中的参考文献格式一般是提前设定好的。

【**例8-10**】使用Bibtex命令一个文献管理文件为`sample.bib`，将文献按照指定格式进行整理，插入参考文献并进行编译。

```tex
% 创建Bibtex文件，并将其命名为sample.bib

@article{einstein,
    author =       "Albert Einstein",
    title =        "{Zur Elektrodynamik bewegter K{\"o}rper}. ({German})
        [{On} the electrodynamics of moving bodies]",
    journal =      "Annalen der Physik",
    volume =       "322",
    number =       "10",
    pages =        "891--921",
    year =         "1905",
    DOI =          "http://dx.doi.org/10.1002/andp.19053221004"
}

@book{latexcompanion,
    author    = "Michel Goossens and Frank Mittelbach and Alexander Samarin",
    title     = "The \LaTeX\ Companion",
    year      = "1993",
    publisher = "Addison-Wesley",
    address   = "Reading, Massachusetts"
}

@misc{knuthwebsite,
    author    = "Donald Knuth",
    title     = "Knuth: Computers and Typesetting",
    url       = "http://www-cs-faculty.stanford.edu/\~{}uno/abcde.html"
}

```

在这三条文献中，`einstein`、`latexcompanion`、`knuthwebsite`是文献的标签，在文档中，只需要在适当位置用引用命令如`\cite{}`便可以引用这些文献，例如，`\cite{einstein}`。

```tex
\documentclass[12pt]{article}

\begin{document}

Some examples for showing how to use \texttt{thebibliography} environment:
\begin{itemize}
    \item Book reference sample: The \LaTeX\ companion book \cite{latexcompanion}.
    \item Paper reference sample: On the electrodynamics of moving bodies \cite{einstein}.
    \item Open-source reference sample: Knuth: Computers and Typesetting \cite{knuthwebsite}.
\end{itemize}

\bibliographystyle{unsrt}
\bibliography{sample}

\end{document}
```

编译上述代码，得到文档如图8.3.3所示。

<p align="center">
<img align="middle" src="docs/latex/chapter-8/graphics/example8_3_3.png" width="450" />
</p>

<center><b>图8.3.3</b> 编译后的文档</center>

在`sample.bib`文件中，根据文献类型可定义文献列表，对于每篇文献，需要整理`author`（作者信息）、`title`（文献标题）等基本信息。在LaTeX文档中，我们需要使用`\bibliographystyle`命令申明参考文献的格式，如本例中的`unsrt`，同时，使用`\bibliography`命令申明参考文献的源文件，即`sample.bib`。

当然，BibTeX文献管理也有很多优点：

- 无需重复输入每条参考文献。文献放在BibTeX之后，引用文献的标签即可在文档中显示参考文献。
- 文档中的参考文献格式是根据文档样式自动设置的，且所有文献的引用风格是一致的。
- 引用同一作者同年的文献过多时，引用格式会自动调整。
- BibTeX文件中的文献只有在文档中明确引用才会显示在文档的参考文献中。


在BibTeX文件中，不同类型的文献是需要进行分类的：

- `article`：对应着期刊或杂志上发表的论文，必须添加的信息有`author`（作者）、`title`（标题）、`journal`（期刊）、`year`（年份）、`volume`（卷），可供选择添加的信息包括`number`（期）、`pages`（页码）、`month`（月份）、`doi`（数字对象识别码）等。
- `book`：对应着书籍，必须添加的信息有`author/editor`（作者或主编）、`title`（书名）、`publisher`（出版社）、`year`（年份），可供选择添加的信息包括`volume/number`（卷/期）、`series`（系列）、`address`（出版地址）、`edition`（版号）、`month`（月份）、`url`（网址）等。
- `inbook`：书籍中的一部分或者某一章节，必须添加的信息有`author/editor`、`title`（标题）、`chapter/pages`（章节/页码）、`publisher`（出版社）、`year`（年份），其他可供选择添加的信息与`book`一致。
- `inproceedings`：对应着会议论文，必须添加的信息有`author`（作者）、`title`（论文标题）、`booktitle`（论文集标题）、`year`（年份），可供选择添加的信息包括`editor`（版号）、`volume/number`（卷或期）、`series`（系列）、`pages`（页码）、`address`（地址）、`month`（月份）、`organization`（组织方）、`publisher`（出版社）等。
- `conference`：对应着会议论文，与`inproceedings`用法一致。
- `mastersthesis`和`proceedings`：分别对应着硕士学位论文和博士学位论文，必须添加的信息有`author`（作者）、`title`（标题）、`school`（学校或研究机构）、`year`（年份）。

> 参考[Bibliography management with bibtex](https://www.overleaf.com/learn/latex/Bibliography_management_with_bibtex)。

### 参考资料

- Martin J. Osborne. [using bibtex: a short guide](https://www.economics.utoronto.ca/osborne/latex/BIBTEX.HTM).
- Wikipedia. [BibTeX](https://en.wikipedia.org/wiki/BibTeX).

【回放】[**8.2 创建超链接**](https://nbviewer.jupyter.org/github/xinychen/latex-cookbook/blob/main/chapter-8/section2.ipynb)

【继续】[**8.4 文献引用格式**](https://nbviewer.jupyter.org/github/xinychen/latex-cookbook/blob/main/chapter-8/section4.ipynb)

### License

<div class="alert alert-block alert-danger">
<b>This work is released under the MIT license.</b>
</div>
