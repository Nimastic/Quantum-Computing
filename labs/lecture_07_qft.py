"""Lecture 7 companion: hand-built QFT circuits."""

from qiskit import QuantumCircuit

from cs4268_qiskit.builders import manual_qft
from cs4268_qiskit.lab_utils import print_ket_amplitudes, print_probabilities, title


def basis_state(bitstring: str) -> QuantumCircuit:
    circuit = QuantumCircuit(len(bitstring))
    for qubit, bit in enumerate(bitstring):
        if bit == "1":
            circuit.x(qubit)
    return circuit


def main() -> None:
    title("Lecture 7: quantum Fourier transform")

    qft_two = basis_state("10")
    qft_two.compose(manual_qft(2), inplace=True)
    print_ket_amplitudes(qft_two, "QFT acting on |10>")

    qft_three = basis_state("101")
    qft_three.compose(manual_qft(3), inplace=True)
    print_ket_amplitudes(qft_three, "QFT acting on |101>")

    hadamards = basis_state("101")
    hadamards.h(0)
    hadamards.h(1)
    hadamards.h(2)
    print_ket_amplitudes(hadamards, "H⊗3 acting on |101> for comparison")

    round_trip = basis_state("101")
    qft = manual_qft(3)
    round_trip.compose(qft, inplace=True)
    round_trip.compose(qft.inverse(), inplace=True)
    print_probabilities(round_trip, "QFT followed by inverse QFT returns the original basis state", qargs=[0, 1, 2])


if __name__ == "__main__":
    main()

