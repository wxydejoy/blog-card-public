## 9.8 插入与调整图片

在制作幻灯片时经常需要插入图片以辅助演讲汇报，对此，Beamer提供了相关宏包及命令可以支持在幻灯片中插入图片并对其进行一系列操作，包括编辑图片、插入子图、调整排列方式、调整布局方式、设置背景图片、在标题页中插入图片、添加动画效果等。

### 9.8.1 插入图片

类似于article文档中插入图片操作，在Beamer中可以基于`\begin{figure} \end{figure}`环境、并使用`\includegraphics[图片参数]{图片名或图片路径}`命令为幻灯片插入图片、以及设置height、width、angle等参数。不同之处主要在于：

- Beamer文档类自带graphicx工具包，因此可以省略声明语句`\usepackage{graphicx}`；

- 在Beamer中浮动图形位置参数h、t、b、p无效，因此需要使用其它方式调整图片位置；

- 在Beamer中使用`\caption{}`命令仅创建图片标题，而不再为图片进行自动编号。为此，需要在导言区额外添加声明语句`\setbeamertemplate{caption}[numbered]`，表示对演示稿中的图片进行自动编号。

【**例9-51**】在`beamer`文档类型中使用`\begin{figure} \end{figure}`环境以及`\includegraphics`命令插入图片，并添加声明`\setbeamertemplate{caption}[numbered]`使得图片进行自动编号。

```tex
\documentclass{beamer}
% 使图片进行自动编号
\setbeamertemplate{caption}[numbered]

\begin{document}

\begin{frame}{Two pictures}
\begin{figure}
\centering
    % 插入第一张图片并设置标题、索引标签
    \includegraphics[width=0.2\linewidth]{blueflower.png}
    \caption{First figure.}
    \label{fig:figlabel1}
    % 插入第二张图片并设置标题、索引标签
    \includegraphics[width=0.2\linewidth]{yellowFlower.png}
    \caption{Second figure.}
    \label{fig:figlabel2}
\end{figure}
\end{frame}

\end{document}
```

编译上述代码，得到的幻灯片如图9.8.1所示。

<p align="center">
<img align="middle" src="latex/chapter-9/graphics/eg6_1new.png" width="450">
</p>

<center><b>图9.8.1</b> 编译后的幻灯片效果</center>

### 9.8.2 编辑图片

读者可以通过修改Beamer主题选项从而为演示稿定制图片标题样式，包括：

- `\setbeamerfont{caption}{size=定制的字体大小}`：设置图片标题的字体大小，如设置为\small、\large、\Large等；

- `\setbeamercolor{caption}{fg=定制的颜色}`：设置图片标题编号的颜色，如设置为red、blue等；

- `\setbeamercolor{caption name}{fg=定制的颜色}`：设置图片标题内容的颜色，如设置为red、blue等。

读者还可以改变图片的不透明度。为此，首先需要调用tikz宏包，使用语句`\usepackage{tikz}`即可；然后将插入的图片作为一个节点`\node`放置到`tikzpicture`环境内，并使用`\node[opacity=定制的不透明度]`语句设置不透明度选项参数，如下所示：
```tex
\begin{tikzpicture}
    \node[opacity=定制的不透明度]{\includegraphics[width=0.3\textwidth]{图片路径}};   
\end{tikzpicture}
```

【**例9-52**】在`beamer`文档类型中使用`\setbeamerfont{caption}`、`\setbeamercolor{caption}`和`\setbeamercolor{caption name}`命令修改图片标题样式；并调用tikz宏包，使用`tikzpicture`环境和`\node`命令设置图片不透明度。

```tex
\documentclass{beamer}
\usepackage{tikz}
\setbeamertemplate{caption}[numbered]
% 定制图片标题样式
\setbeamerfont{caption}{size=\large}
\setbeamercolor{caption name}{fg=red}
\setbeamercolor{caption}{fg=blue}

\begin{document}

\begin{frame}{Two pictures}

\begin{figure}
\centering
    % 插入第一张图片并设置标题、创建索引标签
    \begin{tikzpicture}
    \node[opacity=0.3]
    {\includegraphics[width=0.2\linewidth]{blueflower.png}};   
    \end{tikzpicture}
    \caption{First figure.}
    \label{fig:figlabel1}
    % 插入第二张图片并设置图片不透明度、设置标题、创建索引标签
    \begin{tikzpicture}
    \node[opacity=0.3]
    {\includegraphics[width=0.2\linewidth]{yellowflower.png}};   
    \end{tikzpicture}
    \caption{Second figure.}
    \label{fig:figlabel2}
\end{figure}

\end{frame}

\end{document}
```

