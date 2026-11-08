window.MathJax = {
  tex: { inlineMath: [["\\(", "\\)"]], displayMath: [["\\[", "\\]"]], processEscapes: true },
  options: { ignoreHtmlClass: ".*|", processHtmlClass: "arithmatex" },
  startup: { pageReady: () => MathJax.startup.defaultPageReady() }
};
if (typeof document$ !== "undefined") document$.subscribe(() => {
  if (window.MathJax?.startup?.promise) MathJax.startup.promise.then(() => {
    MathJax.typesetClear(); MathJax.texReset(); return MathJax.typesetPromise();
  });
});
