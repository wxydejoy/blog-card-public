## 9.2 添加动画效果

在制作幻灯片时有时需要添加动画效果。由于LaTeX制作幻灯片会被编译成PDF文档，因此，在Beamer中，实现动画效果的方式是将具有动画内容的幻灯片按照次序拆分成若干页内容，在播放时通过翻页达到“动态”视觉效果。为了便于说明，以下将一个`frame`环境创建的内容称为一页幻灯片或幻灯片页、将动画效果拆分后得到的每一页内容称为该幻灯片的某一帧。

下面介绍在Beamer中常见的几种动画效果命令。

### 9.2.1 `\pause`命令

`\pause`是Beamer中最常用的一种动画效果命令，它的使用方式极其简单，通过在文本或段落中添加`\pause`命令，便可将一页幻灯片拆分成若干帧。一般来说，`\pause`命令后的内容将会在下一帧中显示，从而使幻灯片在内容显示上呈现出动画效果。比如，一般情况下，使用列表环境创建的每项内容（使用`\item`创建）都会在同一帧幻灯片中显示，为了达到各项内容逐个显示的动画效果，可以在两个相邻的`\item`语句之间插入`\pause`命令。

【**例9-11**】在`beamer`文档类型中使用`\pause`命令实现一个简单的动画效果。

```tex
\documentclass{beamer}
\usefonttheme{professionalfonts}

\begin{document}

\begin{frame}
\frametitle{Parent function}
\framesubtitle{A short list}

Please check out the following parent function list.
\begin{enumerate}
\item $y=x$
\pause
\item $y=|x|$
\pause
\item $y=x^{2}$
\pause
\item $y=x^{3}$
\pause
\item $y=x^{b}$
\end{enumerate}
\end{frame}

\end{document}
```

编译上述代码，得到幻灯片如图9.2.1所示。

<p align="center">
<table>
<tr>
<td><img align="middle" src="latex/chapter-9/graphics/example6_1.png" width="450"></td>
<td><img align="middle" src="latex/chapter-9/graphics/example6_2.png" width="450"></td>
</tr>
<tr>
<td><img align="middle" src="latex/chapter-9/graphics/example6_3.png" width="450"></td>
<td><img align="middle" src="latex/chapter-9/graphics/example6_4.png" width="450"></td>
</tr>
<tr>
<td><img align="middle" src="latex/chapter-9/graphics/example6_5.png" width="450"></td>
</tr>
</table>
</p>

<center><b>图9.2.1</b> 编译后的幻灯片效果</center>

### 9.2.2 `\item<>`命令

对于列表环境中的各项内容，也可以通过设置选项指定在该幻灯片的哪些步骤中显示该项内容，从而更加灵活地定制动画效果。具体是使用`\item<>`命令，其中`<>`用于指定显示步骤，对于没有指定`<>`显示范围的内容项默认会在所有幻灯片页面中显示。具体而言，`<>`中的内容存在以下四种格式：

+ `<A,B,C>`：表示内容项将在第A、B、C步中显示。如，`\item<2, 3, 4> $y=x^{2}$`表示该项内容将出现在该页幻灯片放映的第2、3、4步；

+ `<A-B>`：表示内容项将在第A至B步中显示。如，`\item<1-4> $y=x$`表示该项内容将出现在该页幻灯片放映的第1~4步；

+ `<A->`：表示内容项将在第A步及以后显示。如，`\item<2-> $y=x$`表示该项内容将出现在该页幻灯片放映的第2步及之后的步骤中；

+ `<-A>`：表示内容项将在第A步及之前显示。如，`\item<-3> $y=x$`表示该项内容将出现在该页幻灯片放映的第3步及之前的步骤中。

由此创建的一张幻灯片将包含多帧，其帧数由所有`\item<>`命令中设置的最大步骤决定。

如果想要在某一帧中突出某项内容，主要包括以下两种方式：

- 使用`\alert`命令为该项内容指定需要高亮显示的步骤。具体用法如：`\item<2-| alert@3-4> The second item.`，此时内容项“The second item.”将出现在第2步之后的步骤中，并通过命令`\alert`及前缀`@`使其在第3~4步中高亮显示。

【**例9-12**】在`beamer`文档类型中使用`\item<>`定制内容显示范围并使用`\alert`对内容项进行高亮显示，从而实现一个简单的动画效果。

```tex
\documentclass{beamer}
\usefonttheme{professionalfonts}

\begin{document}

\begin{frame}
\frametitle{Parent function}
\framesubtitle{A short list}

Please check out the following parent function list.
\begin{enumerate}
\item<1-| alert@1> $y=x$
\item<2-| alert@2> $y=|x|$
\item<3-| alert@3> $y=x^{2}$
\item<4-| alert@4> $y=x^{3}$
\end{enumerate}

\end{frame}

\end{document}
```

编译上述代码，得到幻灯片如图9.2.2所示。