编译上述代码，得到的幻灯片如图9.8.2所示。

<p align="center">
<img align="middle" src="latex/chapter-9/graphics/eg6_2new.png" width="450">
</p>

<center><b>图9.8.2</b> 编译后的幻灯片效果</center>


### 9.8.3 插入子图

有时需要在Beamer中插入子图，用到的宏包与命令与article文档情况类似。读者可以只需要使用语句`\usepackage{subcaption}`调用subcaption宏包，并在`figure`环境中创建多个`subfigure`环境，每个`subfigure`环境内都可以进行插入子图、设置子图标题和标签等操作。下面来看一个具体的例子：

【**例9-53**】在`beamer`文档类型中，调用subcaption宏包，并使用`figure`环境中的`subfigure`环境创建子图。

```tex
\documentclass{beamer}
% 调用关键宏包subcaption
\usepackage{subcaption}
\setbeamertemplate{caption}[numbered]

\begin{document}

\begin{frame}{Two sub-figures}
\begin{figure}
\centering
    % 插入第一张子图
    \begin{subfigure}{0.4\linewidth}
        \centering
        \includegraphics[width=0.5\linewidth]{blueflower.png}
        \caption{First subfigure.}
        \label{fig:subfiglabel1}
    \end{subfigure}
    % 插入第二张子图
    \begin{subfigure}{0.4\linewidth}
        \centering
        \includegraphics[width=0.5\linewidth]{yellowFlower.png}
        \caption{Second subfigure.}
        \label{fig:subfiglabel2}
    \end{subfigure}
\caption{A figure contains two sub-figures.}
\label{fig:figlabel}
\end{figure}
\end{frame}

\end{document}
```

编译上述代码，得到的幻灯片如图9.8.3所示。

<p align="center">
<img align="middle" src="latex/chapter-9/graphics/eg6_3.png" width="450">
</p>

<center><b>图9.8.3</b> 编译后的幻灯片效果</center>

### 9.8.4 调整排列方式

使用`\centering`命令可以将图片放置到整个幻灯片页面的中央，但有时需要对图片的排列位置进行更多样化的调整。

#### （1）横向分布与纵向分布

使用`\hfill`、`\vfill`命令可以分别控制图片的水平间距和垂直间距。在同一行中，每个`\hfill`产生的间隔是相同的，从而达到将多个图片横向等间距分布的效果；类似地，`\vfill`命令可以实现纵向等间距分布的效果。下面以一个例子对此进行说明：

【**例9-54**】在`beamer`文档类型中，使用`\hfill`命令实现图片横向分布，以及使用`\vfill`命令实现图片纵向分布。

```tex
\documentclass{beamer}

\begin{document}
% 实现图片横向分布
\begin{frame}{Three pictures with the same lateral distance}
\begin{figure}
\includegraphics[width=0.2\linewidth]{redflower.png}
\hfill
\includegraphics[width=0.2\linewidth]{blueflower.png}   
\hfill
\includegraphics[width=0.2\linewidth]{yellowflower.png}
\end{figure}
\end{frame}
\begin{frame}{Three pictures with the same longitudinal distance}
% 实现图片纵向分布
\begin{figure}
\includegraphics[width=0.2\linewidth]{redflower.png}
\vfill
\includegraphics[width=0.2\linewidth]{blueflower.png}   
\vfill
\includegraphics[width=0.2\linewidth]{yellowflower.png}
\end{figure}
\end{frame}

\end{document}
```

编译上述代码，得到的幻灯片如图9.8.4所示。

<p align="center">
<table>
<tr>
<td><img align="middle" src="latex/chapter-9/graphics/eg6_4_1.png" width="450"></td>
<td><img align="middle" src="latex/chapter-9/graphics/eg6_4_2.png" width="450"></td>
</tr>
</table>
</p>

