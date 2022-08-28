## 9.3 块与盒子——添加框元素

在幻灯片中框选文本或图片等元素是常见的操作，可以对幻灯片内容进行划分或者突出重点内容。在Beamer中，可以通过添加区块环境（block environments）或创建盒子（box）结构的方式将文本等元素放在各式各样的框中。

### 9.3.1 区块环境

Beamer提供了区块环境（block）可用于编辑文本内容，通过block环境创建的文本内容将放置在一个框中，使其与普通文本区分开。根据内容样式和使用目的的不同，包括三种区块环境：

+ `block`：一般性区块环境。使用语法为`\begin{block}<指定显示步骤>{设置标题} \end{block}`；

+ `alertblock`：警示性区块环境，主要用于创建警示信息。使用语法为`\begin{alertblock}<指定显示步骤>{设置标题} \end{alertblock}`；

+ `exampleblock`：示例性区块环境，主要用于创建示例文本。使用语法为`\begin{exampleblock}<指定显示步骤>{设置标题} \end{exampleblock}`。

在三种区块环境的开始命令中（如：`\begin{block}<指定显示步骤>{设置标题}`），“<>”可用于指定当前区块内容显示的步骤，实现动画效果；第二个“{}”可用于设置该区块内容的标题，标题将显示在区块内容的上面。此外，区块内容的样式由使用的Beamer主题样式决定。

【**例9-29**】在`beamer`文档类型中使用`block`环境插入一个一般文本框、使用`alertblock`环境插入一个警示性文本框、以及使用`exampleblock`环境插入一个示例性文本框。

```tex
\documentclass{beamer}
\usefonttheme{professionalfonts}
\usetheme{Copenhagen}

\begin{document}

\begin{frame}
\begin{block}<1>{Block1}
This is a generic block.
\end{block}

\begin{alertblock}<1>{Block2}
This is an alert block.
\end{alertblock}

\begin{exampleblock}<1>{Block3}
This is an example block.
\end{exampleblock}
\end{frame}

\end{document}
```

编译上述代码，得到幻灯片如图9.3.1所示。

<p align="center">
<img align="middle" src="latex/chapter-9/graphics/NEWexample05.png" width="450">
</p>

<center><b>图9.3.1</b> 编译后的幻灯片效果</center>

### 9.3.2 定理类环境

对于定理、引理、推论、示例等定理类文本，除了可以考虑使用区块环境创建之外，Beamer也预定义了相应的命令环境可供使用，包括：

+ `definition`：定义环境。使用语法为`\begin{definition}<指定显示步骤>{设置名称} \end{definition}`；

+ `fact`：事实环境。使用语法为`\begin{fact}<指定显示步骤>{设置名称} \end{fact}`；

+ `theorem`：定理环境。使用语法为`\begin{theorem}<指定显示步骤>{设置名称} \end{theorem}`；

+ `lemma`：引理环境。使用语法为`\begin{lemma}<指定显示步骤>{设置名称} \end{lemma}`；

+ `proof`：证明环境。使用语法为`\begin{proof}<指定显示步骤>{设置名称} \end{proof}`；

+ `corollary`：推论环境。使用语法为`\begin{corollary}<指定显示步骤>{设置名称} \end{corollary}`；

+ `example`：示例环境等。使用语法为`\begin{example}<指定显示步骤>{设置名称} \end{example}`。

定理类环境的使用与区块环境类似：使用定理类环境可以创建文本框；开始命令中的“<>”可用于指定当前内容显示的步骤，实现动画效果；第二个“{}”可用于设置该定理类内容的名称。不同于区块环境的是：定理类内容的标题默认为对应的定理类型，如在`definition`环境下，标题即为“Definition”，显示在定理类内容的上方；而定理类内容的名称允许用户自行定制，通常位于定理类内容的左侧，以较大的斜体字标示。

【**例9-30**】在`beamer`文档类型中使用`definition`环境插入一个定义文本框、使用`theorem`环境插入一个定理文本框、以及使用`example`环境插入一个示例文本框。

```tex
\documentclass{beamer}
\usefonttheme{professionalfonts}
\usetheme{Copenhagen}

\begin{document}

\begin{frame}{Definition, theorem and example}
\begin{definition}<1>{Definition Demo}
This is a definition.
\end{definition}

\begin{theorem}<1>{Theorem Demo}
This is a theorem.
\end{theorem}

\begin{example}<1>{Example Demo}
This is an example.
\end{example}
\end{frame}

\end{document}
```

