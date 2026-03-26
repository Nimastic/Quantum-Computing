"""Lecture 5 companion: uncomputation, phase kickback, and Hadamard-Walsh."""

from qiskit import QuantumCircuit

from cs4268_qiskit.lab_utils import print_ket_amplitudes, print_probabilities, title


def main() -> None:
    title("Lecture 5: basic primitives")

    compute_copy = QuantumCircuit(4)
    compute_copy.h(0)
    compute_copy.h(1)
    compute_copy.ccx(0, 1, 2)
    compute_copy.cx(2, 3)
    print_probabilities(compute_copy, "Garbage qubit before uncomputation", qargs=[2])

    uncomputed = compute_copy.copy()
    uncomputed.ccx(0, 1, 2)
    print_probabilities(uncomputed, "Garbage qubit after uncomputation", qargs=[2])
    print_probabilities(uncomputed, "Output qubit keeps the copied function value", qargs=[3])

    kickback = QuantumCircuit(3)
    kickback.h(0)
    kickback.h(1)
    kickback.x(2)
    kickback.h(2)
    kickback.ccx(0, 1, 2)
    print_ket_amplitudes(kickback, "Phase kickback for the AND function")

    hadamard_walsh_zero = QuantumCircuit(2)
    hadamard_walsh_zero.h(0)
    hadamard_walsh_zero.h(1)
    print_ket_amplitudes(hadamard_walsh_zero, "H⊗2 acting on |00>")

    hadamard_walsh_input = QuantumCircuit(2)
    hadamard_walsh_input.x(0)
    hadamard_walsh_input.h(0)
    hadamard_walsh_input.h(1)
    print_ket_amplitudes(hadamard_walsh_input, "H⊗2 acting on |10> shows the sign pattern")


if __name__ == "__main__":
    main()

