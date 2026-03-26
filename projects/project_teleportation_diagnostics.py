"""Deep project: teleportation diagnostics and branch-by-branch recovery."""

from math import pi, sqrt

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

from cs4268_qiskit.lab_utils import print_probabilities, title


def prepare_message(circuit: QuantumCircuit, qubit: int, label: str) -> None:
    if label == "1":
        circuit.x(qubit)
    elif label == "+":
        circuit.h(qubit)
    elif label == "-":
        circuit.x(qubit)
        circuit.h(qubit)
    elif label == "arbitrary":
        circuit.ry(pi / 3, qubit)
        circuit.rz(pi / 5, qubit)


def undo_message(circuit: QuantumCircuit, qubit: int, label: str) -> None:
    if label == "1":
        circuit.x(qubit)
    elif label == "+":
        circuit.h(qubit)
    elif label == "-":
        circuit.h(qubit)
        circuit.x(qubit)
    elif label == "arbitrary":
        circuit.rz(-pi / 5, qubit)
        circuit.ry(-pi / 3, qubit)


def bell_measurement_stage(label: str) -> QuantumCircuit:
    circuit = QuantumCircuit(3)
    prepare_message(circuit, 0, label)
    circuit.h(1)
    circuit.cx(1, 2)
    circuit.cx(0, 1)
    circuit.h(0)
    return circuit


def branch_bob_state(label: str, outcome: str) -> tuple[float, dict[str, complex]]:
    state = Statevector.from_instruction(bell_measurement_stage(label)).reverse_qargs().to_dict()
    amplitudes = {"0": 0j, "1": 0j}
    probability = 0.0
    for basis_state, amplitude in state.items():
        if basis_state[:2] == outcome:
            amplitudes[basis_state[2]] = complex(amplitude)
            probability += abs(amplitude) ** 2
    normalized = {
        basis_state: amplitude / sqrt(probability)
        for basis_state, amplitude in amplitudes.items()
        if probability > 0
    }
    return probability, normalized


def corrected_branch_state(label: str, outcome: str) -> dict[str, complex]:
    probability, amplitudes = branch_bob_state(label, outcome)
    if probability == 0:
        return {"0": 0j, "1": 0j}

    state = Statevector([amplitudes["0"], amplitudes["1"]])
    correction = QuantumCircuit(1)
    if outcome[1] == "1":
        correction.x(0)
    if outcome[0] == "1":
        correction.z(0)
    corrected = state.evolve(correction).to_dict()
    return {str(key): complex(value) for key, value in corrected.items()}


def deferred_teleportation(label: str) -> QuantumCircuit:
    circuit = bell_measurement_stage(label)
    circuit.cx(1, 2)
    circuit.cz(0, 2)
    undo_message(circuit, 2, label)
    return circuit


def main() -> None:
    title("Deep project: teleportation diagnostics")

    label = "arbitrary"
    bell_stage = bell_measurement_stage(label)
    print_probabilities(bell_stage, "Bell-basis outcome distribution for an arbitrary message state", qargs=[0, 1])

    for outcome in ["00", "01", "10", "11"]:
        probability, pre_correction = branch_bob_state(label, outcome)
        post_correction = corrected_branch_state(label, outcome)
        print(f"\nOutcome {outcome} occurs with probability {probability:.6f}")
        print("  Bob before correction:", pre_correction)
        print("  Bob after correction: ", post_correction)

    for label in ["0", "1", "+", "-", "arbitrary"]:
        verification = deferred_teleportation(label)
        print_probabilities(verification, f"Recovered-state check for |{label}>", qargs=[2])


if __name__ == "__main__":
    main()

