## 4.5 线性代数

### 4.5.1 矩阵

在线性代数和众多代数课程中，矩阵是最基础的代数结构，可以直观上理解为数表。使用LaTeX时，我们可以用`\begin{array} \end{array}`环境来书写矩阵。

【**例1**】书写矩阵$\left[\begin{array}{ccc} 1 & 2 & 3 \\ 4 & 5 & 6 \\ \end{array}\right]$和$\left[\begin{array}{c|cc} 1 & 2 & 3 \\ \hline 4 & 5 & 6 \\ \end{array}\right]$。

```tex
\documentclass[12pt]{article}
\begin{document}

$$\left[\begin{array}{ccc} 1 & 2 & 3 \\ 4 & 5 & 6 \\ \end{array}\right]$$
$$\left[\begin{array}{c|cc} 1 & 2 & 3 \\ \hline 4 & 5 & 6 \\ \end{array}\right]$$

\end{document}
```

另外，除了`\begin{array} \end{array}`，我们还可以用`\begin{matrix} \end{matrix}`、`\begin{pmatrix} \end{pmatrix}`、`\begin{Vmatrix} \end{Vmatrix}`等一系列环境来书写矩阵。

【**例2**】针对例4-48，使用

- `\begin{smallmatrix} \end{smallmatrix}`，编译结果为
$$\begin{smallmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ \end{smallmatrix}$$
- `\begin{matrix} \end{matrix}`，编译结果为
$$\begin{matrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ \end{matrix}$$
- `\begin{pmatrix} \end{pmatrix}`，编译结果为
$$\begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ \end{pmatrix}$$
- `\begin{bmatrix} \end{bmatrix}`，编译结果为
$$\begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ \end{bmatrix}$$
- `\begin{Bmatrix} \end{Bmatrix}`，编译结果为
$$\begin{Bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ \end{Bmatrix}$$
- `\begin{vmatrix} \end{vmatrix}`，编译结果为
$$\begin{vmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ \end{vmatrix}$$
- `\begin{Vmatrix} \end{Vmatrix}`，编译结果为
$$\begin{Vmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ \end{Vmatrix}$$

```tex
\documentclass[12pt]{article}
\usepackage{mathtools}
\begin{document}
$$\begin{smallmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ \end{smallmatrix}$$
$$\begin{matrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ \end{matrix}$$
$$\begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ \end{pmatrix}$$
$$\begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ \end{bmatrix}$$
$$\begin{Bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ \end{Bmatrix}$$
$$\begin{vmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ \end{vmatrix}$$
$$\begin{Vmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ \end{Vmatrix}$$

\end{document}
```

在线性代数中，一般用粗体字母或者符号表示矩阵，例如$\mathbf{A},\mathbf{B},\mathbf{C},\mathbf{X},\mathbf{Y},\mathbf{Z}$。

【**例3**】书写矩阵$\mathbf{A}=\begin{bmatrix} a_{11} & a_{12} & \cdots & a_{1n} \\ a_{21} & a_{22} & \cdots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{m1} & a_{m2} & \cdots & a_{mn} \end{bmatrix}$。

```tex
\documentclass[12pt]{article}
\begin{document}
$$\mathbf{A}=\begin{bmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
a_{21} & a_{22} & \cdots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m1} & a_{m2} & \cdots & a_{mn} 
\end{bmatrix}$$

\end{document}
```

当然，有时候，也可以用大写字母直接表示矩阵，用加粗的小写字母表示向量，用小写字母表示标量。需要注意的是，张量作为矩阵的延伸，一般用$\mathcal{X}$或者加粗的$\boldsymbol{\mathcal{X}}$表示，对应的代码分别为`\mathcal{X}`和`\boldsymbol{\mathcal{X}}`。

【**例4**】书写

$$\begin{bmatrix} 1 & 2 \\ 3 & 4 \\ 5 & 6\\ \end{bmatrix}
\begin{bmatrix} 7 \\ 8 \\ \end{bmatrix}
=\begin{bmatrix} 1\times7+2\times8 \\ 3\times7+4\times8 \\
5\times7+6\times8 \\ \end{bmatrix}
=7\begin{bmatrix} 1 \\ 3 \\ 5 \\ \end{bmatrix}
+8\begin{bmatrix} 2 \\ 4 \\ 6 \\ \end{bmatrix}
=\begin{bmatrix} 23 \\ 53 \\ 83 \\ \end{bmatrix}$$

```tex
\documentclass[12pt]{article}
\usepackage{mathtools}
\begin{document}
$$\begin{bmatrix} 1 & 2 \\ 3 & 4 \\ 5 & 6\\ \end{bmatrix}
\begin{bmatrix} 7 \\ 8 \\ \end{bmatrix}
=\begin{bmatrix} 1\times7+2\times8 \\ 3\times7+4\times8 \\
5\times7+6\times8 \\ \end{bmatrix}
=7\begin{bmatrix} 1 \\ 3 \\ 5 \\ \end{bmatrix}
+8\begin{bmatrix} 2 \\ 4 \\ 6 \\ \end{bmatrix}
=\begin{bmatrix} 23 \\ 53 \\ 83 \\ \end{bmatrix}$$

\end{document}
```

【**例5**】书写

$$\boldsymbol{y}:=\boldsymbol{y}+
\left[\begin{array}{c|c|c} A_{1} & \cdots & A_{n} \end{array}\right]
\left[\begin{array}{c} \boldsymbol{x}_{1} \\ \vdots \\ \boldsymbol{x}_{n} \\ \end{array}\right]
=\boldsymbol{y}+\sum_{i=1}^{n}A_{i}\boldsymbol{x}_{i}$$

```tex
\documentclass[12pt]{article}
\usepackage{mathtools}
\begin{document}
$$\boldsymbol{y}:=\boldsymbol{y}+
\left[\begin{array}{c|c|c} A_{1} & \cdots & A_{n} \end{array}\right]
\left[\begin{array}{c} \boldsymbol{x}_{1} \\ \vdots \\ \boldsymbol{x}_{n} \\ \end{array}\right]
=\boldsymbol{y}+\sum_{i=1}^{n}A_{i}\boldsymbol{x}_{i}$$

\end{document}
```

【**例6**】书写

$$\begin{bmatrix} 0 & 0 & 1 \\ 0 & 1 & 0 \\ 1 & 0 & 0 \\ \end{bmatrix}
\begin{bmatrix} a & b & c \\ b & d & e \\ c& e & f \\ \end{bmatrix}
=\begin{bmatrix} c & e & f \\ b & d & e \\ a & b & c \\ \end{bmatrix}$$

```tex
\documentclass[12pt]{article}
\usepackage{mathtools}
\begin{document}
$$\begin{bmatrix} 0 & 0 & 1 \\ 0 & 1 & 0 \\ 1 & 0 & 0 \\ \end{bmatrix}
\begin{bmatrix} a & b & c \\ b & d & e \\ c& e & f \\ \end{bmatrix}
=\begin{bmatrix} c & e & f \\ b & d & e \\ a & b & c \\ \end{bmatrix}$$

\end{document}
```

### 4.5.2 符号

作用于矩阵的符号可分为标记符号和运算符号，就标记符号而言，有

- 矩阵的逆，如$\mathbf{A}^{-1}$，代码为`\mathbf{A}^{-1}`；
- 矩阵的伪逆，写作$\mathbf{A}^{+}$或$\mathbf{A}^{\dagger}$，代码分别为`\mathbf{A}^{+}`和`\mathbf{A}^{\dagger}`；
- 矩阵的转置，写作$\mathbf{A}^{T}$或$\mathbf{A}^{\top}$，代码分别为`\mathbf{A}^{T}`和`\mathbf{A}^{\top}`；
- 酉矩阵的转置，写作$\mathbf{A}^{H}$，代码分别为`\mathbf{A}^{H}`；
- 矩阵的秩，写作$\operatorname{rank}\left(\mathbf{A}\right)$，代码为`\operatorname{rank}\left(\mathbf{A}\right)`；
- 矩阵的迹，写作$\operatorname{Tr}\left(\mathbf{A}\right)$，代码为`\operatorname{Tr}\left(\mathbf{A}\right)`；
- 矩阵的行列式，写作$\det\left(\mathbf{A}\right)$，代码为`\det\left(\mathbf{A}\right)`；

【**例7**】书写矩阵运算规则：

$$\left(\mathbf{A}\mathbf{B}\right)^{-1}=\mathbf{B}^{-1}\mathbf{A}^{-1}$$
$$\left(\mathbf{A}+\mathbf{B}\right)^{\top}=\mathbf{A}^{\top}+\mathbf{B}^{\top}$$
$$\left(\mathbf{A}+\mathbf{B}\right)^{H}=\mathbf{A}^{H}+\mathbf{B}^{H}$$
$$\operatorname{Tr}\left(\mathbf{A}+\mathbf{B}\right)=
\operatorname{Tr}\left(\mathbf{A}\right)+\operatorname{Tr}\left(\mathbf{B}\right)$$
$$\det\left(\mathbf{A}\mathbf{B}\right)=\det\left(\mathbf{A}\right)\det\left(\mathbf{B}\right)$$

```tex
\documentclass[12pt]{article}
\usepackage{mathtools}
\begin{document}

$$\left(\mathbf{A}\mathbf{B}\right)^{-1}=\mathbf{B}^{-1}\mathbf{A}^{-1}$$
$$\left(\mathbf{A}+\mathbf{B}\right)^{\top}=\mathbf{A}^{\top}+\mathbf{B}^{\top}$$
$$\left(\mathbf{A}+\mathbf{B}\right)^{H}=\mathbf{A}^{H}+\mathbf{B}^{H}$$
$$\operatorname{Tr}\left(\mathbf{A}+\mathbf{B}\right)=
\operatorname{Tr}\left(\mathbf{A}\right)+\operatorname{Tr}\left(\mathbf{B}\right)$$
$$\det\left(\mathbf{A}\mathbf{B}\right)=\det\left(\mathbf{A}\right)\det\left(\mathbf{B}\right)$$

\end{document}
```

【**例8**】书写$\frac{\partial}{\partial\mathbf{X}}\operatorname{Tr}
\left(\mathbf{A}\mathbf{X}\mathbf{B}\right)
=\mathbf{A}^{\top}\mathbf{B}^{\top}$。

```tex
\documentclass[12pt]{article}
\usepackage{mathtools}
\begin{document}

$$\frac{\partial}{\partial\mathbf{X}}\operatorname{Tr}
\left(\mathbf{A}\mathbf{X}\mathbf{B}\right)
=\mathbf{A}^{\top}\mathbf{B}^{\top}$$

\end{document}
```

【**例9**】书写多元正态分布的概率密度函数：

$$p\left(\mathbf{x}\right)=
\frac{1}{\sqrt{\operatorname{det}\left(2\pi\mathbf{\Sigma}\right)}}
\exp\left[-\frac{1}{2}\left(\mathbf{x}-\mathbf{\mu}\right)^{\top}
\mathbf{\Sigma}^{-1}\left(\mathbf{x}-\mathbf{\mu}\right)\right]$$

```tex
\documentclass[12pt]{article}
\begin{document}

$$p\left(\mathbf{x}\right)=
\frac{1}{\sqrt{\operatorname{det}\left(2\pi\mathbf{\Sigma}\right)}}
\exp\left[-\frac{1}{2}\left(\mathbf{x}-\mathbf{\mu}\right)^{\top}
\mathbf{\Sigma}^{-1}\left(\mathbf{x}-\mathbf{\mu}\right)\right]$$

\end{document}
```

【**例10**】书写混合高斯分布的概率密度函数：

$$p\left(\mathbf{x}\right)=\sum_{k=1}^{K}\rho_{k}\frac{1}
{\sqrt{\operatorname{det}\left(2\pi\mathbf{\Sigma}_{k}\right)}}
\exp\left[-\frac{1}{2}\left(\mathbf{x}-\mathbf{\mu}_{k}\right)^{\top}
\mathbf{\Sigma}_{k}^{-1}\left(\mathbf{x}-\mathbf{\mu}_{k}\right)\right]$$

```tex
\documentclass[12pt]{article}
\begin{document}

$$p\left(\mathbf{x}\right)=\sum_{k=1}^{K}\rho_{k}\frac{1}
{\sqrt{\operatorname{det}\left(2\pi\mathbf{\Sigma}_{k}\right)}}
\exp\left[-\frac{1}{2}\left(\mathbf{x}-\mathbf{\mu}_{k}\right)^{\top}
\mathbf{\Sigma}_{k}^{-1}\left(\mathbf{x}-\mathbf{\mu}_{k}\right)\right]$$

\end{document}
```

就运算符号而言，有

- Hadamard积，如$\mathbf{A}\circ\mathbf{B}$，代码为`\mathbf{A}\circle\mathbf{B}`；
- Kronecker积，如$\mathbf{A}\otimes\mathbf{B}$，代码为`\mathbf{A}\otimes\mathbf{B}`；
- 内积，如$\left<\mathbf{A},\mathbf{B}\right>$，代码为`\left<\mathbf{A},\mathbf{B}\right>`。

【**例11**】书写Kronecker积运算：

\begin{equation}
\mathbf{X}\otimes\mathbf{Y}=\left[\begin{array}{cccc}
x_{11}\mathbf{Y} & x_{12}\mathbf{Y} & \cdots & x_{1n}\mathbf{Y} \\
x_{21}\mathbf{Y} & x_{22}\mathbf{Y} & \cdots & x_{2n}\mathbf{Y} \\
\vdots & \vdots & \ddots & \vdots \\
x_{m1}\mathbf{Y} & x_{m2}\mathbf{Y} & \cdots & x_{mn}\mathbf{Y}
\end{array}\right]
\end{equation}

```tex
\documentclass[12pt]{article}
\begin{document}

\begin{equation}
\mathbf{X}\otimes\mathbf{Y}=\left[\begin{array}{cccc}
x_{11}\mathbf{Y} & x_{12}\mathbf{Y} & \cdots & x_{1n}\mathbf{Y} \\
x_{21}\mathbf{Y} & x_{22}\mathbf{Y} & \cdots & x_{2n}\mathbf{Y} \\
\vdots & \vdots & \ddots & \vdots \\
x_{m1}\mathbf{Y} & x_{m2}\mathbf{Y} & \cdots & x_{mn}\mathbf{Y}
\end{array}\right]
\end{equation}

\end{document}
```

【**例12**】书写李亚普诺夫方程：

\begin{equation}
\begin{aligned}
&\mathbf{A}\mathbf{X}+\mathbf{X}\mathbf{B}=\mathbf{C} \\
\Rightarrow\quad&\operatorname{vec}\left(\mathbf{X}\right)=
\left(\mathbf{I}\otimes\mathbf{A}+\mathbf{B}^{\top}\otimes\mathbf{I}\right)^{-1}
\operatorname{vec}\left(\mathbf{C}\right)
\end{aligned}
\end{equation}

```tex
\documentclass[12pt]{article}
\begin{document}

\begin{equation}
\begin{aligned}
&\mathbf{A}\mathbf{X}+\mathbf{X}\mathbf{B}=\mathbf{C} \\
\Rightarrow\quad&\operatorname{vec}\left(\mathbf{X}\right)=
\left(\mathbf{I}\otimes\mathbf{A}+\mathbf{B}^{\top}\otimes\mathbf{I}\right)^{-1}
\operatorname{vec}\left(\mathbf{C}\right)
\end{aligned}
\end{equation}

\end{document}
```

### 4.5.3 范数

一般而言，代数结构有标量、向量、矩阵、张量这几种，对于这几种代数结构来说，有时候，为了描述数据特征等，会引入范数这个概念。对于向量而言，常用的范数包括$\ell_{0}$范数、$\ell_{1}$范数、$\ell_{2}$范数，具体来说，给定任意向量$\mathbf{x}$，有

- $\ell_{0}$范数为$\left\|\mathbf{x}\right\|_{0}=\sqrt[0]{\sum_{i} x_{i}^{0}}$，代码为`\left\|\mathbf{x}\right\|_{0}=\sqrt[0]{\sum_{i} x_{i}^{0}}`；
- $\ell_{1}$范数为$\left\|\mathbf{x}\right\|_{1}=\sum_{i}|x_{i}|$，代码为`\left\|\mathbf{x}\right\|_{1}=\sum_{i}|x_{i}|`；
- $\ell_{2}$范数为$\left\|\mathbf{x}\right\|_{2}=\sqrt{\sum_{i}x_{i}^{2}}$，代码为`\left\|\mathbf{x}\right\|_{2}=\sqrt{\sum_{i}x_{i}^{2}}`。

对于矩阵而言，常用的范数包括F范数、核范数。给定任意矩阵$\mathbf{X}$，F范数的表达式为$\left\|\mathbf{X}\right\|_{F}$，代码为`\left\|\mathbf{X}\right\|_{F}`；核范数的表达式为$\left\|\mathbf{X}\right\|_{*}$，代码为`\left\|\mathbf{X}\right\|_{*}`。


【**例13**】书写

$$\frac{1}{2}\mathbf{x}^{\top}\mathbf{A}^{\top}\mathbf{A}\mathbf{x}
-\mathbf{x}^{\top}\mathbf{A}^{\top}\mathbf{b}
=\frac{1}{2}\left\|\mathbf{A}\mathbf{x}-\mathbf{b}\right\|_{2}^{2}
-\frac{1}{2}\left\|\mathbf{b}\right\|_{2}^{2}$$

```tex
\documentclass[12pt]{article}
\begin{document}

$$\frac{1}{2}\mathbf{x}^{\top}\mathbf{A}^{\top}\mathbf{A}\mathbf{x}
-\mathbf{x}^{\top}\mathbf{A}^{\top}\mathbf{b}
=\frac{1}{2}\left\|\mathbf{A}\mathbf{x}-\mathbf{b}\right\|_{2}^{2}
-\frac{1}{2}\left\|\mathbf{b}\right\|_{2}^{2}$$

\end{document}
```

【**例14**】书写

\begin{equation}
\begin{aligned}
&\left\|\left[\begin{array}{cc|cc} a_{11} & a_{12} & a_{13} & a_{14} \\
a_{21} & a_{22} & a_{23} & a_{24} \\
\hline a_{31} & a_{32} & a_{33} & a_{34} \\
a_{41} & a_{42} & a_{43} & a_{44} \\
\hline a_{51} & a_{52} & a_{53} & a_{54} \\
a_{61} & a_{62} & a_{63} & a_{64} \\
\end{array}\right]
-\left[\begin{array}{cc} b_{11} & b_{12} \\
b_{21} & b_{22} \\ b_{31} & b_{32} \\
\end{array}\right]\otimes
\left[\begin{array}{cc} c_{11} & c_{12} \\
c_{21} & c_{22} \\ \end{array}\right]\right\|_{F} \\
=&\left\|\left[\begin{array}{cc|cc}
a_{11} & a_{12} & a_{13} & a_{14} \\
a_{21} & a_{22} & a_{23} & a_{24} \\
\hline a_{31} & a_{32} & a_{33} & a_{34} \\
a_{41} & a_{42} & a_{43} & a_{44} \\
\hline a_{51} & a_{52} & a_{53} & a_{54} \\
a_{61} & a_{62} & a_{63} & a_{64} \\
\end{array}\right]
-\left[\begin{array}{c} b_{11} \\ b_{21} \\ b_{31} \\
b_{12} \\ b_{22} \\ b_{32} \\ \end{array}\right]
\otimes\left[\begin{array}{cccc}
c_{11} & c_{21} & c_{12} & c_{22} \\
\end{array}\right]\right\|_{F}
\end{aligned}
\end{equation}

```tex
\documentclass[12pt]{article}
\begin{document}

\begin{equation}
\begin{aligned}
&\left\|\left[\begin{array}{cc|cc} a_{11} & a_{12} & a_{13} & a_{14} \\
a_{21} & a_{22} & a_{23} & a_{24} \\
\hline a_{31} & a_{32} & a_{33} & a_{34} \\
a_{41} & a_{42} & a_{43} & a_{44} \\
\hline a_{51} & a_{52} & a_{53} & a_{54} \\
a_{61} & a_{62} & a_{63} & a_{64} \\
\end{array}\right]
-\left[\begin{array}{cc} b_{11} & b_{12} \\
b_{21} & b_{22} \\ b_{31} & b_{32} \\
\end{array}\right]\otimes
\left[\begin{array}{cc} c_{11} & c_{12} \\
c_{21} & c_{22} \\ \end{array}\right]\right\|_{F} \\
=&\left\|\left[\begin{array}{cc|cc}
a_{11} & a_{12} & a_{13} & a_{14} \\
a_{21} & a_{22} & a_{23} & a_{24} \\
\hline a_{31} & a_{32} & a_{33} & a_{34} \\
a_{41} & a_{42} & a_{43} & a_{44} \\
\hline a_{51} & a_{52} & a_{53} & a_{54} \\
a_{61} & a_{62} & a_{63} & a_{64} \\
\end{array}\right]
-\left[\begin{array}{c} b_{11} \\ b_{21} \\ b_{31} \\
b_{12} \\ b_{22} \\ b_{32} \\ \end{array}\right]
\otimes\left[\begin{array}{cccc}
c_{11} & c_{21} & c_{12} & c_{22} \\
\end{array}\right]\right\|_{F}
\end{aligned}
\end{equation}

\end{document}
```


### 练习题

> 打开LaTeX在线系统[https://www.overleaf.com](https://www.overleaf.com/project)或本地安装好的LaTeX编辑器，创建名为LaTeX_practice的项目，并同时新建一个以`.tex`为拓展名的源文件，完成以下几道练习题。

[1] 书写

\begin{equation}
\boldsymbol{a}=\vec{a}=
\begin{bmatrix}
a_{1} \\
\vdots \\
a_{n} \\
\end{bmatrix}
\end{equation}

```tex
\documentclass[12pt]{article}
\usepackage{amsmath}
\begin{document}

%% 提示：公式中的字符加粗使用\boldsymbol{}命令，带箭头的向量使用\vec{}或者\overrightarrow{}命令
\begin{equation}
% 在此处书写公式
\end{equation}

\end{document}
```

[2] 书写

\begin{equation}
\nabla f(\mathbf{x})=\begin{pmatrix}\frac{\partial f(\mathbf{x})}{\partial x_{1}} \\ \vdots \\ \frac{\partial f(\mathbf{x})}{\partial x_{n}} \\ \end{pmatrix}
\end{equation}

```tex
\documentclass[12pt]{article}
\usepackage{amssymb, amsfonts}
\begin{document}

%% 提示：梯度对应的命令为\nabla
\begin{equation}
% 在此处书写公式
\end{equation}

\end{document}
```


【回放】[**4.4 微积分**](https://nbviewer.jupyter.org/github/xinychen/latex-cookbook/blob/main/chapter-4/section4.ipynb)

【继续】[**4.6 概率论与数理统计**](https://nbviewer.jupyter.org/github/xinychen/latex-cookbook/blob/main/chapter-4/section6.ipynb)

### License

<div class="alert alert-block alert-danger">
<b>This work is released under the MIT license.</b>
</div>
