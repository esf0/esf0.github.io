---
title: "lens-model: differentiable camera lens model"
excerpt: "A compact PyTorch forward model of a real lens (distortion, field-dependent wavefront, vignetting, radiometry) fitted to images by photometric bundle adjustment, and benchmarked against the classical OpenCV pipeline."
collection: portfolio
---

**Python · PyTorch · optics · computer vision · research in progress, private repository**

Classical camera calibration treats a lens as a few distortion coefficients and locates calibration markers as
blob centroids. On fast or imperfect glass, that ignores the physics: aberrations and vignetting shift the apparent
marker centre by pixels. This project asks how much accuracy a physically grounded model can recover.

* **Ground truth from ray tracing.** A real lens prescription is ray-traced with DeepLens to produce photogrammetry images with known marker positions, including a full sensor noise model.
* **White-box forward model.** Distortion, field-dependent Zernike wavefront, a cat-eye pupil and radiometry, all differentiable in PyTorch.
* **Photometric solver.** Bundle adjustment with a ZNCC curriculum followed by Levenberg-Marquardt over all parameters, evaluated on held-out poses and compared with intensity centroids, ellipse fits and OpenCV reprojection.
* **Rigorous evaluation.** Errors are always reported against several centre conventions (chief ray, zero-tilt, PSF centroid) so a flattering target cannot pass unnoticed. Derivations and measured findings are written up alongside the code.
* Runs are queued on GPU machines with [nodes](/portfolio/03-nodes/).
