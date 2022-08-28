## 3.5 文本编辑

文本编辑是制作文档非常重要的一部分，在编辑文本的过程中，主要关注的内容有如何调整字体样式、字体设置、增加下划线、突出文字、调整字体大小、调整对齐格式等。

### 3.5.1 调整字体样式

调整文字的样式有很多对应的命令，这些命令包括`\textit`、`\textbf`、`\textsc`、`\texttt`，在使用的过程中，需要用到花括号`{}`。具体而言，`\textit`对应着斜体字，`\textbf`对应着粗体字，`\textsc`对应着小型大写字母，`\texttt`对应着打印机字体（即等宽字体）。

【**例1**】使用`\textit`、`\textbf`、`\textsc`、`\texttt`对字体样式进行调整。

```tex
\documentclass[12pt]{article}

\begin{document}

Produce \textit{italicized} text. \\      % 生成斜体字的文本

Produce \textbf{bold face} text. \\       % 生成粗体字的文本

Produce \textsc{small caps} text. \\      % 生成小型大写字母的文本

Produce \texttt{typewriter font} text. \\ % 生成打字机字体的文本

\end{document}
```
编译后效果如图3-5-1所示。

<p align="center">
<img align="middle" src="latex/chapter-3/graphics/example3_5_1.png" width="400" />
</p>

<center><b>图3-5-1</b> 编译后效果</center>

除了这几种字体样式，有时候，如果想对文本中的英文字母进行全部大写，可用`\uppercase`和`\MakeUppercase`两个命令中的任意一个。

