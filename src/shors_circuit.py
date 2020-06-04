"""
https://qiskit.org/documentation/search.html?q=shor&check_keywords=yes&area=default
https://qiskit.org/documentation/stubs/qiskit.aqua.algorithms.Shor.html?highlight=shor#qiskit.aqua.algorithms.Shor
https://arxiv.org/abs/quant-ph/0205095
"""

from qiskit.aqua.algorithms import Shor

shor = Shor(15)
circuit = shor.construct_circuit()
