# Agentic Platform Lab

A sandbox for exploring how agentic systems and AI-augmented tools can support internal developer platforms.

## What’s Here

- Experiments using CNOE + PocketIDP templates on Coder
- GitOps with ArgoCD, Helm, Kubernetes
- Conceptual architecture for a future agentic platform

## Status

This is an evolving lab — expect rough edges.

---

## Currently Exploring

- Prompt-driven self-service workflows
- AI summaries of ArgoCD sync logs
- Minimal agent loops to observe/recommend changes
- “Vibe coding” tools for internal tooling

## Tools & Technologies

- Kubernetes (via CNOE)
- ArgoCD / Helm / GitOps
- ChatGPT / Copilot
- Replit, Coder

## Try It Out

This repo includes a real script to generate a Kubernetes Deployment YAML file:

**`generate_helm_yaml.py`**

```bash
python generate_helm_yaml.py
```

This will create a file named `node-app-deploy.yaml` in the current folder — ready to be used with `kubectl apply -f` or included in a Helm chart.
