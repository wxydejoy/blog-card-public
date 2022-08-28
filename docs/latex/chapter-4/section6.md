## 4.6 概率论与数理统计

概率论与数理统计是许多方向开展科学研究的基础，不管是描述客观存在的数据，还是刻画变量之间的关联规则，凭借概率论知识都能得心应手。概率论的数学公式也有其自身特点，本节主要介绍概率论与数理统计范畴内常用的数学公式在LaTeX中的写法。

### 4.6.1 概率论基础

概率论中有一个重要的准则叫做贝叶斯准则，贝叶斯准则的基础为贝叶斯公式，用来描述两个条件概率之间的关系。

【**例1**】书写贝叶斯公式$p\left(\theta\mid y\right)
=\frac{p\left(\theta,y\right)}{p\left(y\right)}
=\frac{p\left(\theta\right)p\left(y\mid\theta\right)}{p\left(y\right)}$和$p\left(\theta\mid y\right)\propto p\left(\theta\right)p\left(y\mid\theta\right)$。

```tex
\documentclass[12pt]{article}
\begin{document}

$$p\left(\theta\mid y\right)
=\frac{p\left(\theta,y\right)}{p\left(y\right)}
=\frac{p\left(\theta\right)p\left(y\mid\theta\right)}{p\left(y\right)}$$
$$p\left(\theta\mid y\right)\propto p\left(\theta\right)p\left(y\mid\theta\right)$$

\end{document}
```
根据贝叶斯公式中的思想，许多机器学习模型的参数可以用贝叶斯算法来求解。

【**例2**】书写$p\left(y\right)=\int p\left(y,\theta\right)d\theta=\int p\left(\theta\right)p\left(y\mid\theta\right)d\theta$。

```tex
\documentclass[12pt]{article}
\begin{document}

$$p\left(y\right)=\int p\left(y,\theta\right)\,d\theta
=\int p\left(\theta\right)p\left(y\mid\theta\right)\,d\theta$$

\end{document}
```

【**例3**】书写期望$\mathbb{E}\left(x\right)=\int xp\left(x\right)dx$与方差$\mathbb{V}\left(x\right)=\int\left(x-\mathbb{E}\left(x\right)\right)^{2}p\left(x\right)dx$。

```tex
\documentclass[12pt]{article}
\begin{document}

$$\mathbb{E}\left(x\right)=\int xp\left(x\right)dx$$
$$\mathbb{V}\left(x\right)=
\int\left(x-\mathbb{E}\left(x\right)\right)^{2}p\left(x\right)dx$$

\end{document}
```

### 4.6.2 概率分布

概率分布，是指用于表述随机变量取值的概率规律，是概率论中最常见的表达式之一。

【**例4**】书写正态分布$x\sim\mathcal{N}\left(\mu,\sigma^{2}\right)$及$p\left(x\right)=\frac{1}{\sqrt{2\pi}\sigma}\exp\left(-\frac{1}{2\sigma^{2}}\left(x-\mu\right)^{2}\right)$。

```tex
\documentclass[12pt]{article}
\begin{document}

$$x\sim\mathcal{N}\left(\mu,\sigma^{2}\right)$$
$$p\left(x\right)=\frac{1}{\sqrt{2\pi}\sigma}
\exp\left(-\frac{1}{2\sigma^{2}}\left(x-\mu\right)^{2}\right)$$

\end{document}
```

【**例5**】书写

\begin{equation}
p(y)=\frac{\operatorname{Poisson}(y\mid\theta)
\operatorname{Gamma}(\theta\mid\alpha,\beta)}
{\operatorname{Gamma}(\theta\mid\alpha+y,1+\beta)}
=\frac{\Gamma(\alpha+y)\beta^{\alpha}}
{\Gamma(\alpha)y!(1+\beta)^{\alpha+y}}
\end{equation}

