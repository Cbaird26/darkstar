import streamlit as st
from quantum_computing import initialize_ibmq, create_quantum_circuit
from google_ai import initialize_google_ai, predict_with_model

# Initialize IBM Quantum and Google AI
provider = initialize_ibmq()
model = initialize_google_ai()

# Create a quantum circuit and make predictions
qc = create_quantum_circuit()
result = predict_with_model(model, qc)

st.write("Quantum Circuit:", qc.draw())
st.write("Prediction Result:", result)
