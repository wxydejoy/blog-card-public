## 9.6 添加参考文献

通常来说，学术汇报的幻灯片时常需要添加与本研究相关的参考文献作为支撑材料。使用LaTeX制作常规文档时，最常用的文献管理工具是Bibtex，但事实上，Beamer并不支持编译Bibtex。因此，拓展名为`.bib`的文献管理文件在Beamer中是无法使用的，不过我们可以使用`\begin{thebibliography} \end{thebibliography}`环境添加参考文献。

在常规文档中，使用LaTeX创建参考文献的简单方式是使用`\begin{thebibliography} \end{thebibliography}`环境添加参考文献。有了参考文献的条目和标签，在正文中使用`\cite{}`命令进行引用便可让参考文献显示出来，这种做法在Beamer中也是适用的。只不过在添加参考文献时，我们需要对文献的类型进行指定，著作对应着`\beamertemplatebookbibitems`命令，而论文则对应着`\beamertemplatearticlebibitems`。需要注意的是，为了避免文献数量过多而导致的参考文献页面排版问题，可以在`\begin{frame}[allowframebreaks] \end{frame}`环境中申明自动跨页。

【**例9-25**】使用`beamer`文档类型创建幻灯片并在`\begin{thebibliography} \end{thebibliography}`环境中创建参考文献。

```tex
\documentclass{beamer}
\usetheme{CambridgeUS}

\begin{document}

\begin{frame}
\frametitle{Reference Example}

If you have any interest in matrix computations, please referring to \cite{golub2013matrix, petersen2008the}.

\end{frame}

\begin{frame}
\frametitle<presentation>{Further Reading}

\begin{thebibliography}{10}

  \beamertemplatebookbibitems
  \bibitem{golub2013matrix}
    Gene H. Golub and Charles F. Van Loan.
    \newblock {\em Matrix computations}.
    \newblock JHU press, 2013.
    
  \beamertemplatearticlebibitems
  \bibitem{petersen2008the}
    Kaare Brandt Petersen, Michael Syskind Pedersen.
    \newblock The matrix cookbook.
    \newblock {\em Technical University of Denmark}, 510, 2008.

\end{thebibliography}

\end{frame}

\end{document}
```

【**例9-26**】使用`beamer`文档类型创建幻灯片并在`\begin{thebibliography} \end{thebibliography}`环境中创建参考文献，其中，需要对幻灯片申明自动跨页。

```tex
\documentclass{beamer}
\usetheme{CambridgeUS}

\begin{document}

\begin{frame}
\frametitle{Reference Example}

If you have any interest in matrix computations, please referring to \cite{golub2013matrix, petersen2008the}.

\end{frame}

\begin{frame}[allowframebreaks]
\frametitle<presentation>{Further Reading}

\begin{thebibliography}{10}

  \beamertemplatebookbibitems
  \bibitem{golub2013matrix}
    Gene H. Golub and Charles F. Van Loan.
    \newblock {\em Matrix computations}.
    \newblock JHU press, 2013.
    
  \beamertemplatearticlebibitems
  \bibitem{petersen2008the}
    Kaare Brandt Petersen, Michael Syskind Pedersen.
    \newblock The matrix cookbook.
    \newblock {\em Technical University of Denmark}, 510, 2008.
    
  \beamertemplatebookbibitems
  \bibitem{golub2013matrix}
    Gene H. Golub and Charles F. Van Loan.
    \newblock {\em Matrix computations}.
    \newblock JHU press, 2013.
    
  \beamertemplatearticlebibitems
  \bibitem{petersen2008the}
    Kaare Brandt Petersen, Michael Syskind Pedersen.
    \newblock The matrix cookbook.
    \newblock {\em Technical University of Denmark}, 510, 2008.
    
  \beamertemplatebookbibitems
  \bibitem{golub2013matrix}
    Gene H. Golub and Charles F. Van Loan.
    \newblock {\em Matrix computations}.
    \newblock JHU press, 2013.
    
  \beamertemplatearticlebibitems
  \bibitem{petersen2008the}
    Kaare Brandt Petersen, Michael Syskind Pedersen.
    \newblock The matrix cookbook.
    \newblock {\em Technical University of Denmark}, 510, 2008.

\end{thebibliography}

\end{frame}

\end{document}
```

【回放】[**9.5 插入程序源代码**](https://nbviewer.jupyter.org/github/xinychen/latex-cookbook/blob/main/chapter-9/section5.ipynb)

【继续】[**9.7 插入表格**](https://nbviewer.jupyter.org/github/xinychen/latex-cookbook/blob/main/chapter-9/section7.ipynb)

### License

<div class="alert alert-block alert-danger">
<b>This work is released under the MIT license.</b>
</div>
