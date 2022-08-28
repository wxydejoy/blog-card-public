## 4.4 微积分

事实上，数学公式的范畴极为广泛，我们所熟知的大学数学课程中，微积分、线性代数、概率论与数理统计中数学表达式的符号系统均大不相同。本节将主要介绍如何使用LaTeX对微积分中的数学表达式进行书写和编译。

### 4.4.1 极限

求极限是整个微积分中的基石，例如$\lim_{x\to 2}x^{2}$对应的LaTeX代码为`$\lim_{x\to 2}x^{2}$`。

【**例1**】书写以下求极限的表达式：

$$\lim_{x\to-\infty}\frac{3x^{2}-2}{3x-2x^{2}}=\lim_{x\to-\infty}\frac{x^{2}\left(3-\frac{2}{x^{2}}\right)}{x^{2}\left(\frac{3}{x}-2\right)}=\lim_{x\to-\infty}\frac{3-\frac{2}{x^{2}}}{\frac{3}{x}-2}=-\frac{3}{2}$$

```tex
\documentclass[12pt]{article}
\begin{document}

$$\lim_{x\to-\infty}\frac{3x^{2}-2}{3x-2x^{2}}=\lim_{x\to-\infty}\frac{x^{2}\left(3-\frac{2}{x^{2}}\right)}{x^{2}\left(\frac{3}{x}-2\right)}=\lim_{x\to-\infty}\frac{3-\frac{2}{x^{2}}}{\frac{3}{x}-2}=-\frac{3}{2}$$

\end{document}
```

【**例2**】书写极限$\lim_{\Delta t\to0}\frac{s(t+\Delta t)+s(t)}{\Delta t}$和$\displaystyle{\lim_{\Delta t\to0}\frac{s(t+\Delta t)+s(t)}{\Delta t}}$。

```tex
\documentclass[12pt]{article}
\begin{document}

$\lim_{\Delta t\to0}\frac{s(t+\Delta t)+s(t)}{\Delta t}$ \& $\displaystyle{\lim_{\Delta t\to0}\frac{s(t+\Delta t)+s(t)}{\Delta t}}$

\end{document}
```

### 4.4.2 导数

在微积分中，给定函数$f(x)$后，我们能够将其导数定义为

$$f^\prime(a)=\lim_{x\to a}\frac{f(x)-f(a)}{x-a}$$

用LaTeX书写这条公式为`$$f^\prime(a)=\lim_{x\to a}\frac{f(x)-f(a)}{x-a}$$`，有时候，为了让分数的形式在直观上不显得过大，可以用`$$f^\prime(a)=\lim\limits_{x\to a}\frac{f(x)-f(a)}{x-a}$$`，其中，`\lim`和`\limits`两个命令需要配合使用。

需要注意的是，`f^\prime(x)`中的`\prime`命令是标准写法，有时候也可以写作`f'(x)`。

【**例3**】使用`\prime`命令书写导数的定义$f^\prime(x)=\lim_{\Delta x\to 0}\frac{f(x+\Delta x)-f(x)}{\Delta x}$。

```tex
\documentclass[12pt]{article}
\begin{document}

$$f^\prime(x)=\lim_{\Delta x\to 0}\frac{f(x+\Delta x)-f(x)}{\Delta x}$$

\end{document}
```

【**例4**】书写函数$f(x)=3x^{5}+2x^{3}+1$的导数$f^\prime(x)=15x^{4}+6x^{2}$。

```tex
\documentclass[12pt]{article}
\begin{document}

$$f^\prime(x)=15x^{4}+6x^{2}$$

\end{document}
```

微分在微积分中举足轻重，`\mathrm{d}`为微分符号$\mathrm{d}$的命令，一般而言，微分的标准写法为$\frac{\mathrm{d}^{n}}{\mathrm{d}x^{n}}f(x)$。

【**例5**】书写微分$\frac{\mathrm{d}}{\mathrm{d}x}f(x)=15x^{4}+6x^{2}$、$\frac{\mathrm{d}^{2}}{\mathrm{d}^{2}x}f(x)=60x^{3}+12x$。

```tex
\documentclass[12pt]{article}
\begin{document}

$$\frac{\mathrm{d}}{\mathrm{d}x}f(x)=15x^{4}+6x^{2}$$
$$\frac{\mathrm{d}^{2}}{\mathrm{d}^{2}x}f(x)=60x^{3}+12x$$

\end{document}
```

在微积分中，偏微分符号$\partial$的命令为`\partial`，对于任意函数$f(x,y)$，偏微分的标准写法为$\frac{\partial^{n}}{\partial x^{n}}f(x,y)$或$\frac{\partial^{n}}{\partial y^{n}}f(x,y)$。

【**例6**】书写函数$f(x,y)=3x^{5}y^{2}+2x^{3}y+1$的偏微分$\frac{\partial}{\partial x}f(x,y)=15x^{4}y^{2}+6x^{2}y$和$\frac{\partial}{\partial y}f(x,y)=6x^{5}y+2x^{3}$。

```tex
\documentclass[12pt]{article}
\begin{document}

$$\frac{\partial}{\partial x}f(x,y)=15x^{4}y^{2}+6x^{2}y$$
$$\frac{\partial}{\partial y}f(x,y)=6x^{5}y+2x^{3}$$

\end{document}
```

【**例7**】书写偏导数$z=\mu\,\frac{\partial y}{\partial x}\bigg|_{x=0}$。

```tex
\documentclass[12pt]{article}
\begin{document}

$$z=\mu\,\frac{\partial y}{\partial x}\bigg|_{x=0}$$

\end{document}
```


### 4.4.3 积分

