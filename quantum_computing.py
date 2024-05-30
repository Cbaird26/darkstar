from qiskit import QuantumCircuit, IBMQ

def initialize_ibmq(api_token):
    IBMQ.save_account(api_token, overwrite=True)
    IBMQ.load_account()
    provider = IBMQ.get_provider(hub='ibm-q')
    return provider

def create_quantum_circuit(num_qubits=2, depth=3):
    qc = QuantumCircuit(num_qubits)
    for _ in range(depth):
        for qubit in range(num_qubits):
            qc.h(qubit)
            qc.cx(qubit, (qubit + 1) % num_qubits)
    qc.measure_all()
    return qc

def extract_features_from_circuit(qc):
    num_qubits = qc.num_qubits
    depth = qc.depth()
    width = qc.width()
    size = qc.size()
    ops = qc.count_ops()
    return [num_qubits, depth, width, size, ops.get('cx', 0), ops.get('h', 0)]