<center><b>图9.8.4</b> 编译后的幻灯片效果</center>

#### （2）并排显示

在幻灯片中，将不同内容（图片、文本、表格、公式等）并排分栏显示是一种常用的展示方式。前面我们介绍了使用`\hfill`命令实现多个图片并排显示的方式，这里我们接着介绍一种更通用的方式，不仅可以实现图片的并排显示，也可以实现文本等其它内容的并排显示。为此，需要使用`\begin{columns} \end{columns}`环境，并嵌套多个`\begin{column} \end{column}`环境对内容进行分栏，每个`column`环境中的内容都独立成栏，不同栏的内容并排显示。

【**例9-55**】在`beamer`文档类型中，使用`columns`环境创建多列内容实现并排显示效果。

```tex
\documentclass{beamer}

\begin{document}
\begin{frame}{Frame1}

\begin{columns}
% 创建第一列
\begin{column}{0.4\linewidth}
    Here is a description for the blue flower on the right. Here is a description for the blue flower on the right.
\end{column}
% 创建第二列   
\begin{column}{0.4\linewidth}
    \begin{figure}
    \centering
        \includegraphics[width=0.7\linewidth]{blueflower.png}
        \caption{A blue flower.}
    \end{figure}
\end{column}
\end{columns}

\end{frame}

\end{document}
```

编译上述代码，得到的幻灯片如图9.8.5所示。

<p align="center">
<img align="middle" src="latex/chapter-9/graphics/eg6_5.png" width="450">
</p>

<center><b>图9.8.5</b> 编译后的幻灯片效果</center>

#### （3）设置任意图片位置

通过调用tikz宏包及其命令可以为图片指定任意摆放位置。首先使用`\usepackage{tikz}`语句调用tikz宏包，然后调用如下所示的语句：

```tex
\begin{tikzpicture}[remember picture, overlay]
    \node[锚点位置偏移量] at (current page.锚点位置) 
    {
        \includegraphics{图片路径}
    };
\end{tikzpicture}
```

上述示例语句中，包括：

- 在幻灯片中创建`tikzpicture`环境，使用`\node`命令创建一个内容为插入图片的节点；

- 设置`\begin{tikzpicture}[]`的选项为`remember picture, overlay`，从而允许自由放置图片；

- 通过使用`\node[] at ()`语句指定图片摆放位置：

    - 1）`()`中用于设置图片的锚点位置或摆放位置，设置格式为`current page.锚点位置`。在锚点位置设置上：一种方式是使用描述性语言，如`current page.center`表示将图片放在页面正中央、`current page.east`表示将图片放在页面边缘的右方（正东方向）、`current page.north east`表示将图片放在页面边缘的右上方（东北方向），以此类推；另一种方式是使用相对于页面正东方向的逆时针角度，如`current page.0`表示将图片放在页面边缘右方、`current page.45`表示将图片放在页面边缘右上方、`current page.-90`表示将图片放在页面边缘下方；
    
    - 2）`[]`中用于设置锚点位置的偏移量。一种方式是使用描述性语言，包括left、right、above、below，分别表示将图片相对于锚点位置往左、右、上、下偏移，如`\node[left=1cm,above=2cm] at (current page.center)`表示将图片位置设置为页面正中央往左偏移1cm、往上偏移2cm的位置；另一种方式是使用偏移坐标参数`xshift`和`yshift`，如`\node[xshift=-1cm,yshift=2cm] at (current page.center)`的效果等价于`\node[left=1cm,above=2cm] at (current page.center)`。

【**例9-56**】在`beamer`文档类型中，使用`tikzpicture`环境创建以插入的图片作为内容的节点，为`\begin{tikzpicture}`设置选项`remember picture, overlay`，并使用`\node[] at ()`语句设置图片的摆放位置。

