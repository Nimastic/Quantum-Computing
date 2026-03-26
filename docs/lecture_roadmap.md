# Lecture Roadmap

Use this as the bridge between the lecture notes and the lab scripts.

## Lecture 1

- Notes: `CS4268_Scribe_Notes/Lecture1 Final Notes.tex`
- Lab: `labs/lecture_01_qubits.py`
- Focus: basis states, superposition, measurement, vector intuition
- Predict first:
  - What `H|0>` should look like as amplitudes
  - Why `HH|0> = |0>`

## Lecture 2

- Notes: `CS4268_Scribe_Notes/Lecture2 Final Notes.tex`
- Lab: `labs/lecture_02_bases_and_unitaries.py`
- Focus: bra-ket notation, basis changes, unitary gates, phase
- Predict first:
  - Why `|+>` is deterministic in the X basis but random in the Z basis
  - Why `Z|+> = |->` even though Z-basis probabilities do not change

## Lecture 3

- Notes: `CS4268_Scribe_Notes/Lecture3 Final Notes.tex`
- Lab: `labs/lecture_03_composite_systems.py`
- Focus: tensor products, Bell states, entanglement, subsystem behavior
- Predict first:
  - The basis ordering of `|01>` and `|10>`
  - Why Bell-state marginals are uniform even though joint outcomes are correlated

## Lecture 4

- Notes: `CS4268_Scribe_Notes/Lecture4 Final Notes.tex`
- Lab: `labs/lecture_04_teleportation_and_reversible.py`
- Focus: no-cloning, teleportation, reversible classical logic inside quantum circuits
- Predict first:
  - Why a CNOT "copies" `|0>` and `|1>` but fails on `|+>`
  - Why Bob recovers the state only after the correction stage

## Lecture 5

- Notes: `CS4268_Scribe_Notes/Lecture5 Final Notes.tex`
- Lab: `labs/lecture_05_primitives.py`
- Focus: uncomputation, phase kickback, Hadamard-Walsh transform
- Predict first:
  - Which ancilla should return to `|0>` after uncomputation
  - Which basis state picks up a minus sign in the phase-kickback demo

## Lecture 6

- Notes: `CS4268_Scribe_Notes/Lecture6 Final Notes.tex`
- Lab: `labs/lecture_06_deutsch_jozsa_bv.py`
- Focus: interference as computation
- Predict first:
  - Why Deutsch distinguishes constant vs balanced in one query
  - Why BV returns the secret string exactly

## Lecture 7

- Notes: `CS4268_Scribe_Notes/Lecture7 Final Notes.tex`
- Lab: `labs/lecture_07_qft.py`
- Focus: QFT as a structured phase transform
- Predict first:
  - How QFT differs from just applying `H` gates in parallel
  - Why swaps appear at the end of the standard QFT circuit

## Lecture 8

- Notes: `CS4268_Scribe_Notes/Lecture8 Final Notes.tex`
- Lab: `labs/lecture_08_simon.py`
- Focus: hidden structure, linear constraints, hybrid quantum-classical workflow
- Predict first:
  - Which output strings satisfy `y . s = 0`
  - Why the quantum circuit gives constraints instead of the full answer immediately

## Lecture 9

- Notes: `CS4268_Scribe_Notes/Lecture9 Scribe Template.tex`
- Lab: `labs/lecture_09_order_finding.py`
- Focus: periodicity and the period-finding view of Shor
- Predict first:
  - The period of `a^x mod N` for the chosen toy example
  - Where the QFT should place the probability peaks

## Lecture 10

- Notes: `CS4268_Scribe_Notes/Lecture10 Scribe Template.tex`
- Lab: `labs/lecture_10_shor_scaffold.py`
- Focus: continued fractions, order recovery, turning period data into factors
- Predict first:
  - Why even order matters
  - Why `gcd(a^(r/2) +- 1, N)` can reveal nontrivial factors

