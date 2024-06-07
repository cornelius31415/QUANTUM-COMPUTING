#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 19:12:22 2024

@author: cornelius
"""

# -----------------------------------------------------------------------------
#                           ENTANGLEMENT
# -----------------------------------------------------------------------------

"""
                How to entangle 2 qubits q0 and q1
                
                1. Apply Hadamard Gate to q0
                2. Apply CNOT Gate to q1 with q0 as a control qubit

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
#                           QUANTUM PART
# -----------------------------------------------------------------------------

# Quantum Circuit with 2 qubits and 2 classical bits
# Qubits are by default set to state /0>
qc = QuantumCircuit(2,2)

# Entangling the two qubits
qc.h(0)
qc.cx(0,1)

qc.measure(0,0)
qc.measure(1,1)


# -----------------------------------------------------------------------------
#                           VISUALIZATION
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















