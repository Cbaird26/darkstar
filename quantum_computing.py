from qiskit import IBMQ

def initialize_ibmq(api_token):
    IBMQ.save_account(api_token, overwrite=True)
    IBMQ.load_account()
    provider = IBMQ.get_provider(hub='ibm-q')
    return provider

def create_quantum_circuit():
    from qiskit import QuantumCircuit
    qc = QuantumCircuit(2)
    qc.h(0)
    qc.cx(0, 1)
    return qc

def extract_features_from_circuit(qc):
    # Dummy feature extraction for the sake of example
    return [len(qc), qc.depth(), qc.size()]
