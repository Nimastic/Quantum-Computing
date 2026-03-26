"""Deep project: Simon with three work qubits and hidden string 101."""

from itertools import combinations

from qiskit import QuantumCircuit

from cs4268_qiskit.builders import simon_oracle_secret_101
from cs4268_qiskit.classical import solve_constraints_mod2
from cs4268_qiskit.lab_utils import ordered_probabilities, print_counts, print_probabilities, title


def toy_simon_function(bits: str) -> str:
    return f"{int(bits[0]) ^ int(bits[2])}{bits[1]}0"


def select_constraint_rows(rows: list[str], num_bits: int) -> list[str]:
    for candidate_rows in combinations(rows, num_bits - 1):
        solutions = solve_constraints_mod2(list(candidate_rows), num_bits)
        if len(solutions) == 2:
            return list(candidate_rows)
    raise ValueError("Could not find enough independent Simon constraints")


def main() -> None:
    title("Deep project: Simon hidden structure")

    circuit = QuantumCircuit(6)
    for qubit in range(3):
        circuit.h(qubit)
    circuit.compose(simon_oracle_secret_101(), inplace=True)
    for qubit in range(3):
        circuit.h(qubit)

    print_probabilities(circuit, "Simon support for hidden string 101", qargs=[0, 1, 2])
    print_counts(circuit, "Sampled Simon outputs", qargs=[0, 1, 2], shots=64)

    support_rows = [
        row
        for row, probability in ordered_probabilities(circuit, qargs=[0, 1, 2]).items()
        if probability > 0 and row != "000"
    ]
    selected_rows = select_constraint_rows(support_rows, num_bits=3)
    candidates = solve_constraints_mod2(selected_rows, num_bits=3)
    secret_candidate = next(candidate for candidate in candidates if candidate != "000")

    print("\nRows sampled from the orthogonal subspace:", support_rows)
    print("Independent constraint rows used for post-processing:", selected_rows)
    print("Candidates satisfying all constraints:", candidates)
    print(
        "Collision check:",
        f"f(000) = {toy_simon_function('000')},",
        f"f({secret_candidate}) = {toy_simon_function(secret_candidate)}",
    )
    print(f"Recovered secret: {secret_candidate}")


if __name__ == "__main__":
    main()

