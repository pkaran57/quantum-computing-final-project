import logging
from qiskit import Aer

from qiskit.aqua import QuantumInstance
from qiskit.aqua.algorithms import Shor

logging.basicConfig(format="'%(asctime)s' %(name)s %(message)s'", level=logging.INFO)
logger = logging.getLogger('main')

# provider = IBMQ.load_account()
# device = provider.get_backend('ibmq_qasm_simulator')
device = Aer.get_backend('qasm_simulator')

prime_number = 65

shor = Shor(prime_number)
quantum_instance = QuantumInstance(device)

result = shor.run(quantum_instance)

print("The list of factors of {} as computed by Shor is {}.".format(prime_number, result['factors'][0]))
