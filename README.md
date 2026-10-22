<div align="center">
  <img src="docs/assets/promptzilla-mark.svg" alt="PromptZiLLa mark" width="120" />
  <h1>PromptZiLLa</h1>
  <p>
    <strong>LLM prompt-injection research toolkit for structured adversarial testing and model evaluation.</strong>
  </p>
  <p>
    A compact Python package for generating adversarial prompts, cataloging model-specific vulnerability patterns,
    and helping security researchers assess how different LLMs respond to jailbreak-style inputs.
  </p>
</div>

PromptZiLLa is a focused, research-oriented toolkit built around a simple idea: evaluate model resilience against prompt injection, jailbreak framing, and adversarial prompt design in a structured way. The project currently centers on two core elements: a prompt generator and a catalog of representative model families with associated vulnerability vectors.

## At a glance

| Area | Details |
| --- | --- |
| Primary language | Python 3.10+ |
| Package | `promptzilla` |
| Core modules | `src/promptzilla/generator.py`, `src/promptzilla/database.py` |
| Intended use | AI safety testing, red-team prompt generation, model evaluation experiments |
| License | MIT (declared in project metadata) |

## Why this project exists

Large language models are increasingly deployed in settings where prompt handling, instruction hierarchy, and safety filtering matter. PromptZiLLa is designed to support controlled experimentation around those boundaries.

Rather than treating adversarial prompting as a black box, the project organizes the work into a few practical building blocks:

- structured prompt generation for security-oriented testing
- a model reference catalog describing alignment approaches and likely failure modes
- a lightweight research scaffold for extending experiments and reporting findings

This is not a generic application template. It is a focused utility for researchers and security-minded engineers working in AI evaluation and model hardening.

## What the repository contains

The current repository is intentionally compact and clear about scope. It includes the package metadata and the core research primitives:

- `src/promptzilla/generator.py` — generates adversarial prompt variants
- `src/promptzilla/database.py` — stores model metadata and vulnerability vectors
- `pyproject.toml` — Python package metadata and install configuration

This means the project is best understood as a research scaffold and prompt evaluation utility, not a broad SaaS platform or full red-team suite.

## Key capabilities

- Adversarial prompt generation for security and evaluation workflows
- Structured model catalog for comparison across providers and alignment styles
- Lightweight extension point for custom prompt families and evaluations
- Useful starting point for AI safety research, bug-bounty style testing, and experimentation

## How it works

The package is intentionally straightforward:

1. Choose a model entry from the catalog.
2. Generate a prompt variant using the builder utilities.
3. Evaluate the model's response under a controlled prompt scenario.
4. Record the observed attack surface or failure mode.

This makes the project useful for labs, research notes, model testing, and investigating where instruction-following safeguards may break down.

## Installation

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

The package metadata declares Python 3.10+ and installs the core dependency set from `pyproject.toml`.

## Quick start

```python
from promptzilla.database import AI_MODELS_DB
from promptzilla.generator import PromptGenerator

print(AI_MODELS_DB[0]["id"])
print(PromptGenerator.generate_prompt("openai-gpt4o", prompt_type="long"))
```

This demonstrates the repository's current entry points and keeps the workflow focused on concrete prompt generation and model comparison.

## Project structure

```text
.
├── README.md
├── pyproject.toml
├── src/
│   └── promptzilla/
│       ├── __init__.py
│       ├── database.py
│       └── generator.py
└── docs/
    └── assets/
        └── promptzilla-mark.svg
```

## Responsible use

This toolkit is intended for research, security evaluation, and controlled experimentation. Use it responsibly, with explicit permission for any testing environment and in line with applicable legal and organizational policies.

Any prompt generation workflow should be paired with careful review of target usage policies, environment boundaries, and red-team procedures.

## Contributing

Contributions are welcome if they improve the project as a technical research utility:

- add stronger prompt families
- expand the model reference set
- improve evaluation structure and documentation
- refine safety-oriented operational guidance

## License

The project metadata declares an MIT license. If you are packaging or redistributing the repository, verify the repository includes the corresponding license artifact required by your local distribution practices.

---

<div align="center">
  <p><strong>PromptZiLLa</strong> — research tooling for adversarial prompt analysis and LLM safety evaluation.</p>
</div>
