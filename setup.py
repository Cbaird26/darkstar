from setuptools import setup, find_packages

setup(
    name='quantum_supercomputer',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'qiskit==0.39.2',
        'qiskit-terra==0.22.2',
        'qiskit-ibmq-provider==0.19.2',
        'google-cloud-aiplatform==1.10.0',
        'streamlit==1.9.0'
    ],
    dependency_links=[
        'https://pypi.org/simple/qiskit-aer/'
    ],
)
