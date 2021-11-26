from qulacs import Observable, QuantumCircuit, QuantumState
from qulacs.gate import H, CNOT


def fkobayashi_sample(number_of_pairs=2):
    state = QuantumState(2*number_of_pairs)
    for i in range(number_of_pairs):
        H(i).update_quantum_state(state)
        CNOT(i,i+number_of_pairs).update_quantum_state(state)
    return state