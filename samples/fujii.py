from qulacs import Observable, QuantumCircuit, QuantumState
from qulacs.gate import Y, CNOT, merge


def fujii_sample():
    state = QuantumState(3)
    state.set_zero_state()

    circuit = QuantumCircuit(3)
    circuit.add_X_gate(0)
    circuit.add_H_gate(0)
    circuit.add_H_gate(1)
    circuit.add_CNOT_gate(1,2)
    circuit.update_quantum_state(state)
    print(state)

    observable = Observable(3)
    observable.add_operator(0.44, "X 0")
    value = observable.get_expectation_value(state)
    print(value)
