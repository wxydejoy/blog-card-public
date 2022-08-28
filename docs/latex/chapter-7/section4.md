## 7.4 复杂模型实战解析

在本节中，我们将给出一些科研论文中的复杂模型供读者们进一步解析学习。


【**例7-40**】BCPF。

```tex
\documentclass[border=0.1cm]{standalone}
\usepackage[utf8]{inputenc}

\usepackage{tikz}
\usepackage{amsfonts}
\usepackage{amsmath,amssymb}
\usepackage{systeme,mathtools}
\usetikzlibrary{positioning,arrows.meta,quotes}
\usetikzlibrary{shapes,snakes}
\usetikzlibrary{bayesnet}
\tikzset{>=latex}
\tikzstyle{plate caption} = [caption, node distance=0, inner sep=0pt,
below left=5pt and 0pt of #1.south]

\begin{document}
\begin{tikzpicture}

    \node [obs] (x) at (0,0) {\large $x_{\boldsymbol{i}}$};
    \node [circle,draw=black,fill=white,inner sep=0pt,minimum size=0.6cm] (u1) at (-1.2,1.6) { $\boldsymbol{u}_{i_1}^{(1)}$};
    \node [circle,draw=black,fill=white,inner sep=0pt,minimum size=0.6cm] (u3) at (1.2,1.6) { $\boldsymbol{u}_{i_d}^{(d)}$};
    \node [circle,draw=black,fill=white,inner sep=0pt,minimum size=0.65cm] (lambda) at (0,3.0) {\large $\boldsymbol{\lambda}$};

	\node[mark size=1pt,color=black] at (0,1.6) {\pgfuseplotmark{*}};
	\node[mark size=1pt,color=black] at (-0.2,1.6) {\pgfuseplotmark{*}};
	\node[mark size=1pt,color=black] at (0.2,1.6) {\pgfuseplotmark{*}};

    \node [text width=0.5cm] (c0) at (0,4) {$\alpha,\beta$};
    \node [text width=0.5cm] (a0) at (2.5,2.6) {$\alpha,\beta$};
    \node [circle,draw=black,fill=white,inner sep=0pt,minimum size=0.65cm] (tau_epsilon) at (2.5,1.6) {\large $\tau_{\epsilon}$};
    
    \path [draw,->] (u1) edge (x);
    \path [draw,->] (u3) edge (x);
    \path [draw,->] (lambda) edge (u1);
    \path [draw,->] (lambda) edge (u3);

    \path [draw,->] (c0) edge (lambda);
    \path [draw,->] (tau_epsilon) edge (x);
    \path [draw,->] (a0) edge (tau_epsilon);
    \plate [color=red] {part1} {(x)(u1)} { };
    \plate [color=blue] {part3} {(x)(u3)(part1.north east)} { };

    \node [text width=2cm] at (-0.6,-0.5) {\large $n_1$};
    \node [text width=2cm] at (2,-0.5) {\large $n_d$};

\end{tikzpicture}
\end{document}
```
编译上述代码，得到图形如图7.4.1所示。

<p align="center">
<img align="middle" src="latex/chapter-7/graphics/example_sec7_4_1.png" width="250" />
</p>

<center><b>图7.4.1</b> 编译后的图形效果</center>

【**例7-41**】Sticky HDP-HMM。

