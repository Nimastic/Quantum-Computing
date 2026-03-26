"""Deep project: factor 15 with idealized order finding and Shor post-processing."""

from cmath import exp
from math import pi, sqrt

from qiskit.quantum_info import Statevector

from cs4268_qiskit.classical import factors_from_order, multiplicative_order, recover_denominator
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
    title("Deep project: Shor on N = 15")

    modulus = 15
    precision = 16

    print("Coprime bases and their orders modulo 15:")
    for base in [2, 4, 7, 8, 11, 13, 14]:
        order = multiplicative_order(base, modulus)
        factors = factors_from_order(base, modulus, order)
        print(f"  a={base:2d}, order={order}, factor attempt={factors}")

    base = 2
    order = multiplicative_order(base, modulus)
    transformed = exact_dft(periodic_state(register_size=4, period=order))

    print(f"\nUsing a={base}, the order is r={order}.")
    print("Exact order-finding peaks:")
    peaks = []
    for index, probability in enumerate(transformed.probabilities()):
        if probability > 1e-9:
            peaks.append(index)
            print(f"  outcome={index:2d}, probability={probability:.6f}")

    print("\nPost-processing those peak samples:")
    for measured_value in peaks:
        candidate_order = recover_denominator(measured_value, precision, modulus)
        valid = pow(base, candidate_order, modulus) == 1
        factors = factors_from_order(base, modulus, candidate_order) if valid else None
        print(
            f"  y={measured_value:2d} -> candidate r={candidate_order}, "
            f"valid={valid}, factors={factors}"
        )


if __name__ == "__main__":
    main()

