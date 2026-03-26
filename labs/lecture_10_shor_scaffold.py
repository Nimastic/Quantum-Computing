"""Lecture 10 companion: Shor post-processing on a toy factoring example."""

from cs4268_qiskit.classical import factors_from_order, multiplicative_order, recover_denominator
from cs4268_qiskit.lab_utils import title


def main() -> None:
    title("Lecture 10: Shor scaffold")

    modulus = 15
    base = 2
    precision = 16

    order = multiplicative_order(base, modulus)
    print(f"Chosen composite N={modulus}, base a={base}, true multiplicative order r={order}.")

    for measured_value in [8, 4, 12]:
        candidate_order = recover_denominator(measured_value, precision, modulus)
        works = pow(base, candidate_order, modulus) == 1
        print(
            f"Measured value y={measured_value} from a Q={precision} register -> "
            f"candidate denominator {candidate_order} (valid order? {works})"
        )

    recovered_order = recover_denominator(4, precision, modulus)
    factors = factors_from_order(base, modulus, recovered_order)
    print(f"\nUsing the good sample y=4 gives r={recovered_order}.")
    print(f"Nontrivial factors from gcd(a^(r/2) +- 1, N): {factors}")


if __name__ == "__main__":
    main()