<p align="center">
<table>
<tr>
<td><img align="middle" src="latex/chapter-9/graphics/NEWexample7_1.png" width="450"></td>
<td><img align="middle" src="latex/chapter-9/graphics/NEWexample7_2.png" width="450"></td>
</tr>
<tr>
<td><img align="middle" src="latex/chapter-9/graphics/NEWexample7_3.png" width="450"></td>
<td><img align="middle" src="latex/chapter-9/graphics/NEWexample7_4.png" width="450"></td>
</tr>
</table>
</p>

<center><b>图9.2.2</b> 编译后的幻灯片效果</center>

- 使用`\color<范围>{显示颜色}`命令改变内容项的颜色。如`\item<1-> \color<1>{red} The first item.`语句，内容`The first item.`将出现在第一步及之后的步骤中，通过`\color<1>{red}`令该项内容在第一步显示颜色为红色，而在其它步骤中仍为默认颜色。如下例所示，编译得到的效果与上图9.2.2一致：

【**例9-13**】在`beamer`文档类型中使用`\item<>`定制内容显示范围并使用`\color<>{}`对内容项进行高亮显示。

```tex
\documentclass{beamer}
\usefonttheme{professionalfonts}

\begin{document}

\begin{frame}
\frametitle{Parent function}
\framesubtitle{A short list}

Please check out the following parent function list.
\begin{enumerate}
\item<1-> \color<1>{red} $y=x$
\item<2-> \color<2>{red} $y=|x|$
\item<3-> \color<3>{red} $y=x^{2}$
\item<4-> \color<4>{red} $y=x^{3}$
\end{enumerate}

\end{frame}

\end{document}
```

### 9.2.3 其它命令

LaTeX还提供了其它命令可以实现类似的动画效果，同样可以在可选参数`<>`中指定内容项或内容块的显示范围，主要包括`\onslide`、`\uncover`、`\only`、`\visible`、`\invisible`等命令：

+ `\onslide<>{}`：该命令可以指定内容在当前幻灯片页放映的第几步显示。使用该命令时不显示的内容将被“遮挡”，仍将占用其指定的位置（`\uncover<>{}`或`\visible<>{}`也能实现类似效果）；

    【**例9-14**】在`beamer`文档类型中使用`\onslide<>{}`命令实现一个简单的动画效果。

    ```tex
    \documentclass{beamer}
    \usefonttheme{professionalfonts}

    \begin{document}

    \begin{frame}
    \frametitle{Parent function}
    \framesubtitle{A short list}

    \onslide<1->{Please check out the following parent function list.}

    \onslide<2,4>{1. $y=x$}

    \onslide<1-4>{2. $y=|x|$}

    \onslide<2->{3. $y=x^{2}$}

    \onslide<3->{4. $y=x^{3}$}

    \onslide<4>{5. $y=x^{b}$}

    \end{frame}

    \end{document}
    ```

    编译上述代码，得到幻灯片如图9.2.3所示。

    <p align="center">
    <table>
    <tr>
    <td><img align="middle" src="latex/chapter-9/graphics/NEWexample2_1.png" width="450"></td>
    <td><img align="middle" src="latex/chapter-9/graphics/NEWexample2_2.png" width="450"></td>
    </tr>
    <tr>
    <td><img align="middle" src="latex/chapter-9/graphics/NEWexample2_3.png" width="450"></td>
    <td><img align="middle" src="latex/chapter-9/graphics/NEWexample2_4.png" width="450"></td>
    </tr>
    </table>
    </p>

    <center><b>图9.2.3</b> 编译后的幻灯片效果</center>

+ `\only<>{}`：该命令可以指定内容在当前幻灯片页放映的第几步插入。使用该命令时，不显示的内容对应的位置将腾空出来，可以用于显示其它内容；

    【**例9-15**】在`beamer`文档类型中使用`\only<>{}`命令实现一个简单的动画效果。

    ```tex
    \documentclass{beamer}
    \usefonttheme{professionalfonts}

    \begin{document}

    \begin{frame}
    \frametitle{Parent function}
    \framesubtitle{A short list}

    \only<1->{Please check out the following parent function list.}

    \only<2,4>{1. $y=x$}

    \only<1-4>{2. $y=|x|$}

    \only<2->{3. $y=x^{2}$}

    \only<3->{4. $y=x^{3}$}

    \only<4>{5. $y=x^{b}$}

    \end{frame}

    \end{document}
    ```

    编译上述代码，得到幻灯片如图9.2.4所示。

    <p align="center">
    <table>
    <tr>
    <td><img align="middle" src="latex/chapter-9/graphics/NEWexample3_1.png" width="450"></td>
    <td><img align="middle" src="latex/chapter-9/graphics/NEWexample3_2.png" width="450"></td>
    </tr>
    <tr>
    <td><img align="middle" src="latex/chapter-9/graphics/NEWexample3_3.png" width="450"></td>
    <td><img align="middle" src="latex/chapter-9/graphics/NEWexample3_4.png" width="450"></td>
    </tr>
    </table>
    </p>

    <center><b>图9.2.4</b> 编译后的幻灯片效果</center>

