"""Lecture 2 companion: basis changes, phase, and unitary gates."""

from math import pi

from qiskit import QuantumCircuit

from cs4268_qiskit.lab_utils import print_ket_amplitudes, print_probabilities, title


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
    title("Lecture 2: bases and unitaries")

    for state_name in ["0", "1", "+", "-"]:
        z_basis = prepare_named_state(state_name)
        x_basis = prepare_named_state(state_name)
        x_basis.h(0)

        print_probabilities(z_basis, f"|{state_name}> measured in the Z basis", qargs=[0])
        print_probabilities(x_basis, f"|{state_name}> measured in the X basis via H then Z-measurement", qargs=[0])

    phase_demo = QuantumCircuit(1)
    phase_demo.h(0)
    phase_demo.z(0)
    print_ket_amplitudes(phase_demo, "Relative phase demo: Z|+> = |->")

    inverse_demo = QuantumCircuit(1)
    inverse_demo.ry(pi / 7, 0)
    inverse_demo.rz(pi / 5, 0)
    inverse_demo.rz(-pi / 5, 0)
    inverse_demo.ry(-pi / 7, 0)
    print_ket_amplitudes(inverse_demo, "Gate followed by inverse returns to |0>")

    clifford_demo = QuantumCircuit(1)
    clifford_demo.h(0)
    clifford_demo.s(0)
    clifford_demo.sdg(0)
    clifford_demo.t(0)
    clifford_demo.tdg(0)
    print_ket_amplitudes(clifford_demo, "S and T inverse pairs cancel cleanly")


if __name__ == "__main__":
    main()

