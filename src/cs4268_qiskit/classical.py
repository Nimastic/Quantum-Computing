from __future__ import annotations

from fractions import Fraction
from math import gcd


def bitstrings(num_bits: int) -> list[str]:
    return [format(value, f"0{num_bits}b") for value in range(2**num_bits)]


def dot_mod2(left: str, right: str) -> int:
    return sum(int(a) * int(b) for a, b in zip(left, right)) % 2


def solve_constraints_mod2(rows: list[str], num_bits: int) -> list[str]:
    return [candidate for candidate in bitstrings(num_bits) if all(dot_mod2(row, candidate) == 0 for row in rows)]


def multiplicative_order(a: int, modulus: int) -> int:
    if gcd(a, modulus) != 1:
        raise ValueError("a and modulus must be coprime to have a multiplicative order")
    value = 1
    for order in range(1, modulus + 1):
        value = (value * a) % modulus
        if value == 1:
            return order
    raise ValueError("No multiplicative order found")


def recover_denominator(measured_value: int, precision: int, limit: int) -> int:
    return Fraction(measured_value, precision).limit_denominator(limit).denominator


def factors_from_order(a: int, modulus: int, order: int) -> tuple[int, int] | None:
    if order % 2 != 0:
        return None
    midpoint = pow(a, order // 2, modulus)
    if midpoint == modulus - 1:
        return None
    left = gcd(midpoint - 1, modulus)
    right = gcd(midpoint + 1, modulus)
    if left in (1, modulus) or right in (1, modulus):
        return None
    return left, right
