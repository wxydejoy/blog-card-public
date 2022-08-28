## 4.3 希腊字母

我们在初等数学中便已经学习到了一些常用的希腊字母，例如最常见的$\pi$（对应于`\pi`），圆周率$\pi$约等于3.14，圆的面积为$\pi r^{2}$、周长为$2\pi r$。在几何学中，我们习惯用各种希腊字母表示度数，如$\alpha$（对应于`\alpha`）、$\beta$（对应于`\beta`）、$\theta$（对应于`\theta`）、$\phi$（对应于`\phi`）、$\psi$（对应于`\psi`）、$\varphi$（对应于`\varphi`），使用希腊字母既方便，也容易区分于常用的$x,y,z$等其他变量。

实际上，这些希腊字母也可以用来作为变量，在概率论与数理统计中常常出现的变量就包括：

- 正态分布中的$\mu$（命令为`\mu`）、$\sigma$（命令为`\sigma`）；
- 泊松分布中的$\lambda$（命令为`\lambda`）；
- 通常表示自由度的希腊字母为$\nu$(命令为`\nu`)。

另外，在不等式中经常用到的希腊字母有$\delta$（命令为`\delta`）和$\epsilon$（命令为`\epsilon`）。除了这些，希腊字母还有$\gamma$（命令为`\gamma`）、$\eta$（命令为`\eta`）、$\kappa$（命令为`\kappa`）、$\rho$（命令为`\rho`）、$\tau$（命令为`\tau`）和$\omega$（命令为`\omega`）。当然，前面提到的这些希腊字母在用途上并没有严格的界定，很多时候，我们书写数学表达式时可以根据需要选用适当的希腊字母。

【**例1**】书写椭圆$\frac{x^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}=1$的面积公式$S=\pi ab$。

```tex
\documentclass[12pt]{article}
\begin{document}

$$S=\pi ab$$ % 椭圆面积公式

\end{document}
```

【**例2**】书写不等式$a^{\alpha}b^{\beta}\cdots k^{\kappa}l^{\lambda}\leq a\alpha+b\beta+\cdots+k\kappa+l\lambda$。

```tex
\documentclass[12pt]{article}
\begin{document}

$$a^{\alpha}b^{\beta}\cdots k^{\kappa}l^{\lambda}\leq a\alpha+b\beta+\cdots+k\kappa+l\lambda$$

\end{document}
```

【**例3**】书写不等式

$$\phi\left(\frac{x_{1}+x_{2}+\cdots+x_{n}}{n}\right)\leq\frac{\phi\left(x_{1}\right)+\phi\left(x_{2}\right)+\cdots+\phi\left(x_{n}\right)}{n}$$

```tex
\documentclass[12pt]{article}
\begin{document}

$$\phi\left(\frac{x_{1}+x_{2}+\cdots+x_{n}}{n}\right)\leq\frac{\phi\left(x_{1}\right)+\phi\left(x_{2}\right)+\cdots+\phi\left(x_{n}\right)}{n}$$

\end{document}
```

与英文字母类似的是，有些希腊字母不但有小写字母，还有大写字母。有时，根据需要，我们还会对需要斜体的大写字母，具体如下：

- 命令`\Gamma`对应于希腊字母$\Gamma$，命令`\varGamma`对应于$\varGamma$；
- 命令`\Delta`对应于希腊字母$\Delta$，命令`\varDelta`对应于$\varDelta$；
- 命令`\Theta`对应于希腊字母$\Theta$，命令`\varTheta`对应于$\varTheta$；
- 命令`\Lambda`对应于希腊字母$\Lambda$，命令`\varLambda`对应于$\varLambda$；
- 命令`\Pi`对应于希腊字母$\Pi$，命令`\varPi`对应于$\varPi$；
- 命令`\Sigma`对应于希腊字母$\Sigma$，命令`\varSigma`对应于$\varSigma$；
- 命令`\Phi`对应于希腊字母$\Phi$，命令`\varPhi`对应于$\varPhi$；
- 命令`\Omega`对应于希腊字母$\Omega$，命令`\varOmega`对应于$\varOmega$。

从这些大写希腊字母中可以看到：大写希腊字母的命令是将小写希腊字母的命令首字母进行大写，但这些大写希腊字母与小写希腊字母的区别却不仅仅是尺寸不同；当大写希腊字母作为变量时，可以采用斜体字。

【**例4**】书写$\Delta x+\Delta y$和$(i,j,k)\in\Omega$。

```tex
\documentclass[12pt]{article}
\begin{document}

$$\Delta x+\Delta y$$
$$(i,j,k)\in\Omega$$

\end{document}
```


【回放】[**4.2 常用运算符号**](https://nbviewer.jupyter.org/github/xinychen/latex-cookbook/blob/main/chapter-4/section2.ipynb)

【继续】[**4.4 微积分**](https://nbviewer.jupyter.org/github/xinychen/latex-cookbook/blob/main/chapter-4/section4.ipynb)

### License

<div class="alert alert-block alert-danger">
<b>This work is released under the MIT license.</b>
</div>
