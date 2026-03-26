"""Lecture 4 companion: no-cloning, teleportation, and reversible logic."""

from math import pi

from qiskit import QuantumCircuit

from cs4268_qiskit.lab_utils import print_ket_amplitudes, print_probabilities, title


def copier_demo(state_name: str) -> QuantumCircuit:
    circuit = QuantumCircuit(2)
    if state_name == "1":
        circuit.x(0)
    elif state_name == "+":
        circuit.h(0)
    circuit.cx(0, 1)
    return circuit


def main() -> None:
    title("Lecture 4: no-cloning and teleportation")

    for state_name in ["0", "1", "+"]:
        print_ket_amplitudes(copier_demo(state_name), f"CNOT copier attempt starting from |{state_name}>|0>")

    teleport = QuantumCircuit(3)
    theta = pi / 3
    phi = pi / 5

    teleport.ry(theta, 0)
    teleport.rz(phi, 0)

    teleport.h(1)
    teleport.cx(1, 2)

    bell_basis = teleport.copy()
    bell_basis.cx(0, 1)
    bell_basis.h(0)
    print_probabilities(bell_basis, "Alice's Bell-basis measurement probabilities", qargs=[0, 1])

    teleport.cx(0, 1)
    teleport.h(0)
    teleport.cx(1, 2)
    teleport.cz(0, 2)
    teleport.rz(-phi, 2)
    teleport.ry(-theta, 2)
    print_probabilities(teleport, "Bob after inverse state preparation should measure as |0>", qargs=[2])

    reversible_xor = QuantumCircuit(3)
    reversible_xor.x(0)
    reversible_xor.x(1)
    reversible_xor.cx(0, 2)
    reversible_xor.cx(1, 2)
    print_ket_amplitudes(reversible_xor, "Reversible classical XOR: |110> -> |111>")


if __name__ == "__main__":
    main()

