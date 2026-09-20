---
title: "nft-processing: nonlinear Fourier transform toolkit"
excerpt: "Python toolkit for forward and inverse nonlinear Fourier transforms, digital back-propagation and windowed processing of long signals, built on a modified FNFT C library."
collection: portfolio
---

**Python · C/C++ · Jupyter · open source** · [GitHub](https://github.com/esf0/nft-processing)

The nonlinear Fourier transform (NFT) decomposes a signal into the modes that propagate independently in a
nonlinear fibre, which makes it a natural tool for both analysing and transmitting signals. This repository is the
code behind much of my PhD work.

* Forward and inverse NFT and digital back-propagation routines, with custom C++ code for discrete eigenvalues.
* Built on modified versions of the FNFT C library and its FNFTpy Python bindings.
* Utilities for windowing long signals, which is the basis of the continuous-signal processing in the papers below.
* Notebooks demonstrating the workflows.

Related papers: [Numerical approaches in NFT-based signal processing](/publication/2024-02-18-numerical-approaches-in-nonlinear-fourier-transform),
[Next-generation signal processing using windowed NFT](/publication/2024-04-09-next-generation-signal-processing-using-windowed-nonlinear-fourier-transform),
[Neural networks for computing and denoising the continuous NFT spectrum](/publication/2021-11-24-neural-networks-for-computing-and-denoising-the-continuous-nonlinear-fourier-spectrum).
