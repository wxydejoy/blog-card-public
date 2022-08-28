# 第二章 LaTeX基础及文档类型

## 导言

LaTeX是一款基于TeX计算机程序语言的文档排版系统，它沿用了TeX语法规则，但在文档制作与排版方面却比TeX更加灵活，使用LaTeX可轻松制作各类文档。一般而言，LaTeX语法规则是由命令 (command) 与环境 (environment) 构成，基于一些基本命令实现特定功能，例如，使用\usepackage{}命令能调用制作文档所需的宏包。

从代码结构上看，LaTeX制作文档的代码分为前导代码 (preamble) 与主体代码 (body) 两部分，两部分在LaTeX文档制作中扮演的角色不同，并且相对独立。前导代码主要用于申明文档类型、设置排版样式、调用特定宏包、定义特殊命令等；主体代码主要用于明确标题、章节、目录等文章结构以及创作内容。这样的代码结构有诸多优点，举例来说，文档内容创作完成后，我们只需修改前导代码就能实现对文档排版样式的调整或切换。

掌握LaTeX的常用命令与代码结构后，我们便能开始创建简单文档进行实操。从功能上说，LaTeX能满足人们对文档制作多样性的要求，LaTeX提供了基本的文档类型，例如常规文档 (article)、书籍 (book)、报告 (report)、幻灯片 (beamer)等，LaTeX多元化的文档类型能帮我们制作包括期刊论文、技术报告、学位论文、书籍著作、幻灯片、个人简历、海报、信件等在内的各类文档。不同的文档类型在文档大小、排版、章节样式等方面略有不同。因此，使用LaTeX制作文档时，申明文档类型往往是创作的第一步，申明文档类型的命令为\documentclass{}。

【继续】[**2.1 LaTeX语法规则**](https://nbviewer.jupyter.org/github/xinychen/latex-cookbook/blob/main/chapter-2/section1.ipynb)

### License

<div class="alert alert-block alert-danger">
<b>This work is released under the MIT license.</b>
</div>