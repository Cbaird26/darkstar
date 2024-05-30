# quantum_computing.py
from qiskit import QuantumCircuit, transpile, IBMQ, execute, Aer

def initialize_ibmq():
    IBMQ.save_account('526944faf27aeedd952653ff44c8f585f40beb9812cfaca7d4d415ebd4ead190e32ee32ef158ce92c18247d669d2d335bce731f934973d3206b12cf74d91ed2d', overwrite=True)
    provider = IBMQ.load_account()
    return provider

def create_quantum_circuit():
    qc = QuantumCircuit(2, 2)
    qc.h(0)
    qc.cx(0, 1)
    qc.measure([0, 1], [0, 1])
    return qc
