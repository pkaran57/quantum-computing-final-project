"""
https://qiskit.org/documentation/search.html?q=shor&check_keywords=yes&area=default
https://qiskit.org/documentation/stubs/qiskit.aqua.algorithms.Shor.html?highlight=shor#qiskit.aqua.algorithms.Shor
https://arxiv.org/abs/quant-ph/0205095
https://quantum-computing.ibm.com/jupyter/tutorial/fundamentals/4_quantum_circuit_properties.ipynb
"""
import logging

from qiskit.aqua.algorithms import Shor

logging.basicConfig(format="'%(asctime)s' %(name)s %(message)s'", level=logging.INFO)
logger = logging.getLogger()

Ns = 15, 21

for N in Ns:
    shor = Shor(N)

    qc = shor.construct_circuit()

    num_qubits = qc.num_qubits()

    # get the number and type of the gates in circuit
    num_ops = qc.count_ops()

    # get just the raw count of operations by computing the circuits size
    size = qc.size()

    '''The depth of a quantum circuit is a measure of how many "layers" of quantum gates, executed in parallel, 
    it takes to complete the computation defined by the circuit. Because quantum gates take time to implement, 
    the depth of a circuit roughly corresponds to the amount of time it takes the quantum computer to execute the 
    circuit. Thus, the depth of a circuit is one important quantity used to measure if a quantum circuit can be run on a 
    device. '''
    dept = qc.depth()

    logger.info('Shor circuit for factoring {} requires a circuit with {} qubits, {} ops, {} size, {} dept'.format(N,
                                                                                                                   num_qubits,
                                                                                                                   num_ops,
                                                                                                                   size,
                                                                                                                   dept))