```tex
\documentclass{beamer}
% 调用tikz宏包
\usepackage{tikz}

\begin{document}
% 第一页幻灯片
\begin{frame}{Frame1}
% 创建tikzpicture环境，并使用描述性语言设置锚点位置
\begin{tikzpicture}[remember picture, overlay]
    % 将图片放置到幻灯片页中央
    \node at (current page.center) 
    {
        \includegraphics[width=0.2\linewidth]{blueflower.png}
    };
    % 将图片放置到幻灯片页的右边（正东方向）
    \node at (current page.east) 
    {
        \includegraphics[width=0.2\linewidth]{blueflower.png}
    };
    % 将图片放置到幻灯片页的下方（正南方向）
    \node at (current page.south) 
    {
        \includegraphics[width=0.2\linewidth]{blueflower.png}
    };
    % 将图片放置到幻灯片页的左边（正西方向）
    \node at (current page.west) 
    {
        \includegraphics[width=0.2\linewidth]{blueflower.png}
    };
    % 将图片放置到幻灯片页的上方（正北方向）
    \node at (current page.north) 
    {
        \includegraphics[width=0.2\linewidth]{blueflower.png}
    };
\end{tikzpicture}
\end{frame}
% 第二页幻灯片
\begin{frame}{Frame2}
% 创建tikzpicture环境，并使用角度设置锚点位置、使用描述性语言设置锚点偏移量
\begin{tikzpicture}[remember picture, overlay]
    % 将图片放置到幻灯片页的右边，并往左偏移0.5cm
    \node[left=0.5cm] at (current page.0) 
    {
        \includegraphics[width=0.2\linewidth]{blueflower.png}
    };
    % 将图片放置到幻灯片页的下方，并往上偏移0.5cm
    \node[above=0.5cm] at (current page.-90) 
    {
        \includegraphics[width=0.2\linewidth]{blueflower.png}
    };
    % 将图片放置到幻灯片页的左边，并往右偏移0.5cm
    \node[right=0.5cm] at (current page.180) 
    {
        \includegraphics[width=0.2\linewidth]{blueflower.png}
    };
    % 将图片放置到幻灯片页的上方，并往下偏移0.5cm
    \node[below=0.5cm] at (current page.90) 
    {
        \includegraphics[width=0.2\linewidth]{blueflower.png}
    };
\end{tikzpicture}
\end{frame}

\end{document}
```

编译上述代码，得到的幻灯片如图9.8.6所示。

<p align="center">
<table>
<tr>
<td><img align="middle" src="latex/chapter-9/graphics/eg6_6new_1.png" width="450"></td>
<td><img align="middle" src="latex/chapter-9/graphics/eg6_6new_2.png" width="450"></td>
</tr>
</table>
</p>

<center><b>图9.8.6</b> 编译后的幻灯片效果</center>

### 9.8.5 调整布局方式

在幻灯片中，常见的图文布局方式有两种：文字环绕于图片、文字浮于图片上方。下面分别展开介绍。

#### （1）文字环绕图片

为了实现文字环绕图片的显示效果，首先需要使用`\usepackage{wrapfig}`语句调用wrapfig宏包，并创建`\begin{wrapfigure} \end{wrapfigure}`环境插入图片，在`wrapfigure`环境后面输入环绕文本内容，由此创建的文本内容将环绕于插入的图片周围。其中，`wrapfigure`环境与我们熟悉的`figure`环境类似，同样可以使用`\includegraphics`、`\caption`等语句实现相关功能。在`\begin{wrapfigure}{}`语句的`{}`中可以设置图片位置参数，参数选项为r或l，分别表示将图片设置为页面右侧或左侧。

【**例9-57**】在`beamer`文档类型中，使用`wrapfigure`环境插入图片并设置图片位置为页面右侧，实现文字环绕图片的效果。

```tex
\documentclass{beamer}
% 调用wrapfig宏包
\usepackage{wrapfig}

\begin{document}
\begin{frame}{Frame1}
% 创建wrapfigure环境并插入图片
\begin{wrapfigure}{r}{0.5\linewidth}
    \centering
    \includegraphics[width=0.5\linewidth]{blueflower.png}
    \caption{A blue flower.}
\end{wrapfigure}
% 示意性环绕文本
Here is a description for the picture. Here is a description for the picture. Here is a description for the picture. Here is a description for the picture. Here is a description for the picture. Here is a description for the picture. Here is a description for the picture. Here is a description for the picture. Here is a description for the picture. Here is a description for the picture. Here is a description for the picture. Here is a description for the picture.
\end{frame}

\end{document}
```