```tex
\documentclass[12pt]{article}
\begin{document}

\begin{equation}
p(y)=\frac{\operatorname{Poisson}(y\mid\theta)
\operatorname{Gamma}(\theta\mid\alpha,\beta)}
{\operatorname{Gamma}(\theta\mid\alpha+y,1+\beta)}
=\frac{\Gamma(\alpha+y)\beta^{\alpha}}
{\Gamma(\alpha)y!(1+\beta)^{\alpha+y}}
\end{equation}

\end{document}
```

【**例6**】书写

$$\theta\mid y\sim\operatorname{Gamma}\left(\alpha+\sum_{i=1}^{n}y_{i},\beta+\sum_{i=1}^{n}x_{i}\right)$$

```tex
\documentclass[12pt]{article}
\begin{document}

$$\theta\mid y\sim\operatorname{Gamma}\left(\alpha+\sum_{i=1}^{n}y_{i},\beta+\sum_{i=1}^{n}x_{i}\right)$$

\end{document}
```

【**例7**】书写

$$\sigma^{2}\mid y\sim\operatorname{Inv}-\chi^{2}\left(n,s^{2}\right)$$

```tex
\documentclass[12pt]{article}
\begin{document}

$$\sigma^{2}\mid y\sim\operatorname{Inv}-\Chi^{2}\left(n,s^{2}\right)$$

\end{document}
```

【**例8**】书写

$$p\left(\beta\mid\mu_{1},\mu_{2},\tau_{1},\tau_{2},\rho\right)
=\prod_{j=1}^{J}\mathcal{N}\left(\begin{pmatrix}\beta_{1j} \\ \beta_{2j} \end{pmatrix}
\bigg|\begin{pmatrix} \mu_{1} \\ \mu_{2} \end{pmatrix},
\begin{pmatrix} \tau_{1}^{2} & \rho\tau_{1}\tau_{2} \\
\rho\tau_{1}\tau_{2} & \tau_{2}^{2} \end{pmatrix}\right)$$

```tex
\documentclass[12pt]{article}
\begin{document}

$$p\left(\beta\mid\mu_{1},\mu_{2},\tau_{1},\tau_{2},\rho\right)
=\prod_{j=1}^{J}\mathcal{N}\left(\begin{pmatrix}\beta_{1j} \\ \beta_{2j} \end{pmatrix}
\bigg|\begin{pmatrix} \mu_{1} \\ \mu_{2} \end{pmatrix},
\begin{pmatrix} \tau_{1}^{2} & \rho\tau_{1}\tau_{2} \\
\rho\tau_{1}\tau_{2} & \tau_{2}^{2} \end{pmatrix}\right)$$

\end{document}
```

【**例9**】书写

\begin{equation}
\begin{aligned}
y_{ij}&\sim\mathcal{N}\left(\alpha_{j}+x_{ij}\beta_{j},\sigma_{y}^{2}\right) \\
\begin{pmatrix}\alpha \\ \beta \end{pmatrix}&
\sim\mathcal{N}\left(\begin{pmatrix} \mu_{\alpha} \\
\mu_{\beta} \end{pmatrix},
\begin{pmatrix} \sigma_{\alpha}^{2} &
\rho\sigma_{\alpha}\sigma_{\beta} \\
\rho\sigma_{\alpha}\sigma_{\beta} &
\sigma_{\beta}^{2} \end{pmatrix}\right)
\end{aligned}
\end{equation}

```tex
\documentclass[12pt]{article}
\begin{document}

\begin{equation}
\begin{aligned}
y_{ij}&\sim\mathcal{N}\left(\alpha_{j}+x_{ij}\beta_{j},\sigma_{y}^{2}\right) \\
\begin{pmatrix}\alpha \\ \beta \end{pmatrix}&
\sim\mathcal{N}\left(\begin{pmatrix} \mu_{\alpha} \\
\mu_{\beta} \end{pmatrix},
\begin{pmatrix} \sigma_{\alpha}^{2} &
\rho\sigma_{\alpha}\sigma_{\beta} \\
\rho\sigma_{\alpha}\sigma_{\beta} &
\sigma_{\beta}^{2} \end{pmatrix}\right)
\end{aligned}
\end{equation}

\end{document}
```