```tex
\documentclass[border=0.1cm]{standalone}
\usepackage[utf8]{inputenc}

\usepackage{tikz}
\usepackage{amsfonts}
\usepackage{amsmath,amssymb}
\usepackage{systeme,mathtools}
\usetikzlibrary{positioning,arrows.meta,quotes}
\usetikzlibrary{shapes,snakes}
\usetikzlibrary{bayesnet}
\tikzset{>=latex}
\tikzstyle{plate caption} = [caption, node distance=0, inner sep=0pt,
below left=5pt and 0pt of #1.south]

\tikzset{every picture/.style={line width=0.75pt}}

\begin{document}
\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]

    \node [obs] (o1) at (20,20) {$\boldsymbol{o}_1$};
    \node [circle,draw=black,fill=white, inner sep=0pt,minimum size=0.75cm] (p1) at (20,-60) {$z_1$};
    \node [circle,draw=black,fill=white, inner sep=0pt,minimum size=0.75cm] (p0) at (20,-130) {$z_0$};
    \node [obs] (o2) at (70,20) {$\boldsymbol{o}_2$};
    \node [circle,draw=black,fill=white, inner sep=0pt,minimum size=0.75cm] (p2) at (70,-60) {$z_2$};
    \node [obs] (o3) at (160,20) {$\boldsymbol{o}_T$};
    \node [circle,draw=black,fill=white, inner sep=0pt,minimum size=0.75cm] (p3) at (160,-60) {$z_T$};
    \node [circle,draw=black,fill=white,inner sep=0pt,minimum size=0.75cm] (theta) at (-60,-20) {$\theta_i$};
    \node [circle,draw=black,fill=white,inner sep=0pt,minimum size=0.75cm] (pi) at (-60,-100) {$\pi_i$};
    \node [circle,draw=black,fill=white,inner sep=0pt,minimum size=0.75cm] (beta) at (-60,-150) {$\beta$};
    \node [text width=2cm] (inf1) at (-57,10) {\small{$i\in\left\{1,...,\infty \right\}$}};

    \node [text width=2cm] (inf2) at (-57,-70)
    {\small{$i\in\left\{1,...,\infty \right\}$}};

    \node [text width=.2cm] (lambda) at (-130,-20) {$\lambda$};
    \node [text width=.2cm] (alpha) at (-130,-100) {$\alpha$};
    \node [text width=.2cm] (kappa) at (-130,-120) {$\kappa$};
    \node [text width=.2cm] (gamma) at (-130,-150) {$\gamma$};
    \node [text width=.2cm] (gamma) at (-130,-150) {$\gamma$};
    \node [text width=.4cm] (1dot) at (115,-60) {$...$};
    \node [text width=.4cm] (2dot) at (115,20) {$...$};

    \path [draw,->] (p2) edge (1dot);
    \path [draw,->] (1dot) edge (p3);
    \path [draw,->] (p1) edge (o1);
    \path [draw,->] (p2) edge (o2);
    \path [draw,->] (p3) edge (o3);
    \path [draw,->] (p1) edge (p2);
    \path [draw,->] (p0) edge (p1);
    \path [draw,->] (alpha) edge (pi);
    \path [draw,->] (kappa) edge (pi);
    \path [draw,->] (beta) edge (pi);
    \path [draw,->] (gamma) edge (beta);
    \path [draw,->] (lambda) edge (theta);
    \plate [color=black] {part2} {(theta)(inf1)} { };
    \plate [color=black] {part3} {(pi)(inf2)} { };
    \draw[black,->,thick] (pi.east) to [in=-150,out=-16] (147,-65);
    \draw[black,->,thick] (pi.east) to [in=-143,out=-5] (57,-65);
    \draw[black,->,thick] (pi.east) to [in=-135,out=5] (7,-65);
    \draw[black,->,thick] (theta.east) to [in=-150,out=-16] (147,15);
    \draw[black,->,thick] (theta.east) to [in=-143,out=-5] (57,15);
    \draw[black,->,thick] (theta.east) to [in=-135,out=5] (7,15);

\end{tikzpicture}
\end{document}
```
编译上述代码，得到图形如图7.4.2所示。

<p align="center">
<img align="middle" src="latex/chapter-7/graphics/example_sec7_4_2.png" width="400" />
</p>

<center><b>图7.4.2</b> 编译后的图形效果</center>


【**例7-42**】BTMF。

