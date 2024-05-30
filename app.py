import streamlit as st
from quantum_computing import initialize_ibmq, create_quantum_circuit, extract_features_from_circuit
from local_ai import initialize_local_model, predict_with_local_model
import numpy as np

# Replace with your actual IBM Quantum Experience API token
api_token = st.secrets["IBM_QUANTUM_API_TOKEN"]

# Initialize IBM Quantum
provider = initialize_ibmq(api_token)

# Initialize local AI model
model = initialize_local_model()

# Create a quantum circuit and extract features
qc = create_quantum_circuit()
qc_features = extract_features_from_circuit(qc)

# Convert features to numpy array
qc_data = np.array([qc_features])

# Make prediction
prediction = predict_with_local_model(model, qc_data)
st.write("Quantum circuit prediction:", prediction)
