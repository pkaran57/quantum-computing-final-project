import logging

from qiskit.aqua import QuantumInstance
from qiskit.aqua.algorithms import Shor
from src.utils.DeviceUtils import DeviceUtils

logging.basicConfig(format="'%(asctime)s' %(name)s %(message)s'", level=logging.INFO)
logger = logging.getLogger('main')

device = DeviceUtils.get_device(use_local_simulator=False, min_num_qubits=10)
prime_number = 15

shor = Shor(prime_number)
quantum_instance = QuantumInstance(device, skip_qobj_validation=False)

result = shor.run(quantum_instance)

print("The list of factors of {} as computed by Shor is {}.".format(prime_number, result['factors'][0]))