积分的标准写法为$\int_{a}^{b}f(x)\,\mathrm{d}x$，代码为`\int_{a}^{b}f(x)\,\mathrm{d}x`，其中，`\int`表示积分，是英文单词integral的缩写形式，使用`\,`的目的是引入一个空格。

【**例8**】书写积分$\int\frac{\mathrm{d}x}{\sqrt{a^{2}+x^{2}}}=\frac{1}{a}\arcsin\left(\frac{x}{a}\right)+C$和$\int\tan^{2}x\,\mathrm{d}x=\tan x-x+C$。

```tex
\documentclass[12pt]{article}
\begin{document}

$$\int\frac{\mathrm{d}x}{\sqrt{a^{2}+x^{2}}}=\frac{1}{a}\arcsin\left(\frac{x}{a}\right)+C$$
$$\int\tan^{2}x\,\mathrm{d}x=\tan x-x+C$$

\end{document}
```

【**例9**】书写积分$\int_{a}^{b}\left[\lambda_{1}f_{1}(x)+\lambda_{2}f_{2}(x)\right]\,\mathrm{d}x=\lambda_{1}\int_{a}^{b}f_{1}(x)\,\mathrm{d}x+\lambda_{2}\int_{a}^{b}f_{2}(x)\,\mathrm{d}x$和$\int_{a}^{b}f(x)\,\mathrm{d}x=\int_{a}^{c}f(x)\,\mathrm{d}x+\int_{c}^{b}f(x)\,\mathrm{d}x$。

```tex
\documentclass[12pt]{article}
\begin{document}

$$\int_{a}^{b}\left[\lambda_{1}f_{1}(x)+\lambda_{2}f_{2}(x)\right]\,\mathrm{d}x=\lambda_{1}\int_{a}^{b}f_{1}(x)\,\mathrm{d}x+\lambda_{2}\int_{a}^{b}f_{2}(x)\,\mathrm{d}x$$
$$\int_{a}^{b}f(x)\,\mathrm{d}x=\int_{a}^{c}f(x)\,\mathrm{d}x+\int_{c}^{b}f(x)\,\mathrm{d}x$$

\end{document}
```

【**例10**】书写积分

\begin{equation}
\begin{aligned}
V &=2\pi\int_{0}^{1} x\left[1-(x-1)^{2}\right]\,\mathrm{d}x \\
&=2\pi\int_{0}^{2}\left[-x^{3}+2 x^{2}\right]\,\mathrm{d}x \\
&=2\pi\left[-\frac{1}{4} x^{4}+\frac{2}{3} x^{3}\right]_{0}^{2} \\
&=8\pi/3
\end{aligned}
\end{equation}

```tex
\documentclass[12pt]{article}
\begin{document}

\begin{equation}
\begin{aligned}
V&=2\pi\int_{0}^{1} x\left\{1-(x-1)^{2}\right\}\,\mathrm{d}x \\
&=2\pi\int_{0}^{2}\left\{-x^{3}+2 x^{2}\right\}\,\mathrm{d}x \\
&=2\pi\left[-\frac{1}{4} x^{4}+\frac{2}{3} x^{3}\right]_{0}^{2} \\
&=8\pi/3
\end{aligned}
\end{equation}

\end{document}
```

上述介绍的都是一重积分，在微积分课程中，还有二重积分、三重积分等，对于一重积分，LaTeX提供的基本命令为`\int`，二重积分为`\iint`，三重积分为`\iiint`、四重积分为`\iiiint`，当积分为五重或以上时，一般使用`\idotsint`，即$\idotsint$。

【**例11**】书写积分$\iint\limits_{D}f(x,y)\,\mathrm{d}\sigma$和$\iiint\limits_{\Omega}\left(x^{2}+y^{2}+z^{2}\right)\,\mathrm{d}v$。

```tex
\documentclass[12pt]{article}
\begin{document}

$$\iint\limits_{D}f(x,y)\,\mathrm{d}\sigma$$
$$\iiint\limits_{\Omega}\left(x^{2}+y^{2}+z^{2}\right)\,\mathrm{d}v$$

\end{document}
```

在积分中，有一种特殊的积分符号是在标准的积分符号上加上一个圈，可用来表示计算曲线曲面积分，即$\oint_{C}f(x)\,\mathrm{d}x+g(y)\,\mathrm{d}y$，代码为`\oint_{C}f(x)\,\mathrm{d}x+g(y)\,\mathrm{d}y`。

### 练习题

> 打开LaTeX在线系统[https://www.overleaf.com](https://www.overleaf.com/project)或本地安装好的LaTeX编辑器，创建名为LaTeX_practice的项目，并同时新建一个以`.tex`为拓展名的源文件，完成以下几道练习题。

[1] 书写泰勒展开式

\begin{equation}
\begin{aligned}
f\left(x\right)=&\frac{f\left(x_{0}\right)}{0!}+\frac{f'\left(x_{0}\right)}{1!}\left(x-x_{0}\right)^{2} \\
&+\cdots+\frac{f^{\left(n\right)}\left(x_{0}\right)}{n!}\left(x-x_{0}\right)^{n}+R_{n}\left(x\right)
\end{aligned}
\end{equation}

```tex
\documentclass[12pt]{article}
\begin{document}

\begin{equation}
\begin{aligned}
% 在此处书写公式
\end{aligned}
\end{equation}

\end{document}
```

【回放】[**4.3 希腊字母**](https://nbviewer.jupyter.org/github/xinychen/latex-cookbook/blob/main/chapter-4/section3.ipynb)

【继续】[**4.5 线性代数**](https://nbviewer.jupyter.org/github/xinychen/latex-cookbook/blob/main/chapter-4/section5.ipynb)

### License

<div class="alert alert-block alert-danger">
<b>This work is released under the MIT license.</b>
</div>
