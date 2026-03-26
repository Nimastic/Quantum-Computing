"""Lecture 9 companion: idealized period finding for Shor."""

from cmath import exp
from math import pi, sqrt

from qiskit.quantum_info import Statevector

from cs4268_qiskit.classical import multiplicative_order
from cs4268_qiskit.lab_utils import title


def periodic_state(register_size: int, period: int, offset: int = 0) -> Statevector:
    dimension = 2**register_size
    support = list(range(offset, dimension, period))
    amplitude = 1 / sqrt(len(support))
    data = [0j] * dimension
    for index in support:
        data[index] = amplitude
    return Statevector(data)


def exact_dft(state: Statevector) -> Statevector:
    dimension = len(state.data)
    transformed = []
    normalizer = sqrt(dimension)
    for output_index in range(dimension):
        amplitude = sum(
            state.data[input_index] * exp(2j * pi * input_index * output_index / dimension)
            for input_index in range(dimension)
        ) / normalizer
        transformed.append(amplitude)
    return Statevector(transformed)


def main() -> None:
    title("Lecture 9: order finding")

    modulus = 15
    base = 2
    order = multiplicative_order(base, modulus)
    print(f"The classical sequence a^x mod N for a={base}, N={modulus} has order r={order}.")
    for x in range(8):
        print(f"  x={x}: {base}^{x} mod {modulus} = {pow(base, x, modulus)}")

    register_size = 4
    state = periodic_state(register_size=register_size, period=order)
    transformed = exact_dft(state)

    print("\nIdealized periodic superposition support:", list(range(0, 2**register_size, order)))
    print("Exact DFT probabilities of that periodic state:")
    for index, probability in enumerate(transformed.probabilities()):
        if probability > 1e-9:
            print(f"  outcome={index:2d}, probability={probability:.6f}")


if __name__ == "__main__":
    main()
