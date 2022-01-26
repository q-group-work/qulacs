import drawer
from qulacs import QuantumCircuit, ParametricQuantumCircuit
from qulacs.gate import Identity, X, Y, Z, H, S, Sdag, T, Tdag, sqrtX, sqrtXdag, sqrtY, sqrtYdag, CNOT, CZ, SWAP, RX, RY, RZ, Pauli, PauliRotation, U1, U2, U3, DenseMatrix, Measurement, BitFlipNoise, DephasingNoise,  DepolarizingNoise

import matplotlib.pyplot as plt

def sample_circuit():
    circuit = ParametricQuantumCircuit(6)
    circuit.add_X_gate(0)
    circuit.add_Y_gate(0)
    circuit.add_Z_gate(0)
    circuit.add_H_gate(0)
    circuit.add_S_gate(0)
    circuit.add_Sdag_gate(0)
    circuit.add_T_gate(0)
    circuit.add_Tdag_gate(0)
    
    circuit.add_gate(Identity(1))
    circuit.add_gate(H(1))
    circuit.add_gate(X(1))
    circuit.add_gate(Y(1))
    circuit.add_gate(Z(1))
    circuit.add_gate(S(1))
    circuit.add_gate(Sdag(1))
    circuit.add_gate(T(1))
    circuit.add_gate(Tdag(1))
    circuit.add_gate(sqrtX(1))
    circuit.add_gate(sqrtXdag(1))
    circuit.add_gate(RX(1,0.10))
    circuit.add_gate(RY(1,0.20))
    circuit.add_gate(RZ(1,0.30))
    circuit.add_gate(CNOT(1,2))
    circuit.add_gate(SWAP(1,2))
    circuit.add_gate(CZ(1,2))
    return circuit

circuit_qulacs = sample_circuit()
circuit_qiskit = drawer.get_qiskit_circuit(circuit_qulacs)
circuit_qiskit.draw(output="mpl")
plt.show()