编译上述代码，得到幻灯片如图9.3.2所示。

<p align="center">
<img align="middle" src="latex/chapter-9/graphics/NEWexample04.png" width="450">
</p>

<center><b>图9.3.2</b> 编译后的幻灯片效果</center>


### 9.3.3 Beamer中的盒子

Beamer也支持通过绘制外框的方式为幻灯片的元素（如，文本、图片等）加上外框，或者说创建盒子（box）。常用的语法包括调用`\fbox{}`命令绘制简单矩形框、或调用`fancybox`宏包提供的命令（`\shadowbox`，`\doublebox`，`\ovalbox`和`Ovalbox`）创建不同类型的外框。

#### （1）使用`\fbox`命令

使用`\fbox{}`命令可以创建简单的矩形盒子，调用以下命令可以对盒子参数进行修改：

+ `\setlength{\fboxsep}{}`：设置盒子内的元素与其边框之间的距离，默认值为3pt；

+ `\setlength{\fboxrule}{}`：设置盒子边框线的粗细，默认值为0.4pt。

此外，盒子之间的行间距可以使用`\vskip`命令进行修改。

【**例9-31**】在`beamer`文档类型中使用`\fbox{}`命令三个文本盒子、使用`\setlength`命令设置不同参数、并使用`\vskip`命令设置行间距。

```tex
\documentclass{beamer}

\begin{document}

\begin{frame}
\setlength{\fboxsep}{3pt}
\setlength{\fboxrule}{0.4pt}
\fbox{This is our 1st text box.}
\vskip 5mm
\setlength{\fboxsep}{6pt}
\setlength{\fboxrule}{0.8pt}
\fbox{This is our 2nd text box.}
\vskip 5mm
\setlength{\fboxsep}{9pt}
\setlength{\fboxrule}{1.2pt}
\fbox{This is our 3rd text box.}
\end{frame}

\end{document}
```

编译上述代码，得到幻灯片如图9.3.3所示。

<p align="center">
<img align="middle" src="latex/chapter-9/graphics/NEWexample06new.png" width="450">
</p>

<center><b>图9.3.3</b> 编译后的幻灯片效果</center>

对于较短的文本内容，使用`\fbox{}`命令可以实现较好的效果。但由于在`\fbox{}`命令中换行符`\\`不起作用，因此如果要对段落文本或长文本创建盒子，需要先将文本内容放置到段落环境中，然后再调用`\fbox{}`命令。其中，`\begin{minipage}[外部对齐方式][高度][内部对齐方式]{宽度}{内容}  \end{minipage}`环境和`\parbox[外部对齐][高度][内部对齐]{宽度}{内容}`命令是比较常用的处理段落的语法。

【**例9-32**】在`beamer`文档类型中使用`\fbox{}`命令和`minipage`环境创建段落文本盒子。

```tex
\documentclass{beamer}

\begin{document}

\begin{frame}

\fbox{
\begin{minipage}[c][1.8cm][t]{5cm}
{This is our paragraph text box. This is our paragraph text box. This is our paragraph text box. This is our paragraph text box.}
\end{minipage}}

\end{frame}

\end{document}
```

编译上述代码，得到幻灯片如图9.3.4所示。

<p align="center">
<img align="middle" src="latex/chapter-9/graphics/NEWexample07.png" width="450">
</p>

<center><b>图9.3.4</b> 编译后的幻灯片效果</center>

类似地，也可以使用`\parbox`命令处理段落文本，与`minipage`环境类似，该命令也能设置外部对齐方式、高度、内部对齐方式、以及宽度参数。用`\parbox`命令改写例9-32的代码，编译得到与图9.3.4相同的结果，具体语句如下例所示：

【**例9-33**】在`beamer`文档类型中使用`\fbox{}`命令和`\parbox`命令创建段落文本盒子。

```tex
\documentclass{beamer}

\begin{document}

\begin{frame}

\fbox{
\parbox[c][1.8cm][t]{5cm}
{This is our paragraph text box. This is our paragraph text box. This is our paragraph text box. This is our paragraph text box.}}

\end{frame}

\end{document}
```

当然，除了为文本内容创建盒子之外，`\fbox`命令也能为图片等非文本内容创建盒子。

【**例9-34**】在`beamer`文档类型中使用`figure`环境插入三张图片，并使用`\fbox{}`命令将三种图片装入一个盒子中。

