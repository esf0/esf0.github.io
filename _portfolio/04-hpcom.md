---
title: "hpcom: GPU-accelerated optical fibre link simulator"
excerpt: "Open-source Python library for fast, reproducible simulation of coherent optical communication links. Runs the split-step Fourier and Manakov solvers on TensorFlow/GPU, with speed-ups of up to 2000×."
collection: portfolio
---

**Python · TensorFlow · GPU · open source (GPLv3)** · [GitHub](https://github.com/esf0/hpcom) · [PyPI](https://pypi.org/project/hpcom/) · [Docs](https://hpcom.readthedocs.io)

Simulating light propagating through fibre is the bottleneck of most research in optical communications, and it is
even worse when you need millions of labelled examples to train a machine learning model. `hpcom` is the
simulator I wrote for that job at Aston, and it now underpins several of my publications.

* **Fast.** Split-step Fourier and Manakov solvers on TensorFlow/GPU, with simulation speed-ups of up to 2000×.
* **Composable API.** `Transmitter`, `Fiber`, `EDFA`, `Receiver`, `Link` and `Simulation` are validated, frozen dataclasses. Custom link components drop in without plumbing changes.
* **Swappable backends.** A propagator interface sits between the physics and the numerics (NumPy and TensorFlow today; JAX planned).
* **Trustworthy.** Numerical tests pin soliton shape preservation, energy conservation, AWGN BER against theory and digital back-propagation round trips, each with tolerances cited from the literature.
* **Reproducible.** One seed on a `Simulation` splits into independent random streams, so identical seeds give identical results, including amplifier noise.
* **Dataset generation** for ML workflows at scale, and a live demonstration at ECOC 2023 ([paper](/publication/2023-10-01-real-time-demo-hpcom)).
