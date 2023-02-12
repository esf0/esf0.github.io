---
title: "Computing continuous nonlinear Fourier spectrum of optical signal with artificial neural networks"
collection: publications
permalink: /publication/2021-08-01-computing-continuous-nonlinear-fourier-spectrum-of-optical-signal-with-artificial-neural-networks
date: 2021-08-01
venue: 'Applications of Machine Learning 2021 | SPIE'
---
In this work, we demonstrate that the high-accuracy computation of the continuous nonlinear spectrum can 
be performed by using artificial neural networks. We propose the artificial neural network (NN) 
architecture that can efficiently perform the nonlinear Fourier (NF) optical signal processing. 
The NN consists of sequential convolution layers and fully connected output layers. 
This NN predicts only one component of the continuous NF spectrum, such that two identical 
NNs have to be used to predict the real and imaginary parts of the reflection coefficient. 
To train the NN, we precomputed 94035 optical signals. 9403 signals were used for validation 
and excluded from training. The final value of the relative error for the entire validation 
dataset was less than 0.3%. Our findings highlight the fundamental possibility of using the NNs to analyze and process 
complex optical signals when the conventional algorithms can fail to deliver an acceptable result.

Download paper [here](http://esf0.github.io/files/computing_continuous_nonlinear_fourier_spectrum_of_optical_signal_with_artificial_neural_networks.pdf) or 
[here](https://doi.org/10.1117/12.2594127)

```
@inproceedings{10.1117/12.2594127,
author = {Egor Sedov and Jaroslaw Prylepskiy and Igor Chekhovskoy and Sergei Turitsyn},
title = {{Computing continuous nonlinear Fourier spectrum of optical signal with artificial neural networks}},
volume = {11843},
booktitle = {Applications of Machine Learning 2021},
editor = {Michael E. Zelinski and Tarek M. Taha and Jonathan Howe},
organization = {International Society for Optics and Photonics},
publisher = {SPIE},
pages = {118430J},
keywords = {Nonlinear Fourier transform, Neural network, Optical communication, Signal processing},
year = {2021},
doi = {10.1117/12.2594127},
URL = {https://doi.org/10.1117/12.2594127}
}
```