```tex
\documentclass{beamer}

\begin{document}

\begin{frame}

\begin{figure}
\centering
\fbox{
\includegraphics[width=0.2\linewidth]{redflower.png}
\includegraphics[width=0.2\linewidth]{yellowflower.png}
\includegraphics[width=0.2\linewidth]{blueflower.png}
}
\caption{Here is a figure box.}
\end{figure}

\end{frame}

\end{document}
```

编译上述代码，得到幻灯片如图9.3.5所示。

<p align="center">
<img align="middle" src="latex/chapter-9/graphics/NEWexample08.png" width="450">
</p>

<center><b>图9.3.5</b> 编译后的幻灯片效果</center>


#### （2）调用`fancybox`宏包

在`fancybox`宏包中，提供了以下四个命令用来创建不同样式的盒子：

+ `\shadowbox{}`：创建阴影盒子；

+ `\doublebox{}`：创建两重线盒子；

+ `\ovalbox{}`：创建细边线椭圆盒子；

+ `\Ovalbox{}`：创建粗边线椭圆盒子。

【**例9-35**】在`beamer`文档类型中使用`\shadowbox`，`\doublebox`，`\ovalbox`和`Ovalbox`命令创建不同样式的盒子。

```tex
\documentclass{beamer}
\usepackage{fancybox}
\begin{document}

\begin{frame}

\setlength{\fboxsep}{5pt}
\setlength{\fboxrule}{2pt}

\shadowbox{This is a shadowbox.}

\vskip 5mm

\doublebox{This is a doublebox.}

\vskip 5mm

\ovalbox{This is an ovalbox.}

\vskip 5mm

\Ovalbox{This is an Ovalbox.}

\end{frame}

\end{document}
```

编译上述代码，得到幻灯片如图9.3.6所示。

<p align="center">
<img align="middle" src="latex/chapter-9/graphics/NEWexample09.png" width="450">
</p>

<center><b>图9.3.6</b> 编译后的幻灯片效果</center>

类似地，也可以使用上述命令为图片等非文本元素创建不同样式的盒子。

【**例9-36**】在`beamer`文档类型中使用`figure`环境插入四张图片，使用`\shadowbox`，`\doublebox`，`\ovalbox`和`Ovalbox`命令分别为每张图片创建盒子，并使用`\parbox`命令把图片和标题均包含在盒子中。

```tex
\documentclass{beamer}
\usepackage{fancybox}
\begin{document}

\setlength{\fboxsep}{5pt}
\setlength{\fboxrule}{2pt}

\begin{frame}
\begin{figure}
\centering
\shadowbox{
\parbox[c][6cm][t]{5cm}{
\includegraphics[width=1\linewidth]{redflower.png}
\caption{A red flower.}}}
\end{figure}
\end{frame}

\begin{frame}
\begin{figure}
\centering
\doublebox{
\parbox[c][6cm][t]{5cm}{
\includegraphics[width=1\linewidth]{yellowflower.png}
\caption{A yellow flower.}}}
\end{figure}
\end{frame}

\begin{frame}
\begin{figure}
\centering
\ovalbox{
\parbox[c][6cm][t]{5cm}{
\includegraphics[width=1\linewidth]{blueflower.png}
\caption{A blue flower.}}}
\end{figure}
\end{frame}

\begin{frame}
\begin{figure}
\centering
\Ovalbox{
\parbox[c][6cm][t]{5cm}{
\includegraphics[width=1\linewidth]{magentaflower.png}
\caption{A magenta flower.}}}
\end{figure}
\end{frame}

\end{document}
```

编译上述代码，得到幻灯片如图9.3.7所示。

<p align="center">
<table>
<tr>
<td><img align="middle" src="latex/chapter-9/graphics/NEWexample11_1.png" width="450"></td>
<td><img align="middle" src="latex/chapter-9/graphics/NEWexample11_2.png" width="450"></td>
</tr>
<tr>
<td><img align="middle" src="latex/chapter-9/graphics/NEWexample11_3.png" width="450"></td>
<td><img align="middle" src="latex/chapter-9/graphics/NEWexample11_4.png" width="450"></td>
</tr>
</table>
</p>

<center><b>图9.3.7</b> 编译后的幻灯片效果</center>



【回放】[**9.2 添加动画效果**](https://nbviewer.jupyter.org/github/xinychen/latex-cookbook/blob/main/chapter-9/section2.ipynb)

【继续】[**9.4 设置主题样式**](https://nbviewer.jupyter.org/github/xinychen/latex-cookbook/blob/main/chapter-9/section4.ipynb)

### License

<div class="alert alert-block alert-danger">
<b>This work is released under the MIT license.</b>
</div>
