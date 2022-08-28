## 2.6 制作中文文档

起初，LaTeX只提供英文的编译环境，对包括中文在内的其他文字支持程度不好，伴随着LaTeX在文档编辑方面的优势越来越深入人心，LaTeX逐渐开始支持多种文字的编译。在各类LaTeX技术问答社区，我们经常会看到一些关于LaTeX中文文档编译的问题，十几年前，最受大家关心的问题或许还是如何使用LaTeX编译中文文档。

### 2.6.1 使用`ctex`宏包或`ctexart`文档类型

通常来说，最简单的方式在XeLaTeX编译环境下使用`ctex`宏包，即`\usepackage[UTF8]{ctex}`。

【**例1**】在LaTeX中选择XeLaTeX编译器，并使用`ctex`宏包制作一个简单的中文文档。

```tex
\documentclass{article}
\usepackage[UTF8]{ctex}

\begin{document}

永和九年，岁在癸丑，暮春之初，会于会稽山阴之兰亭，修稧（禊）事也。群贤毕至，少长咸集。此地有崇山峻领（岭），茂林修竹；又有清流激湍，映带左右，引以为流觞曲水，列坐其次。虽无丝竹管弦之盛，一觞一咏，亦足以畅叙幽情。

\end{document}
```

编译后效果如图2-6-1所示。

<p align="center">
<img align="middle" src="latex/chapter-2/graphics/zh_example1.png" width="600" />
</p>

<center><b>图2-6-1</b> 编译后的文档</center>

当然，`ctex`中也有一种特定的文档类型，名为`ctexart`，使用这种文档类型即可制作中文文档。

【**例2**】在LaTeX中选择XeLaTeX编译器，并使用`ctexart`文档类型制作一个简单的中文文档。

```tex
\documentclass{ctexart}

\begin{document}

永和九年，岁在癸丑，暮春之初，会于会稽山阴之兰亭，修稧（禊）事也。群贤毕至，少长咸集。此地有崇山峻领（岭），茂林修竹；又有清流激湍，映带左右，引以为流觞曲水，列坐其次。虽无丝竹管弦之盛，一觞一咏，亦足以畅叙幽情。

\end{document}
```

编译后效果如图2-6-2所示。

<p align="center">
<img align="middle" src="latex/chapter-2/graphics/zh_example2.png" width="580" />
</p>

<center><b>图2-6-2</b> 编译后的文档</center>

在`ctexart`文档类型中，我们可自行设置字体类型，可供选择字体类型命令包括楷体 (`\kaishu`)、宋体 (`\songti`)、黑体 (`\heiti`)、仿宋 (`\fangsong`)。

【**例3**】在LaTeX中选择XeLaTeX编辑器，使用`ctexart`文档类型制作中文文档，将字体类型设置为楷体和黑体。

```tex
\documentclass{ctexart}

\begin{document}

{\kaishu 【楷书】

永和九年，岁在癸丑，暮春之初，会于会稽山阴之兰亭，修稧（禊）事也。群贤毕至，少长咸集。此地有崇山峻领（岭），茂林修竹；又有清流激湍，映带左右，引以为流觞曲水，列坐其次。虽无丝竹管弦之盛，一觞一咏，亦足以畅叙幽情。}

{\heiti 【黑体】

永和九年，岁在癸丑，暮春之初，会于会稽山阴之兰亭，修稧（禊）事也。群贤毕至，少长咸集。此地有崇山峻领（岭），茂林修竹；又有清流激湍，映带左右，引以为流觞曲水，列坐其次。虽无丝竹管弦之盛，一觞一咏，亦足以畅叙幽情。}

\end{document}
```

编译后效果如图2-6-3所示。

<p align="center">
<img align="middle" src="latex/chapter-2/graphics/zh_example3.png" width="600" />
</p>

<center><b>图2-6-3</b> 编译后的文档</center>


### 2.6.2 使用`xeCJK`宏包

`xeCJK`宏包是LaTeX中专门用于编译中文的工具包，申明调用该宏包的语句为`\usepackage{xeCJK}`。一般而言，常规的文档类型例如`article`均支持使用`xeCJK`宏包。

