---
title: "nodes: run heavy jobs on your own PCs"
excerpt: "A small command-line tool that turns a handful of personal GPU machines into a job queue: sync a project, queue a job, follow logs, pull results, all over Tailscale, SSH and rsync."
collection: portfolio
---

**Python · Tailscale · SSH · uv · open source** · [GitHub](https://github.com/esf0/nodes)

Modern machine learning work wants a GPU, but most of us already own several computers. `nodes` lets one machine act
as a control station and treat the others as workers, without installing a cluster scheduler.

* `nodes sync` copies a project (uncommitted changes included, `.gitignore` respected) and builds its `uv` environment on the node.
* `nodes run` queues any bash job on a node. One worker per node runs jobs sequentially, which is what a single GPU wants.
* `nodes ps`, `logs`, `wait`, `cancel` and `pull` follow the job and bring results back.
* Everything goes over Tailscale SSH and rsync, so there is nothing else to install or expose on the network.
* Designed to be driven by people and by AI coding agents alike: state is plain files and exit codes are propagated.
