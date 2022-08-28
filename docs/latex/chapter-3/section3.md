## 3.3 生成目录

章节目录一般创建在摘要之后，在LaTeX中，使用`\tableofcontents`命令即可。命令放在哪里，就会在哪里自动创建一个章节目录。默认情况下，该命令会根据用户定义的篇章节标题生成文章目录，目录中将包含`\subsubsection`及其更高层次的结构标题。但对于带星号的章节命令，其章节标题不会出现在目录中。

【**例1**】使用`\tableofcontents`命令创建章节目录。

```tex
\documentclass[12pt]{article}
\begin{document}

\tableofcontents  % 创建章节目录

\section{First Section}
\subsection{Subsection title 1}
\subsection{Subsection title 2}
\subsection{Subsection title 3}
\section{Second Section}
\subsection{Subsection title 4}
\subsection{Subsection title 5}
\subsection{Subsection title 6}
\section*{Third section}
\subsection*{Subsection title 7}
\subsection*{Subsection title 8}
\subsection*{Subsection title 9}

\end{document}
```

编译后的效果如图3-3-1所示：

<p align="center">
<img align="middle" src="latex/chapter-3/graphics/example3_3_1.png" width="500" />
</p>

<center><b>图3-3-1</b> 编译后效果</center>

根据不同的格式需求，用户可以对目录格式进行调整。

- 调整章节层次深度

    在上一节中我们介绍了使用`\setcounter{secnumdepth}{}`计数器命令调整章节自动编号深度，类似地，我们可以通过在导言区使用`\setcounter{tocdepth}{}`命令指定目录中的章节层次深度。
    
    【**例2**】使用`\setcounter{tocdepth}{}`命令调整章节层次深度。
    
    ```tex
    \setcounter{tocdepth}{0}  
    % 目录层次仅包括`\part`和`chapter`
    
    \setcounter{tocdepth}{1}  % 设置目录层次深入到`\section`级
    
    \setcounter{tocdepth}{2}  % 设置目录层次深入到`\subsection`级
    
    \setcounter{tocdepth}{3}  % 设置目录层次深入到`\subsubsection`级，默认值
    ```
    
    上面的语句可以为所有章节指定相同的目录层次深度。此外，我们也可以为每个章节设置不同的目录层次，具体是通过在每个章节创建命令前，使用`\addtocontents{toc}{\setcounter{tocdepth}{}}`命令为该章节指定目录层次深度。
    
    【**例3**】使用`\addtocontents{toc}{\setcounter{tocdepth}{}}`命令为各章节设置不同的目录层次。
    
    ```tex
    \addtocontents{toc}{\setcounter{tocdepth}{1}} % 将章节“First Section”的目录层次深度设为1
    
    \section{First Section}
    
    \addtocontents{toc}{\setcounter{tocdepth}{2}} % 将章节“Second Section”的目录层次深度设为2
    
    \section{Second Section}
    ```
    
- 设置章节标题的“目录别名”

    对于章节标题特别长的情况，直接在目录中显示完整标题显然可视化效果不佳，因此需要为长章节标题设置一个比较短的“目录别名”。通过这种设置，在正文中可以显示完整标题，而在目录中将显示“短标题”。为此，只需要在章节创建命令中添加目录别名选项即可。
    
- 添加目录章节引用链接
    
    如果想要为目录中的章节引用添加链接，使得点击链接后就能跳转到相应章节所在页面，那么只需要在导言区调用`hyperref`宏包、并设置`colorlinks=true`选项即可，此时文档中章节引用及其它交叉引用均会被自动添加链接（添加了链接的引用将显示为红色）。
    
    【**例4**】使用`\section[]{}`设置章节目录别名，并使用`hyperref`宏包为目录章节引用自动添加链接。
    
    ```tex
    \documentclass[12pt]{article}
    \usepackage[colorlinks=true]{hyperref}  % 为文档中的章节引用自动添加链接
    \begin{document}
    
    \tableofcontents

    \section[FS]{First Section}  % 将章节“First Section”的目录别名设为“FS”
    \subsection{Subsection title 1}
    \subsection{Subsection title 2}
    \subsection{Subsection title 3}
    \section[SS]{Second Section}  % 将章节“Second Section”的目录别名设为“SS”
    \subsection{Subsection title 4}
    \subsection{Subsection title 5}
    \subsection{Subsection title 6}
    \section[TS]{Third Section}  % 将章节“Third Section”的目录别名设为“TS”
    \subsection{Subsection title 7}
    \subsection{Subsection title 8}
    \subsection{Subsection title 9}

    \end{document}
    ```
    
    编译后的效果如图3-3-2所示：

    <p align="center">
    <img align="middle" src="latex/chapter-3/graphics/example3_3_2.png" width="500" />
    </p>

    <center><b>图3-3-2</b> 编译后效果</center>
    
    
    
    
 

【回放】[**3.2 创建章节**](https://nbviewer.jupyter.org/github/xinychen/latex-cookbook/blob/main/chapter-3/section2.ipynb)

【继续】[**3.4 编辑段落**](https://nbviewer.jupyter.org/github/xinychen/latex-cookbook/blob/main/chapter-3/section4.ipynb)

### License

<div class="alert alert-block alert-danger">
<b>This work is released under the MIT license.</b>
</div>