> 参考[Force all uppercase](https://latex.org/forum/viewtopic.php?f=44&t=3539)。

【**例2**】分别使用`\uppercase`和`\MakeUppercase`将文本中的英文字母进行全部大写。

```tex
\documentclass[12pt]{article}

\begin{document}

\uppercase{Use uppercase command to force all uppercase.}


\MakeUppercase{Use MakeUppercase command to force all uppercase.}

\end{document}
```

编译后效果如图3-5-2所示。

<p align="center">
<img align="middle" src="latex/chapter-3/graphics/example3_5_2.png" width="400" />
</p>

<center><b>图3-5-2</b> 编译后效果</center>

一般而言，当我们需要对段落、句子、关键词等做特殊标记时，往往会用到上述几种字体样式，其中，打字机字体主要用于代码的排版，有时候，如果需要添加一个网站，通常也会选用打字机字体对文本进行突出，例如`\texttt{https://www.overleaf.com}`。




### 3.5.2 调整字体大小

字体大小的设置一方面可以在申明文档类型的命令`\documentclass[]{}`中指定具体的字体大小（如11pt、12pt）来实现，另一方面也可以通过一些简单的命令来调整。例如：

```tex
\documentclass[12pt]{article}
\begin{document}

Produce {\tiny tiny word}

Produce {\scriptsize script size word}

Produce {\footnotesize footnote size word}

Produce {\normalsize normal size word}

Produce {\large large word}

Produce {\Large Large word}

Produce {\LARGE LARGE word}

Produce {\huge huge word}

Produce {\Huge Huge word}

\end{document}
```

编译后效果如图3-5-3所示。

<p align="center">
<img align="middle" src="latex/chapter-3/graphics/example3_5_3.png" width="400" />
</p>

<center><b>图3-5-3</b> 编译后效果</center>

在这里，这些命令对应的字体依次是从小到大。当然，这些命令也有另外一种使用方法，以`\large`、`\Large`、`\LARGE`为例，我们可以使用`\begin{} \end{}`语句来实现对字体的加大：

```tex
\documentclass[12pt]{article}
\begin{document}

Produce \begin{large}large word\end{large}

Produce \begin{Large}large word\end{Large}

Produce \begin{LARGE}large word\end{LARGE}

\end{document}
```

编译后效果如图3-5-4所示。

<p align="center">
<img align="middle" src="latex/chapter-3/graphics/example3_5_4.png" width="400" />
</p>

<center><b>图3-5-4</b> 编译后效果</center>




### 3.5.3 调整字体颜色

一般而言，文本默认的颜色是黑色，但有时候，我们可以根据需要改变字体的颜色，这通过LaTeX一些拓展的宏包就可以实现，例如`xcolor`。

使用颜色宏包时，我们也可以根据需要自定义颜色，相应的命令为`\definecolor{A}{B}{C}`，其中，位置A是颜色标签，位置B是制定颜色系统为RGB（英文缩写RGB是红色、绿色和蓝色三种颜色的英文单词首字母），位置C是具体的RGB数值。

【**例3**】使用颜色宏包`color`中的`\definecolor{}{}{}`命令自定义一系列颜色并制作简单文档。

```tex
\documentclass[12pt]{article}

\usepackage{color}
\definecolor{kugreen}{RGB}{50, 93, 61}
\definecolor{kugreenlys}{RGB}{132, 158, 139}
\definecolor{kugreenlyslys}{RGB}{173, 190, 177}
\definecolor{kugreenlyslyslys}{RGB}{214, 223, 216}

\begin{document}

This is a simple example for using \LaTeX.

{\color{kugreen}This is a simple example for using \LaTeX.}

{\color{kugreenlys}This is a simple example for using \LaTeX.}

{\color{kugreenlyslys}This is a simple example for using \LaTeX.}

{\color{kugreenlyslyslys}This is a simple example for using \LaTeX.}

\end{document}
```

编译后效果如图3-5-5所示。

<p align="center">
<img align="middle" src="latex/chapter-3/graphics/example3_5_5.png" width="400" />
</p>

<center><b>图3-5-5</b> 编译后效果</center>




### 3.5.4 字体设置

不管是英文还是中文，我们都会越到各种各样的字体，因此，使用LaTeX编译出想要的字体对于整个文档也非常重要。对于英文文档的编译，一般会用宏包`fontspec`设置具体的字体，调用格式为`\usepackage{fontspec}`，需要说明的是，这个宏包只能设置英文的字体。例如：
```tex
\setmainfont{Times New Roman}
\setsansfont{DejaVu Sans}
\setmonofont{Latin Modern Mono}
\setsansfont{[foo.ttf]}   
```
在LaTeX中，编译文档一般默认的英文字体为Computer Modern，如果要将其调整为其他特定类型的字体，可以在前导代码中使用各种字体对应的工具包。

【**例4**】新建一个简单文档，并将字体设置为Palatino。

```tex
\documentclass[a4paper, 12pt]{article}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{palatino} % palatino工具包提供了Palatino字体

\begin{document}

Hello, LaTeXers! This is our first LaTeX document.

\end{document}
```

编译后效果如图3-5-6所示。

<p align="center">
<img align="middle" src="latex/chapter-3/graphics/example3_5_6.png" width="400" />
</p>

<center><b>图3-5-6</b> 编译后效果</center>

如果文档输入的是中文，首先需要申明文档类型为ctex中的ctexart、ctexrep之类的。本书的2.6节已经介绍了部分中文字体的设置方式，宋体、仿宋、隶书、黑体、楷体、幼圆、微软雅黑等字体为目前常用的大部分中文字体，例3-21将使用ctexart给出它们的设置方式。

【**例5**】新建一个简单文档，设置一些宋体、仿宋、隶书、黑体、楷体、幼圆、微软雅黑等字体。
```tex
\documentclass[12pt,a4paper,utf8]{ctexart}

\begin{document}

\noindent 字体（默认宋体）\\
\fangsong 字体（仿宋） \songti 字体（宋体） \lishu 字体（隶书） \heiti 字体（黑体）\\
\CJKfamily{zhkai} 字体（楷书） \CJKfamily{zhyou} 字体（幼圆） \CJKfamily{zhyahei} 字体（微软雅黑）\\

\end{document}
```
编译后效果如图3-5-7所示。

<p align="center">
<img align="middle" src="latex/chapter-3/graphics/example3_5_7_1.png" width="400" />
</p>

<center><b>图3-5-7</b> 编译后效果</center>

> 不同字体对应的工具包可参考[Font typefaces](https://www.overleaf.com/learn/latex/Font_typefaces).




### 3.5.5 下划线与删除线

有时候，为了突出特定的文本，我们也会使用到各种下划线。最常用的下划线命令是`\underline`，然而，这个命令存在一个缺陷，即当文本过长，超过页面宽度时，下划线不会自动跳到下一行，因此，我们需要用到一个叫`ulem`的宏包，使用这个宏包中的命令`\uline`可以增加单下划线，使用`\uuline`可以增加双下划线，而使用`\uwave`则可以增加波浪线。

【**例6**】使用`\underline`、`\uline`、`\uuline`、`\uwave`对文本增加下划线。

```tex
\documentclass[12pt]{article}
\usepackage{ulem}
\begin{document}

Generate \underline{underlined} text. \\     % 生成带下划线的文本（使用\underline命令）

Generate \uline{underlined} text. \\         % 生成单下划线的文本（使用\uline命令）

Generate \uuline{double underlined} text. \\ % 生成单下划线的文本

Generate \uwave{wavy underlined} text. \\   % 生成波浪线的文本

\end{document}
```

编译后效果如图3-5-8所示。

<p align="center">
<img align="middle" src="latex/chapter-3/graphics/example3_5_7.png" width="400" />
</p>

<center><b>图3-5-8</b> 编译后效果</center>

删除线是文字中间划出的线段，常见于文档的审阅。在LaTeX中，我们可以使用宏包`soul`中的`\st`命令生成删除线。

> 参考[Horizontal strikethrough?](https://latex.org/forum/viewtopic.php?f=44&t=5545)。

【**例7**】使用`soul`宏包中的`\st`命令对文本增加删除线。

```tex
\documentclass[12pt]{article}
\usepackage{soul}
\begin{document}

Generate \st{strikethrough} text. \\     % 生成带删除线的文本

Generate \st{many many strikethrough strikethrough strikethrough strikethrough strikethrough strikethrough} text. \\     % 生成带删除线的文本

\end{document}
```

编译后效果如图3-5-9所示。

<p align="center">
<img align="middle" src="latex/chapter-3/graphics/example3_5_8.png" width="750" />
</p>

<center><b>图3-5-9</b> 编译后效果</center>

当然，我们也可以根据需要对文本的下标增加下划线。

> 参考[Underscore (_) symbol as "space" in the generated PDF](https://latex.org/forum/viewtopic.php?f=48&t=8891)

【**例8**】对文本的下标增加下划线。

```tex
\documentclass[12pt]{article}
\begin{document}

This\_is\_text\_with\_underscores.

\end{document}
```

编译后效果如图3-5-10所示。

<p align="center">
<img align="middle" src="latex/chapter-3/graphics/example3_5_9.png" width="400" />
</p>

<center><b>图3-5-10</b> 编译后效果</center>


### 3.5.6 特殊字符

在LaTeX中，有很多特殊字符的编译需要遵循一定的规则，例如，

- 反斜杠 (backslash) 符号是LaTeX中定义和使用各类命令的基本符号，如果要在文档中编译出反斜杠，可使用`\textbackslash`；
- 百分号通常用于注释代码，如果要在文档中编译出百分号，可使用`\%`；
- 美元符号通常用于书写公式，如果要在文档中编译出美元符号，可使用`\$`。

> 参考[how to enter backslash (\) in your text](https://latex.org/forum/viewtopic.php?t=12239)

带圆圈数字可用于各类编号，我们可以根据需要插入这种特殊符号。在LaTeX中，比较常用的一种生成带圆圈数字的方法是使用宏包`pifont`，在前导代码中申明使用宏包，即`\usepackage{pifont}`，根据工宏包所提供的命令`\ding{}`可以生成从1到10的带圆圈数字，且圆圈样式也各异。

> 参考[write number in circle](https://latex.org/forum/viewtopic.php?f=44&t=19995)

【**例9**】使用`pifont`宏包中的命令生成从1到10的带圆圈数字。

```tex
\documentclass[12pt]{article}
\usepackage{pifont}
\begin{document}

How to write a number in a circle? \\
Type 1: \ding{172}-\ding{173}-\ding{174}-\ding{175}-\ding{176}-\ding{177}-\ding{178}-\ding{179}-\ding{180}-\ding{181} \\     % 样式1是从172开始
Type 2: \ding{182}-\ding{183}-\ding{184}-\ding{185}-\ding{186}-\ding{187}-\ding{188}-\ding{189}-\ding{190}-\ding{191} \\     % 样式2是从182开始
Type 3: \ding{192}-\ding{193}-\ding{194}-\ding{195}-\ding{196}-\ding{197}-\ding{198}-\ding{199}-\ding{200}-\ding{201} \\     % 样式3是从192开始
Type 4: \ding{202}-\ding{203}-\ding{204}-\ding{205}-\ding{206}-\ding{207}-\ding{208}-\ding{209}-\ding{210}-\ding{211} \\     % 样式4是从202开始

\end{document}
```
编译后效果如图3-5-11所示。

<p align="center">
<img align="middle" src="latex/chapter-3/graphics/example3_5_10.png" width="400" />
</p>

<center><b>图3-5-11</b> 编译后效果</center>

### 练习题

> 打开LaTeX在线系统[https://www.overleaf.com](https://www.overleaf.com/project)或本地安装好的LaTeX编辑器，创建名为LaTeX_practice的项目，并同时新建一个以`.tex`为拓展名的源文件，完成以下几道练习题。

[1] 使用`\emph`命令对以下指定文字的字体样式进行调整。

```tex
\documentclass[12pt]{article}
\begin{document}

%% 要求：使用\emph生成斜体字的文本
%% 提示：在花括号外适当位置输入\emph命令，并对源文件进行编译
Produce {emphasized} text.

\end{document}
```

[2] 在LaTeX中使用双引号。

```tex
\documentclass[12pt]{article}
\begin{document}

%% 提示：在需要加引号的文本左侧使用``、右侧使用''符号即可
 A quoted word.
 
\end{document}
```

> 注：实际上，还有另外一种方法（参考[Double Quotation Marks](https://latex.org/forum/viewtopic.php?f=44&t=21620)），需要用到`csquotes`宏包中的`\enquote`命令，例如

```tex
\documentclass[12pt]{article}
\usepackage{csquotes}

\begin{document}

A \enquote{quotation with an \enquote{inner} quotation.}
 
\end{document}
```

【回放】[**3.4 编辑段落**](https://nbviewer.jupyter.org/github/xinychen/latex-cookbook/blob/main/chapter-3/section4.ipynb)

【继续】[**3.6 创建列表**](https://nbviewer.jupyter.org/github/xinychen/latex-cookbook/blob/main/chapter-3/section6.ipynb)

### License

<div class="alert alert-block alert-danger">
<b>This work is released under the MIT license.</b>
</div>
