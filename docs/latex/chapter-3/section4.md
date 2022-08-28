## 3.4 编辑段落

### 3.4.1 段落首行缩进调整

许多出版社要求文章段落必须首行缩进，若想调整段落首行缩进的距离，可以使用`\setlength{\parindent}{长度}`命令，在`{长度}`处填写需要设置的距离即可。

【**例1**】使用`\setlength{\parindent}{长度}`命令调整段落首行缩进为两字符。

```tex
\documentclass[12pt]{article}
\setlength{\parindent}{2em}
\begin{document}


In \LaTeX, We can use the setlength command to adjust the indentation distance of the first line. In this case, we set the indentation distance as 2em.

\end{document}
```

编译后效果如图3-4-1所示。

<p align="center">
<img align="middle" src="docs/latex/chapter-3/graphics/example3_4_1.png" width="600" />
</p>

<center><b>图3-4-1</b> 编译后效果</center>

当然，如果不想让段落自动首行缩进, 在段落前使用命令`\noindent`即可。

【**例2**】使用`\noindent`命令使第二段首行不缩进。

```tex
\documentclass[12pt]{article}
\setlength{\parindent}{2em}
\begin{document}


In \LaTeX, We can use the setlength command to adjust the indentation distance of the first line. In this case, we set the indentation distance as 2em.

\noindent In \LaTeX, We can use the setlength command to adjust the indentation distance of the first line. In this case, we set the indentation distance as 2em.

\end{document}
```
编译后效果如图3-4-2所示。

<p align="center">
<img align="middle" src="docs/latex/chapter-3/graphics/example3_4_2.png" width="600" />
</p>

<center><b>图3-4-2</b> 编译后效果</center>

需要注意的是，在段落设置在章节后面时，每一节后的第一段默认是不缩进的，为了使第一段向其他段一样缩进，可以在段落前使用`\hspace*{\parindent}`命令，也可以在源文件的前导代码中直接调用宏包`\usepackage{indentfirst}`。

【**例3**】使用`\hspace*{\parindent}`命令使章节后第一段首行缩进。

```tex
\documentclass[12pt]{article}
\setlength{\parindent}{2em}
\begin{document}

\section{Introduction}

\hspace*{\parindent}In \LaTeX, We can use the setlength command to adjust the indentation distance of the first line. In this case, we set the indentation distance as 2em.


In \LaTeX, We can use the setlength command to adjust the indentation distance of the first line. In this case, we set the indentation distance as 2em.

\end{document}
```
编译后效果如图3-4-3所示。

<p align="center">
<img align="middle" src="docs/latex/chapter-3/graphics/example3_4_3.png" width="600" />
</p>

<center><b>图3-4-3</b> 编译后效果</center>

【**例4**】使用`\usepackage{indentfirst}`命令使章节后第一段首行缩进。

```tex
\documentclass[12pt]{article}
\setlength{\parindent}{2em}
\usepackage{indentfirst}
\begin{document}

\section{Introduction}

In \LaTeX, We can use the setlength command to adjust the indentation distance of the first line. In this case, we set the indentation distance as 2em.


In \LaTeX, We can use the setlength command to adjust the indentation distance of the first line. In this case, we set the indentation distance as 2em.

\end{document}
```
编译后效果如图3-4-4所示。

<p align="center">
<img align="middle" src="docs/latex/chapter-3/graphics/example3_4_4.png" width="600" />
</p>

<center><b>图3-4-4</b> 编译后效果</center>




### 3.4.2 段落间距调整

在使用LaTeX排版时，有时为了使段落与段落之间的区别更加明显，我们可以在段落之间设置一定的间距，最简单的方式是使用`\smallskip`、`\medskip`和`\bigskip`等命令。

> 参考[How to insert a blank line between any two paragraphs???](https://latex.org/forum/viewtopic.php?f=44&t=6934)

【**例5**】使用`\smallskip`、`\medskip`和`\bigskip`等命令调整不同的段落间距。

```tex
\documentclass[12pt]{article}

\begin{document}

How to set space between any two paragraphs?

\smallskip
How to set space between any two paragraphs?

\medskip
How to set space between any two paragraphs?

\bigskip
How to set space between any two paragraphs?

\end{document}
```

编译后效果如图3-4-5所示。

<p align="center">
<img align="middle" src="docs/latex/chapter-3/graphics/example3_4_5.png" width="600" />
</p>

<center><b>图3-4-5</b> 编译后效果</center>

设置段落间距的几种方法：[https://tex.stackexchange.com/questions/41476](https://tex.stackexchange.com/questions/41476)


### 3.4.3 段落添加文本框

有时因为文档全都是大段大段的文字，版面显得较为单调，这时，我们可以通过给文字加边框来让版面有所变化，不至于过于单调。在LaTeX中，我们可以使用`\fbox{}`命令对文本新增边框。

> 参考[How to put a box around multiple lines](https://latex.org/forum/viewtopic.php?f=44&t=4117)。

【**例6**】使用`\fbox{}`创建文本边框。

```tex
\documentclass[12pt]{article}

\begin{document}

\fbox{
	\parbox{0.8\linewidth}{
		In \LaTeX, we can use fbox and parbox to put a box around multiple lines. In this case, we set the linewidth as 0.8.
	}
}

\end{document}
```

编译后效果如图3-4-6所示。

<p align="center">
<img align="middle" src="docs/latex/chapter-3/graphics/example3_4_6.png" width="600" />
</p>

<center><b>图3-4-6</b> 编译后效果</center>



### 3.4.4 段落对齐方式调整

LaTeX默认的对齐方式是两端对齐，有时在进行文档排版的过程中，我们为了突出某一段落的内容，会选择将其居中显示，在LaTeX中，我们可以使用`center`环境对文本进行居中对齐。另外还有一些出版商要求文档是左对齐或者右对齐，这时我们同样可以使用`flushleft`环境和`flushright`环境将文档设置为左对齐或右对齐。


【**例7**】分别使用`center`、`flushleft`和`flushright`环境对文本进行居中对齐、左对齐和右对齐。

```tex
\documentclass[12pt]{article}

\begin{document}

\begin{center}
This is latex-cookbook
\end{center}

\begin{flushleft}
This is latex-cookbook
\end{flushleft}

\begin{flushright}
This is latex-cookbook
\end{flushright}

\end{document}
```

编译后效果如图3-4-7所示。

<p align="center">
<img align="middle" src="docs/latex/chapter-3/graphics/example3_4_7.png" width="600" />
</p>

<center><b>图3-4-7</b> 编译后效果</center>

【回放】[**3.3 生成目录**](https://nbviewer.jupyter.org/github/xinychen/latex-cookbook/blob/main/chapter-3/section3.ipynb)

【继续】[**3.5 编辑文字**](https://nbviewer.jupyter.org/github/xinychen/latex-cookbook/blob/main/chapter-3/section5.ipynb)

### License

<div class="alert alert-block alert-danger">
<b>This work is released under the MIT license.</b>
</div>
