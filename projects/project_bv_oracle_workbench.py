"""Deep project: Bernstein-Vazirani secret sweeps and oracle intuition."""

from qiskit import QuantumCircuit

from cs4268_qiskit.builders import bernstein_vazirani_oracle
from cs4268_qiskit.classical import bitstrings
from cs4268_qiskit.lab_utils import ordered_probabilities, print_probabilities, title


def bv_prefix(secret: str) -> QuantumCircuit:
    circuit = QuantumCircuit(len(secret) + 1)
    ancilla = len(secret)
    circuit.x(ancilla)
    for qubit in range(len(secret) + 1):
        circuit.h(qubit)
    circuit.compose(bernstein_vazirani_oracle(secret), inplace=True)
    return circuit


def bv_full(secret: str) -> QuantumCircuit:
    circuit = bv_prefix(secret)
    for qubit in range(len(secret)):
        circuit.h(qubit)
    return circuit


def main() -> None:
    title("Deep project: Bernstein-Vazirani workbench")

    secret = "1011"
    print(f"Classically you need {len(secret)} queries to recover a {len(secret)}-bit secret.")
    print("Quantumly the Bernstein-Vazirani circuit needs one oracle call.")

    exact = bv_full(secret)
    print_probabilities(exact, f"Exact recovery distribution for secret {secret}", qargs=[0, 1, 2, 3])

    print("\nSweeping every 4-bit secret:")
    for secret in bitstrings(4):
        distribution = ordered_probabilities(bv_full(secret), qargs=[0, 1, 2, 3])
        recovered = next(bitstring for bitstring, probability in distribution.items() if probability > 0.999999)
        print(f"  secret={secret} -> recovered={recovered}")


if __name__ == "__main__":
    main()

