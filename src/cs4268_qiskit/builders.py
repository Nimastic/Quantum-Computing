from __future__ import annotations

from qiskit import QuantumCircuit


def xor_oracle(num_inputs: int, active_bits: list[int] | None = None, flip_output: bool = False) -> QuantumCircuit:
    """Build |x>|y> -> |x>|y xor f(x)| for a parity-style Boolean function."""
    active_bits = active_bits or []
    circuit = QuantumCircuit(num_inputs + 1, name="Q_f")
    target = num_inputs
    if flip_output:
        circuit.x(target)
    for bit in active_bits:
        circuit.cx(bit, target)
    return circuit


def bernstein_vazirani_oracle(secret: str) -> QuantumCircuit:
    active_bits = [index for index, bit in enumerate(secret) if bit == "1"]
    return xor_oracle(len(secret), active_bits=active_bits)


def simon_oracle_secret_11() -> QuantumCircuit:
    """
    Two-qubit Simon oracle with hidden string s = 11.

    f(x0, x1) = (x0 xor x1, 0)
    so the collisions are:
    00 <-> 11 and 01 <-> 10
    """
    circuit = QuantumCircuit(4, name="O_simon")
    circuit.cx(0, 2)
    circuit.cx(1, 2)
    return circuit


def simon_oracle_secret_101() -> QuantumCircuit:
    """
    Three-qubit Simon oracle with hidden string s = 101.

    f(x0, x1, x2) = (x0 xor x2, x1, 0)
    so the collisions are exactly x and x xor 101.
    """
    circuit = QuantumCircuit(6, name="O_simon_101")
    circuit.cx(0, 3)
    circuit.cx(2, 3)
    circuit.cx(1, 4)
    return circuit


def manual_qft(num_qubits: int, include_swaps: bool = True) -> QuantumCircuit:
    circuit = QuantumCircuit(num_qubits, name=f"QFT_{num_qubits}")
    for target in range(num_qubits):
        circuit.h(target)
        for control in range(target + 1, num_qubits):
            angle = 3.141592653589793 / (2 ** (control - target))
            circuit.cp(angle, control, target)
    if include_swaps:
        for left in range(num_qubits // 2):
            right = num_qubits - left - 1
            circuit.swap(left, right)
    return circuit
