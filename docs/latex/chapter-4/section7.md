## 4.7 优化理论

优化理论是科学研究的另一个重要方向，它的关键在于使用数学模型对现实问题建模，并在若干约束的条件下，求问题的最优解，主要分为单目标优化、多目标优化两种类型。不管是单目标优化还是多目标优化，其数学表达式的主要内容均包括目标函数及约束条件两个主要部分。

【**例1**】书写如下带约束的优化问题：

\begin{equation}
\begin{aligned}
&\min_{x}\,f(x) \\
&\text{s.t.}\,x\in\mathcal{X},\quad g_{j}\left(x\right)\leq 0,\,j=1,\ldots,r
\end{aligned}
\end{equation}

其中，min是minimize的缩写，s.t.是subject to的缩写。

```tex
\documentclass[12pt]{article}
\begin{document}

\begin{equation}
\begin{aligned}
&\min_{x}\,f(x) \\
&\text{s.t.}\,x\in\mathcal{X},\quad g_{j}\left(x\right)\leq 0,\,j=1,\ldots,r
\end{aligned}
\end{equation}

\end{document}
```

【**例2**】书写$x^{*}\in\operatorname{arg}\min_{x\in\mathcal{X}}~L(x,\lambda^{*})$。

```tex
\documentclass[12pt]{article}
\begin{document}

$$x^{*}\in\operatorname{arg}\min_{x\in\mathcal{X}}~L(x,\lambda^{*})$$

\end{document}
```

【**例3**】书写一个由有限个向量$\boldsymbol{x}_{1},\ldots,\boldsymbol{x}_{m}$构成的集合：

$$\operatorname{conv}\left(\{\boldsymbol{x}_{1},\cdots,\boldsymbol{x}_{m}\}\right)
=\left\{\sum_{i=1}^{m}\alpha_{i}\boldsymbol{x}_{i}
\bigm|\alpha_{i}\geq 0,\,i=1,\ldots,m,\,\sum_{i=1}^{m}\alpha_{i}=1\right\}$$

```tex
\documentclass[12pt]{article}
\usepackage{mathtools}
\begin{document}

$$\operatorname{conv}\left(\{\boldsymbol{x}_{1},\cdots,\boldsymbol{x}_{m}\}\right)
=\left\{\sum_{i=1}^{m}\alpha_{i}\boldsymbol{x}_{i}
\bigm|\alpha_{i}\geq 0,\,i=1,\ldots,m,\,\sum_{i=1}^{m}\alpha_{i}=1\right\}$$

\end{document}
```

【**例4**】书写

\begin{equation}
\begin{aligned}
f^{\star}(y)&=\sup_{x\in\mathbb{R}^{n}}~\left\{xy-f(x)\right\},\quad y\in\mathbb{R}^{n} \\
f^{\star\star}(x)&=\sup_{y\in\mathbb{R}^{n}}~\left\{xy-f^{\star}(y)\right\},\quad x\in\mathbb{R}^{n}
\end{aligned}
\end{equation}

其中，sup是supremum的缩写，表示上确界。

```tex
\documentclass[12pt]{article}
\usepackage{amssymb, amsfonts}
\begin{document}

\begin{equation}
\begin{aligned}
&f^{\star}(y)=\sup_{x\in\mathbb{R}^{n}}~\left\{xy-f(x)\right\},\quad y\in\mathbb{R}^{n} \\
&f^{\star\star}(x)=\sup_{y\in\mathbb{R}^{n}}~\left\{xy-f^{\star}(y)\right\},\quad x\in\mathbb{R}^{n}
\end{aligned}
\end{equation}

\end{document}
```

【**例5**】书写

\begin{equation}
f(x)=\inf_{z\in\mathbb{R}^{m}}~F(x,z),\quad x\in\mathbb{R}^{n}
\end{equation}

其中，inf是infimum的缩写，表示下确界。

```tex
\documentclass[12pt]{article}
\usepackage{amssymb, amsfonts}
\begin{document}

\begin{equation}
f(x)=\inf_{z\in\mathbb{R}^{m}}~F(x,z),\quad x\in\mathbb{R}^{n}
\end{equation}

\end{document}
```

【**例6**】书写

\begin{equation}
p(u)=\inf_{x\in\mathcal{X}}\sup_{z\in\mathcal{Z}}~\left\{\phi(x,z)-u'z\right\},\quad u\in\mathbb{R}^{m}
\end{equation}

```tex
\documentclass[12pt]{article}
\usepackage{amssymb, amsfonts}
\begin{document}

\begin{equation}
p(u)=\inf_{x\in\mathcal{X}}\sup_{z\in\mathcal{Z}}~\left\{\phi(x,z)-u'z\right\},\quad u\in\mathbb{R}^{m}
\end{equation}

\end{document}
```

### 练习题

> 打开LaTeX在线系统[https://www.overleaf.com](https://www.overleaf.com/project)或本地安装好的LaTeX编辑器，创建名为LaTeX_practice的项目，并同时新建一个以`.tex`为拓展名的源文件，完成以下几道练习题。

1. 书写

\begin{equation}
\begin{aligned}
q(\mu)=&\inf_{u\in\mathbb{R}^{m}}~\left\{p(u)+u'\mu\right\} \\
=&\inf_{u\in\mathbb{R}^{m}}\inf_{x\in\mathcal{X}}~\left\{p_{x}(u)+u'\mu\right\} \\
=&\inf_{x\in\mathcal{X}}\inf_{u\in\mathbb{R}^{m}}~\left\{p_{x}(u)+u'\mu\right\} \\
=&\inf_{x\in\mathcal{X}}~\left\{-p_{x}^{\star}(-\mu)\right\}
\end{aligned}
\end{equation}

```tex
\documentclass[12pt]{article}
\usepackage{amssymb, amsfonts}
\begin{document}

\begin{equation}
\begin{aligned}
% 在此处书写公式
\end{aligned}
\end{equation}

\end{document}
```


【回放】[**4.6 概率论与数理统计**](https://nbviewer.jupyter.org/github/xinychen/latex-cookbook/blob/main/chapter-4/section6.ipynb)

### License

<div class="alert alert-block alert-danger">
<b>This work is released under the MIT license.</b>
</div>