编译上述代码，得到的幻灯片如图9.8.7所示。

<p align="center">
<img align="middle" src="latex/chapter-9/graphics/eg6_7.png" width="450">
</p>

<center><b>图9.8.7</b> 编译后的幻灯片效果</center>


#### （2）文字浮于图片上方

图片浮于文字上方是另一种常用的图文布局方式。为此，读者需要使用`\usepackage{tikz}`语句调用tikz宏包，在`tikzpicture`环境中使用`\node`命令创建一个内容为插入图片的节点、一个内容为文本的节点，并将文本节点的位置设为图片节点的中央。

【**例9-58**】在`beamer`文档类型中，使用`tikzpicture`环境创建一个内容为插入图片的节点、一个内容为文本的节点，并设置第一个节点的名称和图片透明度、第二个节点的文本样式和位置。

```tex
\documentclass{beamer}
% 调用tikz宏包
\usepackage{tikz}

\begin{document}
\begin{frame}{Frame1}

\begin{tikzpicture}
% 创建一个内容为图片的节点，节点名为myfirstfigure
\node(myfirstfigure)[opacity=0.4]
{
    \includegraphics[width=0.3\linewidth]{greyflower.png}
    \includegraphics[width=0.3\linewidth]{greyflower.png}
    \includegraphics[width=0.3\linewidth]{greyflower.png}
};
% 创建一个内容为文本的节点
\node
[ 
    text=teal,
    font={\huge\bfseries}
] at (myfirstfigure.center) {Text over the picture!};
\end{tikzpicture}

\end{frame}

\end{document}
```

编译上述代码，得到的幻灯片如图9.8.8所示。

<p align="center">
<img align="middle" src="latex/chapter-9/graphics/eg6_8.png" width="450">
</p>

<center><b>图9.8.8</b> 编译后的幻灯片效果</center>

### 9.8.6 设置背景图片

在Beamer中可以很方便地为演示稿设置全局或局部的背景图片，通过使用`\setbeamertemplate{background canvas}{插入背景图片}`语句设置背景画布选项即可。

【**例9-59**】在`beamer`文档类型中，`\setbeamertemplate{background canvas}{插入背景图片}`语句设置全局及局部背景画布选项。

```tex
\documentclass{beamer}
\usetheme{AnnArbor}

% 设置全局背景画布选项
\setbeamertemplate{background canvas}
{
    \includegraphics[width=\paperwidth,height=\paperheight]{lines.png}%
}

\begin{document}
% 第一页幻灯片使用全局背景画布
\begin{frame}{Frame1}
\end{frame}
{
% 设置局部特定背景画布选项
\setbeamertemplate{background canvas}
{
    \includegraphics[width=\paperwidth,height=\paperheight]{AI.png}%
}
% 第二页幻灯片使用局部特定背景画布
\begin{frame}{Frame2}
\end{frame}
}
% 第三页幻灯片使用全局背景画布
\begin{frame}{Frame3}
\end{frame}
% 第四页幻灯片使用全局背景画布
\begin{frame}{Frame4}
\end{frame}
\end{document}
```

编译上述代码，得到的幻灯片如图9.8.9所示。

<p align="center">
<table>
<tr>
<td><img align="middle" src="latex/chapter-9/graphics/eg6_9_1.png" width="450"></td>
<td><img align="middle" src="latex/chapter-9/graphics/eg6_9_2.png" width="450"></td>
</tr>
<tr>
<td><img align="middle" src="latex/chapter-9/graphics/eg6_9_3.png" width="450"></td>
<td><img align="middle" src="latex/chapter-9/graphics/eg6_9_4.png" width="450"></td>
</tr>
</table>
</p>

<center><b>图9.8.9</b> 编译后的幻灯片效果</center>

如上例所示，为了让插入的图片充满整个页面，应使用`width=\paperwidth`和`height=\paperheight`选项；修改局部特定背景画布时，应用`{}`符号将`\setbeamertemplate`语句及其作用的局部`frame`环境放在一起。

