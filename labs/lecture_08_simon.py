"""Lecture 8 companion: a toy Simon instance with s = 11."""

from qiskit import QuantumCircuit

from cs4268_qiskit.builders import simon_oracle_secret_11
from cs4268_qiskit.classical import solve_constraints_mod2
from cs4268_qiskit.lab_utils import ordered_probabilities, print_counts, print_probabilities, title


def toy_simon_function(bits: str) -> str:
    return f"{(int(bits[0]) ^ int(bits[1]))}0"


def main() -> None:
    title("Lecture 8: Simon's algorithm")

    circuit = QuantumCircuit(4)
    circuit.h(0)
    circuit.h(1)
    circuit.compose(simon_oracle_secret_11(), inplace=True)
    circuit.h(0)
    circuit.h(1)

    print_probabilities(circuit, "Work-register output distribution", qargs=[0, 1])
    print_counts(circuit, "Sampled Simon outputs", qargs=[0, 1], shots=32)

    exact_rows = [
        row
        for row, probability in ordered_probabilities(circuit, qargs=[0, 1]).items()
        if probability > 0 and row != "00"
    ]
    candidates = solve_constraints_mod2(exact_rows, num_bits=2)
    print("\nConstraint rows from the quantum step:", exact_rows)
    print("Solutions to y . s = 0:", candidates)

    secret_candidate = next(candidate for candidate in candidates if candidate != "00")
    print(
        "Collision check:",
        f"f(00) = {toy_simon_function('00')},",
        f"f({secret_candidate}) = {toy_simon_function(secret_candidate)}",
    )
    print(f"Recovered secret: {secret_candidate}")


if __name__ == "__main__":
    main()

