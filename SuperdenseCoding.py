#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 17:14:36 2024

@author: cornelius
"""

# -----------------------------------------------------------------------------
#                               SUPERDENSE CODING
# -----------------------------------------------------------------------------



"""
                            SUPERDENSE CODING
             
            - Encode the information of 2 classical bits in 1 qubit
            - Qubit is then transported via a quantum channel
            
                                STEPS
                   1. Entangle q0 and q1
                      Alice gets q0 and Bob gets q1 
                      apply Hadamard gate to q0
                      apply CNOT gate to q1 with q0 as a control qubit
                      
                   2. If 1st bit is 1 apply phase flip to q0
                      If 1st bit is 0 q0 remains unchanged
                      
                   3. If 2nd bit is 1 apply NOT gate to q0
                      If 2nd bit is 0 q0 remains unchanged
                   
                   4. Send q0 via Quantum Channel to Bob
                   
                   5. Bob applies CNOT to q1 with q0 as a control qubit
                   
                   6. Bob applies Hadamard to q0
                   
                   7. Bob measures q0 and q1
                      
"""

"""

                    https://pypi.org/project/qiskit/#history
                    
                    qiskit                            0.46.0
                    qiskit-aer                        0.14.2
                    qiskit-ibm-runtime                0.23.0
                    qiskit-terra                      0.46.0

"""


import warnings
from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import circuit_drawer
from qiskit.visualization import plot_histogram

# -----------------------------------------------------------------------------
#                               WARNINGS
# -----------------------------------------------------------------------------

#                       Suppress or reset warnings

warnings.filterwarnings("ignore")
#warnings.resetwarnings()

# -----------------------------------------------------------------------------
#                             QUANTUM PART
# -----------------------------------------------------------------------------

# Bits we want to send

bit1 = 1
bit2 = 0

# Create a Quantum Circuit with 2 qubits and 2 classical bits
qc = QuantumCircuit(2,2)

# Entangle the 2 qubits
qc.h(0)
qc.cx(0,1)

qc.barrier()


# Depending on the value of the bits gates are applied to q0
if bit1 == 1:
    qc.z(0)
    
if bit2 == 1:
    qc.x(0)
    
qc.barrier()

# Send q0 to Bob

qc.cx(0,1)
qc.h(0)
qc.measure(0,1)    # weird internal structure in the classical register
qc.measure(1,0)    # intuitively i would measure q0 and store it in c0 but
                   # that somehow flips the order of the bits  


# -----------------------------------------------------------------------------
#                             VISUALIZATION
# -----------------------------------------------------------------------------

qc.draw('mpl')
print(qc)

# -----------------------------------------------------------------------------
#                        EXECUTION ON SIMULATOR
# -----------------------------------------------------------------------------


# Parameters for execution on simulator
backend = Aer.get_backend('qasm_simulator')
shots = 1024  # the number of shots in the experiment

# Run the algorithm
result = execute(qc, backend=backend, shots=shots).result()

# Shows the results obtained from the quantum algorithm
counts = result.get_counts()
plot_histogram(counts)

print('\nThe measured outcomes of the circuits are:', counts)
