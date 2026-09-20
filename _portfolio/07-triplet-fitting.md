---
title: "triplet-fitting: Gaussian mixture models of nonlinear distortion"
excerpt: "Python package that fits Gaussian mixture models to triplets of transmitted and received symbols from simulated optical links, across launch powers and many runs, to characterise nonlinear signal behaviour."
collection: portfolio
---

**Python · MATLAB engine · scikit-learn · pandas · research code** · [GitHub](https://github.com/esf0/triplet-fitting) · [DOI 10.5281/zenodo.13628611](https://doi.org/10.5281/zenodo.13628611)

In a nonlinear fibre, the distortion of a symbol depends on its neighbours, so the received points are not the simple
Gaussian clouds that standard receivers assume. This package builds datasets of symbol triplets from simulated
transmissions (generated with [hpcom](/portfolio/04-hpcom/)) and fits mixtures of Gaussians to them.

* Dataset builders for triplets across launch powers and independent runs, and a `fit_all` entry point to fit them in bulk.
* EM fitting of Gaussian mixtures through the MATLAB engine and David Barber's BRML toolkit, wrapped behind a Python interface.
* Packaged, tested and archived on Zenodo with a citable version.

Related paper: [Examining nonlinear behaviors in optical communication systems using Gaussian mixture model](/publication/2024-06-20-nonlinear-behaviors-optical-gmm).
