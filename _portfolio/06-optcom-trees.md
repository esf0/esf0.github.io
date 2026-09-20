---
title: "optcom-trees: forest-based nonlinear equalisers"
excerpt: "Random forest, gradient boosting and XGBoost models that learn to undo the nonlinear distortion of coherent optical signals from a symbol's neighbours, as a fast, FPGA-friendly alternative to neural-network equalisers."
collection: portfolio
---

**Python · scikit-learn · XGBoost · research code** · [GitHub (master branch)](https://github.com/esf0/optcom-trees/tree/master)

Neural-network equalisers can compensate nonlinear distortion in fibre links, but they are heavy for real-time
hardware. Tree ensembles are a cheap alternative: at inference time they are just a set of comparisons, which maps
naturally onto an FPGA. This code base is where I built and benchmarked them on simulated transmission data.

* Random forest, gradient boosting and XGBoost regressors (and classifiers), trained on simulated received symbols.
* Features built from each symbol's *m* neighbouring symbols, with the target being the nonlinear shift of the received constellation point.
* Works on data simulated with [hpcom](/portfolio/04-hpcom/), with evaluation across launch powers, feature-importance analysis and custom loss experiments.

Related work: [Gradient boosting for nonlinear equalisation](/publication/2023-06-26-gradient-boosting-nonlinear-equalization)
(CLEO/Europe 2023), the [Forest Equalization poster](/talks/2023-02-14-top-conference) (TOP 2023) and my
[PhD thesis](/publication/2023-07-10-phd-thesis-nonlinear-optical).
