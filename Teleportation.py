#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 08:57:54 2024

@author: cornelius
"""

"""
                https://pypi.org/project/qiskit/#history
                
                qiskit                            0.46.0
                qiskit-aer                        0.14.2
                qiskit-ibm-runtime                0.23.0
                qiskit-terra                      0.46.0




                        TELEPORTATION PROTOCOL
                        
                We start with 3 qubits q0, q1, q2
                Aice wants to teleport q0 to Bob
                
                1. Alice and Bob entangle q1 and q2
                2. Alice takes q0 and q1, Bob takes q2
                3. Alice applies CNOT to q1 with q0 as a control qubit
                4. Alice applies Hadamard to q0
                5. Alice measures both q0 and q1 and sends 
                   2 classical bits to Bob
                6. Bob applies CNOT to his qubit q2 with q1 as a control qubit
                7. Bob applies C-phase-flip to q2 with q0 as control qubit
"""




import warnings
from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import circuit_drawer
from qiskit.visualization import plot_histogram

# ---------------           WARNINGS             --------------------
# Suppress or reset warnings
warnings.filterwarnings("ignore")
#warnings.resetwarnings()
# -------------------------------------------------------------------

qc = QuantumCircuit(3,3)

# Set q0 (Qubit to teleport) to /
qc.x(0)                     
qc.barrier()


# Entangle q1 and q2
qc.h(1)
qc.cx(1,2)
qc.barrier()

# Prepare q0 to teleport
qc.cx(0,1)
qc.h(0)
qc.barrier()

# Measure both qubits and turn them into classical bits
qc.measure(0, 0)
qc.measure(1, 1)
qc.barrier()


# Measured q0 and q1 travel as classical bits to Bob

qc.cx(1,2)
qc.cz(0, 2)

# Bob measures his qubit q2. It should always result in the state of q0
# In the process of teleporting the original state of q0 has been distroyed
# It is now put onto Bob's qubit q2 which acts like a blank piece of paper
# to print the information onto (which was in q0 and then transported as 2 bits)
qc.measure(2, 2)



# -----------------------------------------------------------------------------
#                             VISUALIZATION
# -----------------------------------------------------------------------------

print(qc)
qc.draw('mpl')

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




























