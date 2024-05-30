import streamlit as st
from quantum_computing import initialize_ibmq, create_quantum_circuit
from local_ai import initialize_local_model, predict_with_local_model
import numpy as np

# Initialize IBM Quantum
provider = initialize_ibmq()

# Initialize local AI model
model = initialize_local_model()

# Create a quantum circuit and make predictions
qc = create_quantum_circuit()

# Assuming `qc` is a numpy array or can be converted to one
qc_data = np.array([qc])  # Modify as needed to match your model's expected input

prediction = predict_with_local_model(model, qc_data)
st.write("Quantum circuit prediction:", prediction)
