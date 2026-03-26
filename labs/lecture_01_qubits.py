"""Lecture 1 companion: qubits, superposition, and measurement."""

from qiskit import QuantumCircuit

from cs4268_qiskit.lab_utils import print_counts, print_ket_amplitudes, print_probabilities, title


def prepare_named_state(name: str) -> QuantumCircuit:
    circuit = QuantumCircuit(1)
    if name == "1":
        circuit.x(0)
    elif name == "+":
        circuit.h(0)
    elif name == "-":
        circuit.x(0)
        circuit.h(0)
    return circuit


def main() -> None:
    title("Lecture 1: bits to qubits")

    for state_name in ["0", "1", "+", "-"]:
        circuit = prepare_named_state(state_name)
        print_ket_amplitudes(circuit, f"State |{state_name}>")
        print_probabilities(circuit, f"Z-basis probabilities for |{state_name}>", qargs=[0])

    hadamard_round_trip = QuantumCircuit(1)
    hadamard_round_trip.h(0)
    hadamard_round_trip.h(0)
    print_ket_amplitudes(hadamard_round_trip, "Applying H twice returns to the starting state")

    plus_state = prepare_named_state("+")
    print_counts(plus_state, "Sampled measurements for |+> in the computational basis", qargs=[0], shots=32)


if __name__ == "__main__":
    main()

