## 10.4 简历制作

LaTeX可制作各类文档，其中也不乏简历，与其他各类文档相比，简历在制作的过程中注重内容的简洁与清晰。使用LaTeX制作简历有诸多优势：第一，无需考虑字体、颜色、排版等问题；第二，LaTeX拥有众多简历模板可供选择，易于切换简历的排版风格。

### 10.4.1 使用`article`文档类型制作简历

`article`文档类型是LaTeX中极为常用的一种文档类型，使用`article`文档类型制作简历时，可将文档的结构命令如`\section{}`、`\subsection{}`、`\subsubsection{}`等格式稍作调整。

```tex
\documentclass{article}

\begin{document}



\end{document}
```


### 10.4.1 自定义简历格式

在 LaTeX 文件中编写`documentclass{article}`时，包括了类文件`article.cls`。该类文件定义了组织文档的所有命令，比如片段和标题，它还配置这些命令如何影响页面的格式和布局。使用LaTeX制作简历时，我们需要自定义文档格式。其中最简洁的方法是将所有信息保存在个人类文件中，这样可以使文档的结构与格式完全分离，从而便于使用。因此，我们需要创建一个简历的类文件，例如`CV.cls`，然后在类文件内定义文档格式。

所有类文件都应该以下面两行代码开头，应该将它们添加到`CV.cls`的顶部。

```tex

\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{CV}[2021/08/29 My custom CV class]

```

`\NeedsTeXFormat{LaTeX2e}`命令告诉编译器该包适用于哪个版本的 LaTeX,LaTeX 的当前版本是 LaTeX2e。`\ProvidesClass{CV}[2021/08/29 My custom CV class]`第一个参数应该匹配类文件的文件名，并告诉 LaTeX 包的名称。第二个参数是可改变的，它提供了类的描述，这些描述将出现在日志和其他地方。

随后，我们创建一个编译文件`CV.tex`，并将以下代码键入文件，填写简历中的个人信息。

```tex

\documentclass{CV}

\begin{document}

\section{Research Interests}
\subsection{Machine Learning}

\section{Education}
\subsection{University of Nowhere}

\end{document}
```

编译效果如图10.4.1所示。

<p align="center">
<img align="middle" src="docs/latex/chapter-10/graphics/example10_4_1.png" width="250" />
</p>

<center><b>图10.4.1</b> 编译后效果</center>

如图10.4.1所示，标准的文章标题并不适合简历，所以我们希望用更整洁的格式取代它们。为此，我们可以在`CV.cls`文件中重新定义`section`命令以输出自定义格式。在这里我们需要使用`titlesec`宏包，调用命令为`\RequirePackage{titlesec}`，随后，我们便可以自定义标题格式。在`CV.cls`文件中键入以下代码：

```tex

\RequirePackage{titlesec}

\titleformat{\section}         
  {\bfseries\Large\scshape\raggedright} 
  {}{0em}                      
  {}                           
  [\titlerule]   
  
\titleformat{\subsection}
  {\large\scshape\raggedright}
  {}{0em}
  {}

```

键入以上代码后，再次编译`CV.tex`文件，编译效果如图10.4.2所示。

<p align="center">
<img align="middle" src="docs/latex/chapter-10/graphics/example10_4_2.png" width="550" />
</p>

<center><b>图10.4.2</b> 编译后效果</center>

自定义标题格式可以使用以下命令：

- \bfseries, \itshape: 标题加粗或加斜体;
- \scshape： 小型资本;
- \small, \normalsize, \large, \Large, \LARGE, \huge, \Huge: 设定字型大小;
- \rmfamily, \sffamily, \ttfamily: 将字体类型分别设置为有衬线字体、无衬线字体或打字机字体。

简历的部分章节需要添加日期，我们在`CV.cls`文件中定义一个新命令`\datedsubsection`，命令可以让我们在子章节标题中添加日期，新命令代码为：

```tex

\newcommand{\datedsubsection}[2]{%
  \subsection[#1]{#1 \hfill #2}%
}

```
键入以上代码后，在`CV.tex`文件中更改部分代码，使用新定义命令：

