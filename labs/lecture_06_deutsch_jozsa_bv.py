"""Lecture 6 companion: Deutsch, Deutsch-Jozsa, and Bernstein-Vazirani."""

from qiskit import QuantumCircuit

from cs4268_qiskit.builders import bernstein_vazirani_oracle, xor_oracle
from cs4268_qiskit.lab_utils import print_counts, print_probabilities, title


def deutsch_like_circuit(oracle: QuantumCircuit, num_inputs: int) -> QuantumCircuit:
    circuit = QuantumCircuit(num_inputs + 1)
    ancilla = num_inputs
    circuit.x(ancilla)
    for qubit in range(num_inputs + 1):
        circuit.h(qubit)
    circuit.compose(oracle, inplace=True)
    for qubit in range(num_inputs):
        circuit.h(qubit)
    return circuit


def main() -> None:
    title("Lecture 6: interference as computation")

    deutsch_constant = deutsch_like_circuit(xor_oracle(1, active_bits=[]), num_inputs=1)
    deutsch_balanced = deutsch_like_circuit(xor_oracle(1, active_bits=[0]), num_inputs=1)
    print_probabilities(deutsch_constant, "Deutsch with a constant oracle", qargs=[0])
    print_probabilities(deutsch_balanced, "Deutsch with a balanced oracle", qargs=[0])

    dj_constant = deutsch_like_circuit(xor_oracle(3, active_bits=[]), num_inputs=3)
    dj_balanced = deutsch_like_circuit(xor_oracle(3, active_bits=[0, 1, 2]), num_inputs=3)
    print_probabilities(dj_constant, "Deutsch-Jozsa on a constant 3-bit oracle", qargs=[0, 1, 2])
    print_probabilities(dj_balanced, "Deutsch-Jozsa on a balanced parity oracle", qargs=[0, 1, 2])

    secret = "1011"
    bv_circuit = deutsch_like_circuit(bernstein_vazirani_oracle(secret), num_inputs=len(secret))
    print_probabilities(bv_circuit, f"Bernstein-Vazirani exact output for secret {secret}", qargs=[0, 1, 2, 3])
    print_counts(bv_circuit, "BV sampled output", qargs=[0, 1, 2, 3], shots=32)


if __name__ == "__main__":
    main()

