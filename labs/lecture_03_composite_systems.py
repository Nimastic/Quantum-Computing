"""Lecture 3 companion: tensor products, Bell states, and marginals."""

from qiskit import QuantumCircuit

from cs4268_qiskit.lab_utils import print_counts, print_ket_amplitudes, print_probabilities, title


def main() -> None:
    title("Lecture 3: composite systems")

    product_state = QuantumCircuit(2)
    product_state.h(0)
    product_state.x(1)
    print_ket_amplitudes(product_state, "Product state |+1>")
    print_probabilities(product_state, "Joint probabilities for |+1>", qargs=[0, 1])

    bell_state = QuantumCircuit(2)
    bell_state.h(0)
    bell_state.cx(0, 1)
    print_ket_amplitudes(bell_state, "Bell state from H on q0 followed by CX(0, 1)")
    print_probabilities(bell_state, "Bell-state joint probabilities", qargs=[0, 1])
    print_probabilities(bell_state, "Bell-state marginal on q0", qargs=[0])
    print_probabilities(bell_state, "Bell-state marginal on q1", qargs=[1])
    print_counts(bell_state, "Bell-state sampled outcomes", qargs=[0, 1], shots=32)


if __name__ == "__main__":
    main()