+ `\invisible<>{}`：该命令的作用效果与`\visible<>{}`相反，用于指定内容在当前幻灯片页放映的第几步不可见。但与`\visible<>{}`相同的是，使用`\invisible<>{}`命令时，不可见的内容仍占据着对应的位置，不可用于显示其它内容。如下例中的代码所示，编译后得到的效果与图9.1.8一致。

    【**例9-16**】在`beamer`文档类型中使用`\invisible<>{}`命令实现一个简单的动画效果。

    ```tex
    \documentclass{beamer}
    \usefonttheme{professionalfonts}

    \begin{document}

    \begin{frame}
    \frametitle{Parent function}
    \framesubtitle{A short list}

    \visible<1-4>{Please check out the following parent function list.}

    \invisible<1,3>{1. $y=x$}

    \invisible<>{2. $y=|x|$}

    \invisible<1>{3. $y=x^{2}$}

    \invisible<1-2>{4. $y=x^{3}$}

    \invisible<1-3>{5. $y=x^{b}$}

    \end{frame}

    \end{document}
    ```

### 9.2.4 自动计数

上述介绍的动画效果定制命令均通过在`<>`中指定具体的数字指定内容显示范围。此时，如果想要在开始处或中间插入新的内容项，则其余所有内容项的`<>`显示范围都必须作出相应调整，显然不够灵活。LaTeX提供了一种更巧妙的方式可以解决这类问题：使用“+”号代替具体数字，从1开始进行自动递增计数。就例9-13而言，可以用“+”符号代替各`<>`中的具体数字，可以得到完全相同的编译效果。修改后的语句如下：

【**例9-17**】在`beamer`文档类型中使用`+`符号灵活定制幻灯片效果。

```tex
\documentclass{beamer}
\usefonttheme{professionalfonts}

\begin{document}

\begin{frame}
\frametitle{Parent function}
\framesubtitle{A short list}

Please check out the following parent function list.
\begin{enumerate}
\item<+-| alert@+> $y=x$  % 此时“+”号对应数字1
\item<+-| alert@+> $y=|x|$  % 此时“+”号对应数字2
\item<+-| alert@+> $y=x^{2}$  % 此时“+”号对应数字3
\item<+-| alert@+> $y=x^{3}$  % 此时“+”号对应数字4
\end{enumerate}

\end{frame}

\end{document}
```

上述语句每一条`\item`格式相同，因此也可以简写为如下语句：

```tex
\documentclass{beamer}
\usefonttheme{professionalfonts}

\begin{document}

\begin{frame}
\frametitle{Parent function}
\framesubtitle{A short list}

Please check out the following parent function list.
\begin{enumerate}[<+-| alert@+>]
\item $y=x$
\item $y=|x|$
\item $y=x^{2}$
\item $y=x^{3}$
\end{enumerate}

\end{frame}

\end{document}
```

有时在`<>`中使用的数字不总是从1开始递增，那么就需要使用“+(偏移量)”的命令格式。比如，如果当前“+”号对应的计数器值为3，那么`<+(2)->`意味着在当前计数器值的基础上加2，`<+(-2)->`则意味着在当前计数器值的基础上减2。

【**例9-18**】在`beamer`文档类型中使用`+(偏移量)`符号灵活定制任意显示步骤的幻灯片效果。

```tex
\documentclass{beamer}
\usefonttheme{professionalfonts}

\begin{document}

\begin{frame}
\frametitle{Parent function}
\framesubtitle{A short list}

Please check out the following parent function list.
\begin{enumerate}
\item<+(1)-> $y=x$  % 相当于`\item<2-> $y=x$`
\item<-+(2)> $y=|x|$  % 相当于`\item<-4> $y=|x|$`
\item<+(-1)-+(1)> $y=x^{2}$  % 相当于`\item<2-4> $y=x^{2}$`
\item<+(-1)> $y=x^{3}$  % 相当于`\item<3> $y=x^{3}$`
\end{enumerate}

\end{frame}

\end{document}
```

编译上述代码，得到幻灯片如图9.2.5所示。

<p align="center">
<table>
<tr>
<td><img align="middle" src="latex/chapter-9/graphics/NEWexample10_1.png" width="450"></td>
<td><img align="middle" src="latex/chapter-9/graphics/NEWexample10_2.png" width="450"></td>
</tr>
<tr>
<td><img align="middle" src="latex/chapter-9/graphics/NEWexample10_3.png" width="450"></td>
<td><img align="middle" src="latex/chapter-9/graphics/NEWexample10_4.png" width="450"></td>
</tr>
</table>
</p>

<center><b>图9.2.5</b> 编译后的幻灯片效果</center>

【回放】[**9.1 基本介绍**](https://nbviewer.jupyter.org/github/xinychen/latex-cookbook/blob/main/chapter-9/section1.ipynb)

【继续】[**9.3 块与盒子——添加框元素**](https://nbviewer.jupyter.org/github/xinychen/latex-cookbook/blob/main/chapter-9/section3.ipynb)

### License

<div class="alert alert-block alert-danger">
<b>This work is released under the MIT license.</b>
</div>