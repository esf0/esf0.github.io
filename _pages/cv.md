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

Researcher | Machine Learning & Software Engineer | AI Consultant

Experienced researcher and software engineer with a strong background in full-cycle software development, including
design, coding, testing and deployment. Skilled in machine learning and coding, with a deep understanding of maths and
physics. Committed to being part of a team that drives new discoveries and builds innovative technology.
See also my [projects](/portfolio/).

Work experience
======

### Team Lead, Metrology Department
**Industrial 3D scanning manufacturer**, Luxembourg · 06/2024 – present

* Lead the verification and certification programme for production 3D scanners, so that results are standards-driven, traceable and audit-ready (VDI/VDE 2634-3, ISO/IEC 17025).
* Build and maintain the internal metrology software stack in C++ and Python: automated processing, test parametrisation, and certificate and report generation.
* Lead cross-functional root-cause investigations of accuracy regressions with hypothesis-driven experiments (recalibration targets, focus and projection distance changes, optics prototypes), and turn the results into engineering decisions.
* Designed and ran repeatability and reproducibility studies: experimental planning, automated data capture, statistical variance decomposition and formal validation reports.
* Developed point-cloud and geometric analysis tools that speed up investigations and make measurements more robust.
* Own metrology end to end: fixtures and experimental setups, automated capture with robots and stands, analysis, and documented conformance procedures.
* Day-to-day engineering leadership: planning, PR reviews, mentoring and QMS documentation.

### Independent AI / ML Consultant (part-time)
05/2024 – present

* Designed automated AI pipelines with LangChain, LlamaIndex, n8n and FastAPI, integrating LLM-based systems into business processes and engineering workflows, including CI/CD.
* Architected multi-agent systems with structured roles (planner / executor / critic) and retrieval-augmented generation, connected to external APIs, CRM and ERP systems.
* Built AI-augmented development pipelines with LLM agents for code review, specification drafting, automated testing, documentation and refactoring.
* Delivered applied ML in computer vision and audio: segmentation, feature extraction, classification, detection, and environment-adaptive voice activity detection (VAD).
* Built LLM assistants for Telegram and WhatsApp and enterprise knowledge systems with scalable RAG architectures.

### Principal ML Engineer
**Confidential XR/AI startup**, remote · 10/2023 – 05/2024

* Designed and built the full AI and voice interaction pipeline for real-time NPCs in immersive VR, with conversational latency under 500 ms.
* Implemented the distributed backend: adaptive VAD, LLM-based dialogue orchestration and a procedural quest generation engine.
* Owned model selection, orchestration logic, latency optimisation and deployment strategy across model layer, retrieval, backend services and cloud.

### Researcher & Software Engineer
**Aston Institute of Photonic Technologies**, Birmingham, UK · 10/2020 – 05/2024

* Developed [hpcom](https://github.com/esf0/hpcom), an open-source simulation library for optical signal transmission with speed-ups of up to 2000×.
* Built a data platform for optical-communication machine learning that generates over 1,000,000 data points per minute and supports several research projects.
* Built a machine learning platform that roughly doubled the efficiency of long-distance optical transmission in simulation.
* Contributed to a new software model for improving optical communication systems.
* Supervised several Master's students on research projects.
* Delivered 100+ hours of practical classes in digital signal processing, Python and mathematics for Bachelor students.

### Visiting Researcher & Software Engineer (collaboration)
**Huawei**, Moscow, Russia · 02/2021 – 05/2023

* Built a data processing platform in Python on top of optimised C++ libraries, a 60× speed-up that cut computation from weeks to hours.
* Developed and validated physics-informed signal processing and machine learning methods for transmission over distances of up to 2000 km, with up to a 10× performance gain in some systems.
* Streamlined code and data management, which shortened software deployment time.

### Researcher & Software Engineer
**Nonlinear Photonics Laboratory**, Novosibirsk, Russia · 09/2016 – 05/2022

* Led a team of 6 scientists and engineers through a 2-year collaboration with a corporate partner.
* Developed software for analysing complex data in long-distance communication systems (125% system performance improvement).
* Developed methods for analysing optical channel dynamics: 3× faster computation and up to 4× better reconstruction accuracy than earlier techniques.
* Research on optical signal characteristics led to two publications and presentations at five major conferences.

### Teaching Assistant (part-time)
**Novosibirsk State University**, Russia · 08/2019 – 07/2020

* Practical classes in mathematical analysis and computational physics for Bachelor students.

### Research Internship
**Argon**, Paris, France · 11/2018 – 02/2019

* Built a reinforcement-learning algorithm that improved supply-chain performance in simulation, and a web platform to demonstrate it.

### Research Internship
**Deutsches Elektronen-Synchrotron (DESY)**, Hamburg, Germany · 06/2016 – 09/2016

* Developed multidimensional parameter optimisation for calibrating the Central Drift Chamber of the Belle II experiment, improving track reconstruction accuracy and resolution.

### Research Internship
**Budker Institute of Nuclear Physics**, Novosibirsk, Russia · 07/2013 – 08/2016

* Studied the radiation hardness of scintillation crystals for the Belle II calorimeter and built an automated measurement setup ([published](/publication/2017-06-26-radiation-hardness-study)).

Education
======

* **PhD, Machine Learning in Optical Communication**, Aston University, UK
* **PhD, Advanced Theory of Optical Communication**, Novosibirsk State University, Russia (incomplete)
* **Engineering degree, Mechanical Engineering and Materials Science**, École des Ponts ParisTech, France
* **Master with honours, Quantum Optics**, Novosibirsk State University, Russia
* **Bachelor with honours, High Energy Physics**, Novosibirsk State University, Russia

Skills
======

* **Software development:** C, C++, Python, Docker, Git, Linux, distributed systems, HPC (CUDA, OpenMP, MPI), CI/CD, code review, full SDLC
* **Machine learning and AI:** PyTorch, TensorFlow, JAX, scikit-learn, LLM systems, RAG, multi-agent architectures, computer vision, audio processing, numerical methods, physics simulation
* **AI tooling:** LangChain, LlamaIndex, FastAPI, n8n, prompt engineering, AI-augmented SDLC
* **Hardware and metrology:** 3D scanning, 3D printing, CATIA, SolidWorks, mechanical prototyping
* **Languages:** English (fluent), Russian (native), French (working proficiency)

Awards
======

* Scholarship for Abroad Studies, Ministry of Science and Higher Education of the Russian Federation (2020, 2021)
* Hackathon winner, TensorHack (2019)
* Erasmus+ scholarship (2018); French Government scholarship (2017)
* BP scholarship (2014, 2015); PricewaterhouseCoopers scholarship (2013)

Publications
======
  <ul>{% for post in site.publications reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>

Talks
======
  <ul>{% for post in site.talks reversed %}
    {% include archive-single-talk-cv.html  %}
  {% endfor %}</ul>
