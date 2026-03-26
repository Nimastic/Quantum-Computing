# CS4268 Qiskit Companion

This repo now has two parallel tracks:

- `CS4268_Scribe_Notes/`: your theory-first lecture notes.
- `labs/`: small Qiskit labs that mirror those lectures and turn the math into executable experiments.
- `notebooks/`: generated lecture notebooks and project notebooks.
- `projects/`: deeper follow-on builds for the more algorithm-heavy topics.

The goal is not to replace the theory. The goal is to make each theorem, circuit identity, and algorithm concrete enough that you can predict what the code should do before you run it.

## Setup

Create a virtual environment and install the local package in editable mode:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e .[notebook,noise]
```

The base dependency is `qiskit`. The `notebook` extra gives you Jupyter, and the `noise` extra adds `qiskit-aer` for later noisy-simulation experiments.

## How To Use The Labs

Each file under `labs/` is a notebook-friendly Python script that uses `# %%` cell markers. You can:

- run it as a script: `python labs/lecture_01_qubits.py`
- open it in an editor that understands `# %%` cells
- copy sections into a notebook if you prefer `ipynb`

Actual `.ipynb` versions are generated into `notebooks/` by:

```bash
.venv/bin/python tools/generate_notebooks.py
```

Recommended loop for every lecture:

1. Read the matching scribe notes first.
2. Predict the amplitudes or measurement outcomes on paper.
3. Run the smallest matching lab.
4. Explain any mismatch before moving on.

## Lecture Map

| Lecture | Notes | Lab |
| --- | --- | --- |
| 1 | `Lecture1 Final Notes.tex` | `labs/lecture_01_qubits.py` |
| 2 | `Lecture2 Final Notes.tex` | `labs/lecture_02_bases_and_unitaries.py` |
| 3 | `Lecture3 Final Notes.tex` | `labs/lecture_03_composite_systems.py` |
| 4 | `Lecture4 Final Notes.tex` | `labs/lecture_04_teleportation_and_reversible.py` |
| 5 | `Lecture5 Final Notes.tex` | `labs/lecture_05_primitives.py` |
| 6 | `Lecture6 Final Notes.tex` | `labs/lecture_06_deutsch_jozsa_bv.py` |
| 7 | `Lecture7 Final Notes.tex` | `labs/lecture_07_qft.py` |
| 8 | `Lecture8 Final Notes.tex` | `labs/lecture_08_simon.py` |
| 9 | `Lecture9 Scribe Template.tex` | `labs/lecture_09_order_finding.py` |
| 10 | `Lecture10 Scribe Template.tex` | `labs/lecture_10_shor_scaffold.py` |

More detailed prompts live in `docs/lecture_roadmap.md`.

## Deep Projects

The deeper follow-on scripts live under `projects/` and currently cover:

- teleportation diagnostics
- Bernstein-Vazirani secret sweeps
- a larger Simon toy instance
- a Shor-style factor-15 scaffold

Generated notebook versions of those live under `notebooks/projects/`.

## Structure

```text
docs/                     Study prompts and lecture-by-lecture roadmap
labs/                     One Qiskit lab per lecture
notebooks/                Generated lecture notebooks and project notebooks
projects/                 Deeper follow-on builds
src/cs4268_qiskit/        Reusable helper code for the labs
tools/                    Utility scripts such as notebook generation
CS4268_Scribe_Notes/      Lecture notes from the course
```

## Scope

This companion intentionally stays on the "small executable demos" side:

- single-qubit intuition
- bases and unitaries
- tensor products and Bell states
- no-cloning and teleportation
- uncomputation and phase kickback
- Deutsch, Deutsch-Jozsa, Bernstein-Vazirani
- hand-built QFT
- toy Simon
- idealized order-finding and Shor post-processing

It does not try to be a production quantum SDK project or a full hardware workflow.
