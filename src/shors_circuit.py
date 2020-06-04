import logging
import os

from qiskit.aqua.algorithms import Shor

from definitions import OUTPUT_DIR

logging.basicConfig(format="%(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

Ns = 15, 21, 33, 35

for N in Ns:
    logging.info("\nShor's circuit configuration for factoring {}:".format(N))
    shor = Shor(N)

    qc = shor.construct_circuit()
    qc.draw(output='latex_source', filename=(os.path.join(OUTPUT_DIR, 'shors-diag-for-{}.tex'.format(N))))

    num_qubits = qc.num_qubits
    num_classical_bits = qc.num_clbits

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

    logger.debug(
        "Shor's circuit for factoring {} requires:\n {} qubits,\n {} classical bits,\n {} ops,\n {} size,\n {} dept".format(
            N,
            num_qubits,
            num_classical_bits,
            num_ops,
            size,
            dept))
