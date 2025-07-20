---
title: "Neural networks for computing and denoising the continuous nonlinear Fourier spectrum in focusing nonlinear Schrödinger equation"
collection: publications
category: manuscripts
permalink: /publication/2021-11-24-neural-networks-for-computing-and-denoising-the-continuous-nonlinear-fourier-spectrum
excerpt: ''
date: 2021-11-24
venue: 'Scientific Reports | Nature Publishing Group UK'
---
We combine the nonlinear Fourier transform (NFT) signal processing with machine learning methods 
for solving the direct spectral problem associated with the nonlinear Schrödinger equation. 
The latter is one of the core nonlinear science models emerging in a range of applications. 
Our focus is on the unexplored problem of computing the continuous nonlinear Fourier spectrum 
associated with decaying profiles, using a specially-structured deep neural network which we coined NFT-Net. 
The Bayesian optimisation is utilised to find the optimal neural network architecture. 
The benefits of using the NFT-Net as compared to the conventional numerical NFT methods becomes 
evident when we deal with noise-corrupted signals, where the neural networks-based processing 
results in effective noise suppression. This advantage becomes more pronounced when the noise 
level is sufficiently high, and we train the neural network on the noise-corrupted field profiles. 
The maximum restoration quality corresponds to the case where the signal-to-noise ratio of the training 
data coincides with that of the validation signals. Finally, we also demonstrate that the NFT b-coefficient 
important for optical communication applications can be 
recovered with high accuracy and denoised by the neural network with the same architecture.

Download paper [here](http://esf0.github.io/files/publication/neural_networks_for_computing_and_denoising_the_continuous_nonlinear_fourier_spectrum.pdf) or 
[here](https://www.nature.com/articles/s41598-021-02252-9)  
Initial version at [researchsquare](https://assets.researchsquare.com/files/rs-654419/v1_covered.pdf?c=1631871409)

```
@article{sedov2021neural,
  title={Neural networks for computing and denoising the continuous nonlinear Fourier spectrum in focusing nonlinear Schr{\"o}dinger equation},
  author={Sedov, Egor V and Freire, Pedro J and Seredin, Vladimir V and Kolbasin, Vladyslav A and Kamalian-Kopae, Morteza and Chekhovskoy, Igor S and Turitsyn, Sergei K and Prilepsky, Jaroslaw E},
  journal={Scientific Reports},
  volume={11},
  number={1},
  pages={22857},
  year={2021},
  publisher={Nature Publishing Group UK London}
}
```