### 练习题

> 打开LaTeX在线系统[https://www.overleaf.com](https://www.overleaf.com/project)或本地安装好的LaTeX编辑器，创建名为LaTeX_practice的项目，并同时新建一个以`.tex`为拓展名的源文件，完成以下几道练习题。

1. 书写

\begin{equation}
p\left(\alpha,\beta\mid y\right)\propto p\left(\alpha,\beta\right)\prod_{j=1}^{J}\frac{\Gamma\left(\alpha+\beta\right)}{\Gamma\left(\alpha\right)\Gamma\left(\beta\right)}\frac{\Gamma\left(\alpha+y_{j}\right)\Gamma\left(\beta+n_{j}-y_{j}\right)}{\Gamma\left(\alpha+\beta+n_{j}\right)}
\end{equation}

```tex
\documentclass[12pt]{article}
\begin{document}

%% 提示：Gamma函数对应的命令为\Gamma
\begin{equation}
% 在此处书写公式
\end{equation}

\end{document}
```

2. 书写

\begin{equation}
\text{Pr}\left(y_{jt}=1\right)=\operatorname{logit}^{-1}\left(\beta_{0}+\beta_{1}x_{j1}+\beta_{2}x_{j2}+\beta_{3}\left(1-x_{j2}\right)t+\beta_{4}x_{j2}t+\alpha_{j}\right)
\end{equation}

```tex
\documentclass[12pt]{article}
\begin{document}

%% 提示：logit函数对应的命令为\operatorname{logit}
\begin{equation}
% 在此处书写公式
\end{equation}

\end{document}
```

3. 书写

\begin{equation}
p_{i}=\text{Pr}\left(y_{i}^{\text{rep}}<y_{i}\mid y\right)+\frac{1}{2}\text{Pr}\left(y_{i}^{\text{rep}}=y_{i}\mid y\right)
\end{equation}

```tex
\documentclass[12pt]{article}
\begin{document}

\begin{equation}
% 在此处书写公式
\end{equation}

\end{document}
```

4. 书写

\begin{equation}
p\left(\theta\mid x,y_{\text{obs}},I\right)=p\left(\theta\mid x\right)\iint p\left(\phi\mid x,\theta\right)p\left(y\mid x,\theta\right)p\left(I\mid x,y,\phi\right)\,\mathrm{d}y_{\text{mis}}\mathrm{d}\phi
\end{equation}

```tex
\documentclass[12pt]{article}
\begin{document}

\begin{equation}
% 在此处书写公式
\end{equation}

\end{document}
```

5. 书写

\begin{equation}
\log p\left(\theta\mid y\right)=-\frac{1}{2}\sum_{j=1}^{J}\frac{\left(y_{j}-\alpha_{j}\right)^{2}}{\sigma_{j}^{2}}-8\log\tau-\frac{1}{2\tau^{2}}\sum_{j=1}^{J}\left(\alpha_{j}-\mu\right)^{2}+\text{const}
\end{equation}

```tex
\documentclass[12pt]{article}
\begin{document}

%% 提示：log函数对应的命令为\log
\begin{equation}
% 在此处书写公式
\end{equation}

\end{document}
```


【回放】[**4.5 线性代数**](https://nbviewer.jupyter.org/github/xinychen/latex-cookbook/blob/main/chapter-4/section5.ipynb)

【继续】[**4.7 优化理论**](https://nbviewer.jupyter.org/github/xinychen/latex-cookbook/blob/main/chapter-4/section7.ipynb)

### License

<div class="alert alert-block alert-danger">
<b>This work is released under the MIT license.</b>
</div>
