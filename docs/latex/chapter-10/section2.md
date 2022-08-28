## 10.2 算法伪代码

算法这个词的英文是algorithm，它几乎贯穿了整个计算机的各个领域。算法伪代码作为自然语言与类编程语言组成的混合结构，它在描述算法结构和思路方面要比纯编程语言更简洁且可读性更好、相比自然语言则更准确。同时，我们也能很容易地将算法伪代码转换成计算机程序。因此，在计算机相关的技术文档或文献中，适当使用算法伪代码解释技术架构会更方便读者理解。

在LaTeX中，为了便于创建算法伪代码，现有很多相关的宏包，例如`algorithm`和`algorithmic`，在前导代码中申明使用这些宏包便可使用相应的算法伪代码环境。宏包`algorithm`提供的算法伪代码环境为`\begin{algorithm} \end{algorithm}`和`\begin{algorithmic} \end{algorithmic}`。

【**例1**】使用`algorithm`和`algorithmic`宏包中相应的环境创建一个简单的算法伪代码。

```tex
\documentclass[12pt]{article}
\usepackage{algorithm}
\usepackage{algorithmic}
\usepackage{amsmath, amsfonts}

\begin{document}

This is a simple example:

\begin{algorithm}
\renewcommand{\algorithmicrequire}{\textbf{Input:}}
\renewcommand{\algorithmicensure}{\textbf{Output:}}
\caption{Inner product of vectors}
\begin{algorithmic}[1]
\REQUIRE $\boldsymbol{x},\boldsymbol{y}\in\mathbb{R}^{n}$
\ENSURE $c$
\STATE $c=0$
\FOR{$i=1$ to $n$}
\STATE $c=c+x_iy_i$
\ENDFOR
\end{algorithmic}
\end{algorithm}

\end{document}
```

编译上述代码，得到的算法伪代码如图10.2.1所示。

<p align="center">
<img align="middle" src="latex/chapter-10/graphics/example1.png" width="750" />
</p>

<center><b>图10.2.1</b> 编译后的算法伪代码</center>

在例子中，语句`\renewcommand{\algorithmicrequire}{\textbf{Input:}}`表示将算法伪代码中的关键词require替换成Input，同理，我们也能将关键词ensure替换成Output。


除了`algorithm`和`algorithmic`这两个专门用于创建算法伪代码的宏包，还有一个非常常用的宏包，叫`algorithm2e`，它与`algorithm`宏包创建出来的算法伪代码在样式上略有不同，`algorithm2e`也提供了一种`\begin{algorithm} \end{algorithm}`环境。

【**例2**】使用`algorithm`宏包中相应的环境创建一个简单的算法伪代码。

```tex
\documentclass[12pt]{article}
\usepackage[linesnumbered, boxed]{algorithm2e}
\usepackage{amsmath, amsfonts}

\begin{document}

This is a simple example:

\IncMargin{1em}
\begin{algorithm}
\SetKwInOut{Input}{Input}
\SetKwInOut{Output}{Output}
\caption{Inner product of vectors}
\Input{$\boldsymbol{x},\boldsymbol{y}\in\mathbb{R}^{n}$}
\Output{$c$}
$c=0$\;
\For{$i=1$ \KwTo $n$}{
$c=c+x_iy_i$\;
}
\end{algorithm}

\end{document}
```

编译上述代码，得到的算法伪代码如图10.2.2所示。

<p align="center">
<img align="middle" src="latex/chapter-10/graphics/example2.png" width="750" />
</p>

<center><b>图10.2.2</b> 编译后的算法伪代码</center>

在例子中，申明使用宏包`algorithm2e`时将参数设置为`linesnumbered`和`boxed`，这两个参数分别表示对算法伪代码各行进行编号和对算法伪代码区域加边框，作为全局参数，会成为算法伪代码中的默认设置。

### 参考资料

- 宏包algorithm2e的使用说明文档：[algorithm2e.sty — package for algorithms](https://mirrors.cqu.edu.cn/CTAN/macros/latex/contrib/algorithm2e/doc/algorithm2e.pdf), July 18, 2017.

【回放】[**10.1 程序源代码**](https://nbviewer.jupyter.org/github/xinychen/latex-cookbook/blob/main/chapter-10/section1.ipynb)

【继续】[**10.3 海报制作**](https://nbviewer.jupyter.org/github/xinychen/latex-cookbook/blob/main/chapter-10/section3.ipynb)

### License

<div class="alert alert-block alert-danger">
<b>This work is released under the MIT license.</b>
</div>