### 9.8.7 在标题页中插入图片

在前面的章节中我们介绍了在Beamer中使用`\titlepage`命令创建标题页的语句。事实上，除了可以在标题页中添加标题名称、作者、机构单位等信息之外，在标题页中添加图片或图标也是一种常见的操作。为此，只需要在标题页信息中添加`\titlegraphic{插入图片}`命令即可，如下例所示：

【**例9-60**】在`beamer`文档类型中，使用`\titlegraphic{插入图片}`命令为标题页插入图片，并使用`\titlepage`命令创建标题页。

```tex
\documentclass{beamer}
\usetheme{AnnArbor}

\begin{document}

\title{A presentation about AI}
\author{The author's name}
\institute{The institute's name}
\date{2021/1/1}
% 在标题页中添加图片
\titlegraphic
{
    \includegraphics[width=2cm]{robot.png}
}
\begin{frame}
    \titlepage
\end{frame}

\end{document}
```

编译上述代码，得到的幻灯片如图9.8.10所示。

<p align="center">
<img align="middle" src="latex/chapter-9/graphics/eg6_10.png" width="450">
</p>

<center><b>图9.8.10</b> 编译后的幻灯片效果</center>

此外，可以结合前面介绍的tikz宏包及其命令将图片调整到更合适的位置。

【**例9-61**】在`beamer`文档类型中，使用`\titlegraphic{插入图片}`命令为标题页插入图片，并在`tikzpicture`环境中使用`\node`命令调整图片位置为右下方。

```tex
\documentclass{beamer}
% 调用tikz宏包
\usepackage{tikz}
\usetheme{AnnArbor}

\begin{document}

\title{A presentation about AI}
\author{The author's name}
\institute{The institute's name}
\date{2021-8-30}
% 在标题页中添加图片并指定位置
\titlegraphic
{
    \begin{tikzpicture}[overlay, remember picture]
        \node[above=0.8cm] at (current page.-43){
        \includegraphics[width=1.5cm]{robot.png}
        };
    \end{tikzpicture}
}
\begin{frame}
    \titlepage
\end{frame}

\end{document}
```

编译上述代码，得到的幻灯片如图9.8.11所示。

<p align="center">
<img align="middle" src="latex/chapter-9/graphics/eg6_11.png" width="450">
</p>

<center><b>图9.8.11</b> 编译后的幻灯片效果</center>


### 9.8.8 添加动画效果

如果想要为图片添加动画效果，使得不同的图片分步显示，使用设置了显示范围选项的`\includegraphics<显示范围>{图片路径}`命令插入图片即可。

【**例9-62**】在`beamer`文档类型中使用`\includegraphics<>{}`命令插入多张图片并分步显示。

```tex
\documentclass{beamer}

\begin{document}

\begin{frame}

\includegraphics<1->[width=0.2\linewidth]{redflower.png}
\includegraphics<2->[width=0.2\linewidth]{yellowflower.png}
\includegraphics<3->[width=0.2\linewidth]{blueflower.png}

\end{frame}

\end{document}
```

编译上述代码，得到的幻灯片如图9.8.12所示。

<p align="center">
<table>
<tr>
<td><img align="middle" src="latex/chapter-9/graphics/NEWexample4_1.png" width="450"></td>
<td><img align="middle" src="latex/chapter-9/graphics/NEWexample4_2.png" width="450"></td>
</tr>
<tr>
<td><img align="middle" src="latex/chapter-9/graphics/NEWexample4_3.png" width="450"></td>
</tr>
</table>
</p>

<center><b>图9.8.12</b> 编译后的幻灯片效果</center>


### 参考资料

- Charles T. Batts. [A Beamer Tutorial in Beamer](https://www.uncg.edu/cmp/reu/presentations/Charles%20Batts%20-%20Beamer%20Tutorial.pdf), April 4, 2007.

【回放】[**9.7 插入表格**](https://nbviewer.jupyter.org/github/xinychen/latex-cookbook/blob/main/chapter-9/section7.ipynb)

### License

<div class="alert alert-block alert-danger">
<b>This work is released under the MIT license.</b>
</div>