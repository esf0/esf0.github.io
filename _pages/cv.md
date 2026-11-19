---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
  - /experience/
---

{% include base_path %}

Researcher | Machine Learning & Software Engineer | AI Enthusiast

Machine learning and software engineer. PhD in machine learning, 13+ years of C++ and Python.
I build GPU-accelerated models, LLM agent systems and real-time voice and vision pipelines, and take them to production.
I lead the metrology department of a 3D-scanner manufacturer and took its lab to ISO/IEC 17025 accreditation.
See also my [projects](/portfolio/).

Work experience
======

### Team Lead, Metrology Department
**Industrial 3D scanning manufacturer**, Luxembourg · 06/2024 – present

* Built from scratch a GPU digital twin of the full imaging chain (scene, lens and sensor) that combines physics models with machine learning in PyTorch.
* Reached 0.005-0.03 px target accuracy with consumer-grade optics at 100-1000 mm, about 4× better than standard OpenCV calibration.
* Led the metrology lab to ISO/IEC 17025 accreditation. Wrote the procedures, validated the test methods and trained the technical staff.
* Built the C++ and Python software that tests and certifies production 3D scanners to VDI/VDE 2634-3, with traceable, audit-ready certificates.
* Found the root causes of accuracy regressions with planned experiments on calibration targets, focus distance and optics prototypes, and turned the results into engineering decisions.
* Designed and ran Repeatability & Reproducibility studies, from the experiment plan and automated capture to variance analysis and the validation report.
* Designed test fixtures and ran automated capture on robots and stands.
* Run the team day to day, including planning, PR reviews, mentoring and QMS documents. Kept critical work on schedule while key stakeholders were absent.

### AI Enthusiast (independent, part-time)
Remote · 05/2024 – present

* Built LLM automation with LangChain, LlamaIndex, n8n and FastAPI. The pipelines connect language models to CRM, ERP and CI/CD systems.
* Designed multi-agent systems (planner, executor, critic) with retrieval-augmented generation (RAG).
* Added LLM agents to the software process for code review, specifications, test generation and documentation.
* Delivered computer vision and audio models for segmentation, detection, classification and voice activity detection that adapts to background noise.
* Built Telegram and WhatsApp assistants and company knowledge bases on RAG.

### Principal ML Engineer
**Confidential XR/AI startup**, remote · 10/2023 – 05/2024

* Designed and built the AI voice pipeline for real-time talking characters in VR. Response time was under 500 ms.
* Built the distributed backend with adaptive voice detection, LLM dialogue control and procedural quest generation.
* Owned model choice, latency tuning and cloud deployment.

### Researcher & Software Engineer
**Aston Institute of Photonic Technologies**, Birmingham, UK · 10/2020 – 05/2024

* Created [HpCom](https://github.com/esf0/hpcom), an open-source GPU library (TensorFlow, CUDA, JAX) for optical transmission simulation. It runs up to 2000× faster than earlier tools.
* Built a data platform that generates 1,000,000+ data points per minute for machine learning projects.
* Developed ML methods (neural networks, gradient boosting, k-means, PCA) that doubled transmission efficiency on long-haul optical links.
* Published 20+ papers and presented at ECOC, CLEO/Europe, SPIE and IEEE IPC.
* Supervised Master's students and taught 100+ hours of digital signal processing, Python and mathematics.

### Visiting Researcher & Software Engineer (research collaboration)
**Huawei**, Moscow, Russia · 02/2021 – 05/2023

* Built a Python data processing platform on optimised C++ libraries. It ran 60× faster and cut computation time from weeks to hours.
* Developed physics-informed signal processing and ML for links up to 2000 km. Some systems gained up to 10× in performance.
* Wrote cross-platform code for CPU, GPU and TPU, and tested FPGA and ASIC targets with oneAPI and OpenCL.
* Reorganised data and code management, which cut deployment time.

### Researcher & Software Engineer
**Nonlinear Photonics Laboratory**, Novosibirsk, Russia · 09/2016 – 05/2022

* Led a team of 6 scientists and engineers in a 2-year project with a major industrial partner.
* Wrote C++ and Python analysis software for long-distance communication systems that improved system performance by 125%.
* Developed channel analysis methods that are 3× faster and up to 4× more accurate than earlier methods.
* Built distributed simulations with OpenMP and MPI.

### Teaching Assistant (part-time)
**Novosibirsk State University**, Novosibirsk, Russia · 08/2019 – 07/2020

* Taught mathematical analysis and computational physics. All of my students passed.

### Research Intern
**Argon**, Paris, France · 11/2018 – 02/2019

* Built a reinforcement learning agent that beat traditional methods in a supply-chain simulation, and a web demo of it for clients.

### Research Intern
**Deutsches Elektronen-Synchrotron (DESY)**, Hamburg, Germany · 06/2016 – 09/2016

* Optimised the calibration of the Belle II drift chamber, which improved track reconstruction accuracy.

### Research Intern
**Budker Institute of Nuclear Physics**, Novosibirsk, Russia · 07/2013 – 08/2016

* Tested the radiation hardness of CsI(Tl) crystals for the Belle II calorimeter and built an automated measurement setup ([published](/publication/2017-06-26-radiation-hardness-study)).

Education
======

* **PhD, Machine Learning for Optical Communications**, Aston University, Birmingham, UK · 10/2020 – 12/2023  
  Thesis: *Machine learning for performance improvement of long-haul end-to-end optical transmission systems*
* **MEng, Mechanical Engineering and Materials Science**, École des Ponts ParisTech, Paris, France · 09/2017 – 08/2019  
  Diplôme d'ingénieur (double degree with Novosibirsk State University)
* **MSc with honours, Quantum Optics**, Novosibirsk State University, Russia · 09/2016 – 08/2019
* **BSc with honours, High Energy Physics**, Novosibirsk State University, Russia · 09/2012 – 06/2016
* **PhD, Advanced Theory of Optical Communication** (not completed), Novosibirsk State University, Russia · 09/2019 – 05/2022

Skills
======

* **Languages & engineering:** C++, C, Python, SQL, Git, Linux, Docker, CI/CD, distributed systems, code review
* **Machine learning:** PyTorch, TensorFlow, JAX, scikit-learn, computer vision, audio processing, gradient boosting
* **Vision & optics:** digital twins, differentiable optical simulation, camera calibration, photogrammetry, point clouds
* **LLM systems:** RAG, multi-agent systems, LangChain, LlamaIndex, FastAPI, n8n, Claude, Cursor
* **HPC:** CUDA, OpenMP, MPI, oneAPI, OpenCL, GPU optimisation
* **Research:** numerical methods, nonlinear Fourier transform, physics simulation, signal processing
* **Metrology:** ISO/IEC 17025 (accredited lab), VDI/VDE 2634, 3D scanning, 3D printing, CATIA, SolidWorks
* **Spoken languages:** English (fluent), Russian (native), French (working proficiency)

Awards
======

* Scholarship for study abroad, Ministry of Science and Higher Education of the Russian Federation (2020, 2021)
* Hackathon winner, TensorHack (2019)
* Erasmus+ scholarship (2018)
* French Government scholarship (2017)
* BP scholarship (2014, 2015)
* PricewaterhouseCoopers scholarship (2013)

Publications and talks
======

* [Publications](/publications/): journal articles, conference papers, theses and preprints. Also on [Google Scholar]({{ site.author.googlescholar }}) and [ORCID]({{ site.author.orcid }}).
* [Talks](/talks/): conference talks and posters.

Interests
======

Drone piloting, snowboarding, travel.
