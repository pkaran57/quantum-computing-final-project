import os

import qiskit
from qiskit import (
    QuantumCircuit,
    execute,
    Aer)
from qiskit.providers.ibmq.job import IBMQJobApiError
from qiskit.providers.jobstatus import JOB_FINAL_STATES

from definitions import OUTPUT_DIR

print(qiskit.__qiskit_version__)

# Use Aer's qasm_simulator
simulator = Aer.get_backend('qasm_simulator')

# Create a Quantum Circuit acting on the q register
circuit = QuantumCircuit(2, 2)

# Add a H gate on qubit 0
circuit.h(0)

# Add a CX (CNOT) gate on control qubit 0 and target qubit 1
circuit.cx(0, 1)

# Map the quantum measurement to the classical bits
circuit.measure([0,1], [0,1])

# Execute the circuit on the qasm simulator
job = execute(circuit, simulator, shots=1000)

try:
    job_status = job.status()  # Query the backend server for job status.
    if job_status not in JOB_FINAL_STATES:
        print("The job is still running")
except IBMQJobApiError as ex:
    print("Something wrong happened!: {}".format(ex))

# Grab results from the job
result = job.result()

# Returns counts
counts = result.get_counts(circuit)
print("\nTotal count for 00 and 11 are:",counts)

# Draw the circuit
print(circuit.draw(output='text',
                   filename=(os.path.join(OUTPUT_DIR, 'circuit-diag.png'))))
