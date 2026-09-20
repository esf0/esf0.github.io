---
title: "Real-time conversational NPCs for VR"
excerpt: "End-to-end AI and voice pipeline for talking NPCs in immersive VR: adaptive voice activity detection, LLM dialogue orchestration and procedural quest generation, at under 500 ms latency."
collection: portfolio
---

**Python · LLMs · speech (STT/TTS/VAD) · distributed backend · commercial project, details confidential**

I was the principal ML engineer for the AI stack of a VR startup that wanted non-player characters to hold real
conversations with players. The hard part is not any single model but keeping the whole loop fast enough to feel like a
person is answering.

* **Latency budget under 500 ms** from the player finishing a sentence to the NPC replying, across speech recognition, language model and synthesis.
* **Adaptive voice activity detection** that copes with noisy, changing environments and decides when the player has really stopped talking.
* **LLM dialogue orchestration** that keeps characters in role and consistent with the scenario.
* **Procedural quest generation** driven by the same language-model stack.
* **Distributed backend and deployment**, including model selection, retrieval, cloud services and latency optimisation, delivered end to end.

I later reused the same building blocks (voice pipelines, RAG, agent orchestration) in consulting projects.