```tex
\documentclass[border=0.1cm, 12pt]{standalone}
\usepackage{tikz}
\usepackage{amsfonts}
\usepackage{amsmath,amssymb}
\usepackage{systeme,mathtools}
\usetikzlibrary{positioning,arrows.meta,quotes}
\usetikzlibrary{shapes,snakes}
\usetikzlibrary{bayesnet}
\tikzset{>=latex}
\tikzstyle{plate caption} = [caption, node distance=0, inner sep=0pt,
below left=5pt and 0pt of #1.south]
\begin{document}
\begin{tikzpicture}

	\node [obs,inner sep=0pt,minimum size=0.8cm] (obs) at (0.8+2.4,0+0.8-0.3) {\normalsize$y_{i,t+1}$};
	\node [obs,minimum size=0.95cm] (obs1) at (-0.8+2.4,0+0.8-0.3) {\normalsize$y_{i,t}$};
	\node [circle,draw=black,fill=white,inner sep=0pt,minimum size=0.8cm] (obs2) at (-0.8+2.4-1.6,0.5) {$y_{i,t-1}$};
	\node [circle,draw=black,fill=white,inner sep=0pt,minimum size=0.8cm] (xtd1) at (-2.6,-2.0) {\scalebox{0.85}[1]{$\boldsymbol{x}_{t-d+1}$}};
	\node [circle,draw=black,fill=white,inner sep=0pt,minimum size=1cm] (xtd) at (-4.2,-2.0) {$\boldsymbol{x}_{t-d}$};
	\node [circle,draw=black,fill=white,inner sep=0pt,minimum size=1cm] (xt1) at (3.2,-2.0) {$\boldsymbol{x}_{t+1}$};
    \node [circle,draw=black,fill=white,inner sep=0pt,minimum size=1cm] (xt2) at (1.6,-2.0) {$\boldsymbol{x}_{t}$};
	\node [circle,draw=black,fill=white,inner sep=0pt,minimum size=1cm] (xt3) at (0,-2.0) {$\boldsymbol{x}_{t-1}$};
	\node [circle,draw=black,fill=white,inner sep=0pt,minimum size=1cm] (w) at (2.4-0.8,2.3-0.4) {$\boldsymbol{w}_{i}$};
    \node [circle,draw=black,fill=white,inner sep=0pt,minimum size=0.9cm] (lambda) at (3.2-0.8,3.8-0.4) {$\Lambda_{w}$};
    \node [circle,draw=black,fill=white,inner sep=0pt,minimum size=0.9cm] (mu) at (0+2.4-1.6,3.8-0.4) {$\boldsymbol{\mu}_{w}$};
    \node [circle,draw=black,fill=white,inner sep=0pt,minimum size=0.9cm] (kappa) at (0.8,-4) {$\Sigma$};
    \node [circle,draw=black,fill=white,inner sep=0pt,minimum size=0.9cm] (thetak) at (-1.3,-4) {$A$};

	\node[mark size=1pt,color=black] at (-1.6+2.4-1.6,0+0.8-0.3) {\pgfuseplotmark{*}};
	\node[mark size=1pt,color=black] at (-1.8+2.4-1.6,0+0.8-0.3) {\pgfuseplotmark{*}};
	\node[mark size=1pt,color=black] (leftnode0) at (-2.0+2.4-1.6,0+0.8-0.3) {\pgfuseplotmark{*}};

	\node[mark size=1pt,color=black] at (1.6+2.4,0+0.8-0.3) {\pgfuseplotmark{*}};
	\node[mark size=1pt,color=black] at (1.8+2.4,0+0.8-0.3) {\pgfuseplotmark{*}};
	\node[mark size=1pt,color=black] (rightnode0) at (2.0+2.4,0+0.8-0.3) {\pgfuseplotmark{*}};

	\node[mark size=1pt,color=black] at (-1.1,-2) {\pgfuseplotmark{*}};
	\node[mark size=1pt,color=black] at (-1.3,-2) {\pgfuseplotmark{*}};
	\node[mark size=1pt,color=black] at (-1.5,-2) {\pgfuseplotmark{*}};

	\node[mark size=1pt,color=black] (leftnode1) at (-5.4,-2) {\pgfuseplotmark{*}};
	\node[mark size=1pt,color=black] at (-5.2,-2) {\pgfuseplotmark{*}};
	\node[mark size=1pt,color=black] at (-5.0,-2) {\pgfuseplotmark{*}};

	\node[mark size=1pt,color=black] (rightnode1) at (4.4,-2) {\pgfuseplotmark{*}};
	\node[mark size=1pt,color=black] at (4.2,-2) {\pgfuseplotmark{*}};
	\node[mark size=1pt,color=black] at (4.0,-2) {\pgfuseplotmark{*}};

    \node [circle,draw=black,fill=white,inner sep=0pt,minimum size=0.8cm] (tau) at (3.0+2.4-1.2,-1.8+0.8) {$\tau$};
    \node [text width=0.6cm] (gamma1) at (3.0+2.4,-1.8+0.8) {$\alpha,\beta$};
    \node [text width=0.9cm] (gamma2) at (0+2.4,4.8-0.3) {\small $W_0,\nu_0$};
    \node [text width=0.5cm] (mu0) at (0+2.4-1.6,4.8-0.3) {$\boldsymbol{\mu}_0$};
    \node [text width=0.9cm] (gamma3) at (0.8,-5.1) {\small $S_0,\nu_0$};
    \node [text width=1.2cm] (gamma4) at (-1.3,-5.1) {\small $M_0,\Psi_0$};
    
    \path [draw,->] (w) edge (obs);
    \path [draw,->] (w) edge (obs1);
 	\path [draw,->,dashed] (w) edge (obs2);
    \path [draw,->] (lambda) edge (w);
    \path [draw,->] (kappa) edge (xtd);
    \path [draw,->] (kappa) edge (xtd1);
    \path [draw,->] (kappa) edge (xt1);
    \path [draw,->] (kappa) edge (xt2);
    \path [draw,->] (kappa) edge (xt3);
    \path [draw,->] (gamma1) edge (tau);
    \path [draw,->] (gamma2) edge (lambda);
    \path [draw,->] (gamma3) edge (kappa);
    \path [draw,->] (gamma4) edge (thetak);
    \path [draw,->] (lambda) edge (mu);
    \path [draw,->] (mu) edge (w);
    \path [draw,->] (mu0) edge (mu);
    \path [draw,->] (tau) edge (obs);
    \path [draw,->] (tau) edge (obs1);
    \path [draw,->,dashed] (tau) edge (obs2);
	\path [draw,->] (xt1) edge (obs);
	\path [draw,->] (xt2) edge (xt1);
 	\path [draw,->] (xt3) edge (xt2);
 	\path [draw,->,dashed] (xt3) edge (obs2);
	\path [draw,->] (xt3) edge [bend left] node [right] {} (xt1);
 	\path [draw,->] (xtd) edge [bend left] node [right] {} (xt2);
 	\path [draw,->] (xtd) edge [bend left] node [right] {} (xt3);
 	\path [draw,->] (xtd) edge (xtd1);
 	\path [draw,->] (xtd1) edge [bend left] node [right] {} (xt1);
 	\path [draw,->] (xtd1) edge [bend left] node [right] {} (xt2);
 	\path [draw,->] (xtd1) edge [bend left] node [right] {} (xt3);
	\path [draw,->] (xt2) edge (obs1);
	\path [draw,->] (thetak) edge (xt1);
	\path [draw,->] (thetak) edge (xt2);
	\path [draw,->] (thetak) edge (xt3);
	\path [draw,->] (thetak) edge (xtd);
	\path [draw,->] (thetak) edge (xtd1);
	\path [draw,->] (kappa) edge (thetak);

    \node [text width=2.2cm] (m) at (-1+2.5-1.5,2.6+0.8-1.6) {\small{$i\in\left\{1,...,N\right\}$}};
    \plate [color=black] {part1} {(leftnode0)(rightnode0)(obs)(obs1)(w)(m)} { };
    
\end{tikzpicture}
\end{document}
```
编译上述代码，得到图形如图7.4.3所示。

