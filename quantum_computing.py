from qiskit import QuantumCircuit, transpile, execute, Aer
from qiskit.providers.ibmq import IBMQ

def initialize_ibmq():
    IBMQ.save_account('YOUR_IBM_QUANTUM_ACCOUNT_KEY')
    provider = IBMQ.load_account()
    return provider

def create_quantum_circuit():
    qc = QuantumCircuit(2)
    qc.h(0)
    qc.cx(0, 1)
    return qc
