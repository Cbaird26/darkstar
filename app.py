# app.py
import streamlit as st
from quantum_computing import initialize_ibmq, create_quantum_circuit
from google_ai import initialize_google_ai, predict_with_model

# Initialize IBM Quantum and Google AI
project_id = "sigma-seer-405001"
location = "us-central1"  # Choose a valid region from the provided list
model_name = "your-model-name"  # Replace with your actual model name

provider = initialize_ibmq()
model = initialize_google_ai(project_id, location, model_name)

# Create a quantum circuit and make predictions
qc = create_quantum_circuit()

if model is not None:
    prediction = predict_with_model(model, qc)
    st.write("Quantum circuit prediction:", prediction)
else:
    st.error("Failed to initialize the Google AI model.")