<p align="center">
<img align="middle" src="latex/chapter-7/graphics/example_sec7_4_3.png" width="500" />
</p>

<center><b>图7.4.3</b> 编译后的图形效果</center>

【**例7-43**】矩阵分解示意图。

```tex
\documentclass[border=0.1cm]{standalone}
\usepackage[utf8]{inputenc}

\usepackage{tikz}
\usepackage{amsfonts}
\usepackage{amsmath,amssymb}
\usepackage{systeme,mathtools}
\usetikzlibrary{positioning,arrows.meta,quotes}
\usetikzlibrary{shapes,snakes}
\usetikzlibrary{bayesnet}
\tikzset{>=latex}

\begin{document}
\begin{tikzpicture}

    \draw [very thick] (0,0) rectangle (3.6/2,2.4/2);
    \filldraw [fill=green!20!white,draw=green!40!black] (0,0) rectangle (3.6/2,2.4/2);
    \filldraw [fill=white] (0.4/2,0.4/2) rectangle (0.8/2,0.8/2);
    \filldraw [fill=white] (2.4/2,0.4/2) rectangle (2.8/2,0.8/2);
    \filldraw [fill=white] (0.8/2,1.2/2) rectangle (1.2/2,1.6/2);
    \filldraw [fill=white] (2.0/2,1.6/2) rectangle (2.4/2,2.0/2);
    \filldraw [fill=white] (0.4/2,2.0/2) rectangle (0.8/2,2.4/2);
    \filldraw [fill=white] (2.4/2,2.0/2) rectangle (2.8/2,2.4/2);
    \filldraw [fill=white] (2.8/2,1.2/2) rectangle (3.2/2,2.0/2);
    \draw [step=0.4/2, very thin, color=gray] (0,0) grid (3.6/2,2.4/2);
    \draw (1.8/2,-0.3) node {{\color{red}\scriptsize{$Y\in\mathbb{R}^{m\times f}$}}};
    \draw (4.4/2,1.2/2) node {{\color{black}\large{$\approx$}}};
    \draw [very thick] (5.2/2,0) rectangle (6.0/2,2.4/2);
    \filldraw [fill=green!20!white,draw=green!40!black] (5.2/2,0) rectangle (6.0/2,2.4/2);
    \draw [step=0.4/2, very thin, color=gray] (5.2/2,0) grid (6.0/2,2.4/2);
    \draw (5.6/2,-0.3) node {{\color{black}\scriptsize{$W\in\mathbb{R}^{m\times r}$}}};
    \draw (6.8/2,1.2/2) node {{\color{black}\large{$\times$}}};
    \draw [very thick] (7.6/2,0.8/2) rectangle (11.2/2,1.6/2);
    \filldraw [fill=green!20!white,draw=green!40!black] (7.6/2,0.8/2) rectangle (11.2/2,1.6/2);
    \draw [step=0.4/2, very thin, color=gray] (7.6/2,0.8/2) grid (11.2/2,1.6/2);
    \draw (9.4/2,0) node {{\color{red}\scriptsize{$X^{T}\in\mathbb{R}^{r\times f}$}}};
    
\end{tikzpicture}
\end{document}
```
编译上述代码，得到图形如图7.4.4所示。

<p align="center">
<img align="middle" src="latex/chapter-7/graphics/example_sec7_4_4.png" width="350" />
</p>

<center><b>图7.4.4</b> 编译后的图形效果</center>

更多模型例子可以参考开源项目：[https://github.com/xinychen/awesome-latex-drawing](https://github.com/xinychen/awesome-latex-drawing)。

【回放】[**7.3 高级功能**](https://nbviewer.jupyter.org/github/xinychen/latex-cookbook/blob/main/chapter-7/section3.ipynb)

### License

<div class="alert alert-block alert-danger">
<b>This work is released under the MIT license.</b>
</div>