【**例4**】在LaTeX中选择XeLaTeX编译器，并在`article`文档类型中使用`xeCJK`宏包制作一个简单的中文文档。

```tex
\documentclass{article}
\usepackage{xeCJK}

\begin{document}

永和九年，岁在癸丑，暮春之初，会于会稽山阴之兰亭，修稧（禊）事也。群贤毕至，少长咸集。此地有崇山峻领（岭），茂林修竹；又有清流激湍，映带左右，引以为流觞曲水，列坐其次。虽无丝竹管弦之盛，一觞一咏，亦足以畅叙幽情。

\end{document}
```

编译后效果如图2-6-4所示。

<p align="center">
<img align="middle" src="latex/chapter-2/graphics/zh_example4.png" width="600" />
</p>

<center><b>图2-6-4</b> 编译后的文档</center>


### 2.6.3 使用`CJKutf8`宏包

`CJKutf8`宏包提供了一种编译中文的环境，即`\begin{CJK}{UTF8}{字体类型} \end{CJK}`，这里可以选择的字体类型有很多种，例如宋体 (gbsn)、楷体 (gkai)。需要注意的是，`CJKutf8`一般是在pdfLaTeX编译器中使用。

【**例5**】在LaTeX中选择pdfLaTeX编译器，使用`CJKutf8`宏包中的`\begin{CJK}{UTF8}{gkai} \end{CJK}`环境制作一个简单的中文文档。

```tex
\documentclass{article}
\usepackage{CJKutf8}

\begin{document}

\begin{CJK}{UTF8}{gkai}
永和九年，岁在癸丑，暮春之初，会于会稽山阴之兰亭，修稧（禊）事也。群贤毕至，少长咸集。此地有崇山峻领（岭），茂林修竹；又有清流激湍，映带左右，引以为流觞曲水，列坐其次。虽无丝竹管弦之盛，一觞一咏，亦足以畅叙幽情。
\end{CJK}

\end{document}
```

编译后效果如图2-6-5所示。

<p align="center">
<img align="middle" src="latex/chapter-2/graphics/zh_example5.png" width="600" />
</p>

<center><b>图2-6-5</b> 编译后的文档</center>


### 2.6.4 制作报告

开源项目[https://github.com/MCG-NKU/NSFC-LaTex](https://github.com/MCG-NKU/NSFC-LaTex)提供了国家自然科学基金申报书的LaTeX模板。

### 2.6.5 推荐资源

目前在Overleaf上已经出现了许多中文文档LaTeX模板，除了一些学位论文模板，一些中文学术期刊如《计算机学报》也提供了科技论文的LaTeX模板。

《中国科学：信息科学》[https://www.overleaf.com/project/5e99712a0916c900018d11af](https://www.overleaf.com/project/5e99712a0916c900018d11af)

《计算机学报》[https://www.overleaf.com/project/5f4793c256c62e0001f06d95](https://www.overleaf.com/project/5f4793c256c62e0001f06d95)

中文学位论文模板：

《浙江大学学位论文模板》[https://www.overleaf.com/project/610fa05007d0073d5405a04f](https://www.overleaf.com/project/610fa05007d0073d5405a04f)

《武汉大学博士学位论文模板》[https://www.overleaf.com/project/610fa09e07d007fa5605a1e9](https://www.overleaf.com/project/610fa09e07d007fa5605a1e9)

《中山大学研究生毕业论文模板》[https://www.overleaf.com/project/610fa17307d007f2d305a388](https://www.overleaf.com/project/610fa17307d007f2d305a388)

《南京大学研究生毕业论文模板》[https://www.overleaf.com/project/610fa1d007d00704c305a3eb](https://www.overleaf.com/project/610fa1d007d00704c305a3eb)

【回放】[**2.5 一些基本命令**](https://nbviewer.jupyter.org/github/xinychen/latex-cookbook/blob/main/chapter-2/section5.ipynb)

### License

<div class="alert alert-block alert-danger">
<b>This work is released under the MIT license.</b>
</div>
