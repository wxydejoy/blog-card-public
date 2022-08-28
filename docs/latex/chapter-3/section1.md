## 3.1 创建标题部分、摘要及关键词

文档主体代码是指位于document环境的部分。在文档正文章节内容及目录之前，一般先创建标题部分（包括文档标题、作者和日期）、摘要、以及关键词信息，这也是文档主体代码中最开始的部分。下面分别介绍这部分的创建过程。

### 3.1.1 创建标题部分

这一部分与`2.5.1添加标题、日期、作者信息`类似

- 使用`\title{}`命令设置文档标题

    对于较长的文档标题，可以使用`\\`对标题内容进行分行。

- 使用`\author{}`命令设置作者

    如果有多个作者，作者之间可以使用`\and`进行分隔。

- 使用`\date{}`命令设置日期信息

    在实际使用时，有时需要省略日期信息，那么在{}中不写任何内容即可。如果想要使用默认值（当前日期），则应使用`\date`命令。
    
- 使用`\maketitle`命令完成标题部分的创建

   仅仅执行上述三行语句无法在文档编译时生成标题部分，还必须在之后加上`\maketitle`命令，表示对标题部分内容进行排版才能真正实现标题部分的创建，具体实例见例1。




### 3.1.2 创建摘要及关键词

在LaTeX中，使用`abstract`环境撰写文档摘要部分，并在其后使用`\textbf{}`命令设置文档关键词。

【**例1**】创建标题部分、摘要及关键词。

```tex
\documentclass[fontsize=12pt]{article}

\begin{document}

\title{My title} % 设置文档标题
\author{A, B and C} % 设置作者
\date{August 2021} % 设置日期信息
\maketitle %

\begin{abstract}  % 设置摘要
This is the abstract. This is the abstract. This is the abstract. This is the abstract. This is the abstract. This is the abstract. 
\end{abstract}
\textbf{Keywords: keyword1, keyword2, keyword3}  % 设置关键词

Hello, LaTeX! Hello, LaTeX! Hello, LaTeX! Hello, LaTeX! Hello, LaTeX! Hello, LaTeX! Hello, LaTeX! Hello, LaTeX! Hello, LaTeX! Hello, LaTeX! Hello, LaTeX! Hello, LaTeX!  % 文档内容

\end{document}
```

编译后的效果如图3-1-1所示：

<p align="center">
<img align="middle" src="docs/latex/chapter-3/graphics/example3_1_1.png" width="500" />
</p>

<center><b>图3-1-1</b> 编译后效果</center>





【回放】[**导言**](https://nbviewer.jupyter.org/github/xinychen/latex-cookbook/blob/main/chapter-3/section0.ipynb)

【继续】[**3.2 创建章节**](https://nbviewer.jupyter.org/github/xinychen/latex-cookbook/blob/main/chapter-3/section2.ipynb)

### License

<div class="alert alert-block alert-danger">
<b>This work is released under the MIT license.</b>
</div>