```tex
\documentclass{CV}

\begin{document}

\section{Research Interests}
\subsection{Machine Learning}

\section{Education}
\datedsubsection{University of Nowhere}{2012---2016} %使用新定义命令

\end{document}
```

编译效果如图10.4.3所示。

<p align="center">
<img align="middle" src="docs/latex/chapter-10/graphics/example10_4_3.png" width="550" />
</p>

<center><b>图10.4.3</b> 编译后效果</center>

在简历中，名字通常在最上面，并且包含相关的联系方式，同样地我们在`CV.cls`文件中定义一个新命令`\name`来添加名字，定义另一个新命令`\contact`来添加联系方式。

```tex

\newcommand{\name}[1]{%
  \centerline{\Huge{#1}}
}

\newcommand\contact[5]{%
    \centerline{%
        \makebox[0pt][c]{%
            #1 {\large\textperiodcentered} #2 {\large\textperiodcentered} #3
            \ #4 \ \ #5%
        }%
    }%
}

```

键入以上代码后，在`CV.tex`文件中使用新定义命令`\name`和`\contact`：

```tex
\documentclass{CV}

\begin{document}

\name{John Kim}

\contact{123 Broadway}{London}{UK 12345}{john@kim.com}{(000)-111-1111}

\section{Research Interests}
\subsection{Machine Learning}
My research interest is machine learning. 

\section{Education}
\datedsubsection{University of Nowhere}{2012---2016}
I attended the University of Nowhere from 2012 to 2016.

\end{document}
```
编译效果如图10.4.4所示。

<p align="center">
<img align="middle" src="docs/latex/chapter-10/graphics/example10_4_4.png" width="550" />
</p>

<center><b>图10.4.4</b> 编译后效果</center>

当然也可以自定义一些列表：

```tex

\newcommand{\researchitems}[3]{%
    \begin{itemize}
    \item #1
    \item #2
    \item #3
    \end{itemize}%
}

```

键入以上代码后，在`CV.tex`文件中使用新定义命令`\researchitems`：

```tex
\documentclass{CV}

\begin{document}

\name{John Kim}

\contact{123 Broadway}{London}{UK 12345}{john@kim.com}{(000)-111-1111}

\section{Research Interests}
\subsection{Machine Learning}
My research interest is machine learning.
\researchitems
{Logistic regression}
{Neural Networks}
{SVM}

\section{Education}
\datedsubsection{University of Nowhere}{2012---2016}
I attended the University of Nowhere from 2012 to 2016.

\end{document}
```

编译效果如图10.4.5所示。

<p align="center">
<img align="middle" src="docs/latex/chapter-10/graphics/example10_4_5.png" width="550" />
</p>

<center><b>图10.4.5</b> 编译后效果</center>



### 10.4.2 参考模板制作简历

LaTeX在线网站Overleaf中提供了海量的[简历模板](https://www.overleaf.com/gallery/tagged/cv)，我们可以在寻找精美的、简洁的、正式的等各种类型的简历模板，并在上面填写自己的信息即可。Overleaf的简历模板中，前三个例子如图10.4.6所示。

<p align="center">
<table>
<tr>
<td><img align="middle" src="docs/latex/chapter-10/graphics/example10_4_6_1.png" width="300"></td>
<td><img align="middle" src="docs/latex/chapter-10/graphics/example10_4_6_2.png" width="300"></td>
<td><img align="middle" src="docs/latex/chapter-10/graphics/example10_4_6_3.png" width="300"></td>
</tr>
</table>
</p>

<center><b>图10.4.6</b> Overleaf的简历模板</center>

### 10.4.3 制作中文简历



### 参考资料

[1] 适用中文的简历模板（GitHub网址为[https://github.com/dyweb/awesome-resume-for-chinese](https://github.com/dyweb/awesome-resume-for-chinese)）.

### License

<div class="alert alert-block alert-danger">
<b>This work is released under the MIT license.</b>
</div>
