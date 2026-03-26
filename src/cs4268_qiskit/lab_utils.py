from __future__ import annotations

from typing import Iterable

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector


DEFAULT_SHOTS = 2048
DEFAULT_SEED = 7


def title(text: str) -> None:
    line = "=" * len(text)
    print(f"\n{line}\n{text}\n{line}")


def subtitle(text: str) -> None:
    line = "-" * len(text)
    print(f"\n{text}\n{line}")


def statevector_for(circuit: QuantumCircuit) -> Statevector:
    bare_circuit = circuit.remove_final_measurements(inplace=False)
    return Statevector.from_instruction(bare_circuit)


def ordered_statevector_dict(circuit: QuantumCircuit, decimals: int = 3) -> dict[str, complex]:
    state = statevector_for(circuit).reverse_qargs()
    return {str(key): value for key, value in sorted(state.to_dict(decimals=decimals).items())}


def ordered_probabilities(
    circuit: QuantumCircuit,
    qargs: Iterable[int] | None = None,
    decimals: int = 6,
) -> dict[str, float]:
    state = statevector_for(circuit)
    ordered_qargs = list(reversed(list(qargs))) if qargs is not None else list(reversed(range(circuit.num_qubits)))
    probs = state.probabilities_dict(qargs=ordered_qargs, decimals=decimals)
    return {str(key): float(value) for key, value in sorted(probs.items())}


def ordered_counts(
    circuit: QuantumCircuit,
    qargs: Iterable[int] | None = None,
    shots: int = DEFAULT_SHOTS,
    seed: int = DEFAULT_SEED,
) -> dict[str, int]:
    state = statevector_for(circuit)
    state.seed(seed)
    ordered_qargs = list(reversed(list(qargs))) if qargs is not None else list(reversed(range(circuit.num_qubits)))
    counts = state.sample_counts(shots=shots, qargs=ordered_qargs)
    return {str(key): int(value) for key, value in sorted(counts.items())}


def print_ket_amplitudes(circuit: QuantumCircuit, label: str) -> None:
    subtitle(label)
    print(circuit.draw(output="text"))
    print("Amplitudes (shown in q0,q1,... order):")
    for basis_state, amplitude in ordered_statevector_dict(circuit).items():
        print(f"  |{basis_state}>: {amplitude}")


def print_probabilities(
    circuit: QuantumCircuit,
    label: str,
    qargs: Iterable[int] | None = None,
) -> None:
    subtitle(label)
    for basis_state, probability in ordered_probabilities(circuit, qargs=qargs).items():
        print(f"  P({basis_state}) = {probability:.6f}")


def print_counts(
    circuit: QuantumCircuit,
    label: str,
    qargs: Iterable[int] | None = None,
    shots: int = DEFAULT_SHOTS,
) -> None:
    subtitle(label)
    for basis_state, count in ordered_counts(circuit, qargs=qargs, shots=shots).items():
        print(f"  {basis_state}: {count}")
