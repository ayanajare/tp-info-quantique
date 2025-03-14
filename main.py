from qiskit import QuantumCircuit
from qiskit.quantum_info import SparsePauliOp
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager
from qiskit_ibm_runtime import EstimatorV2 as Estimator
from qiskit_ibm_runtime import QiskitRuntimeService
from dotenv import load_dotenv
import os


 
qc = QuantumCircuit(2)
 
qc.h(0)
 
qc.cx(0, 1)
 
qc.draw("mpl")
load_dotenv()

QiskitRuntimeService.save_account(
  token=os.getenv("API_KEY"),
  channel="ibm_quantum",
  overwrite=True
)
 
observables_labels = ["IZ", "IX", "ZI", "XI", "ZZ", "XX"]
observables = [SparsePauliOp(label) for label in observables_labels]


service = QiskitRuntimeService()
 
backend = service.least_busy(simulator=False, operational=True)
 
pm = generate_preset_pass_manager(backend=backend, optimization_level=1)
isa_circuit = pm.run(qc)
 
isa_circuit.draw("mpl", idle_wires=False)
 
estimator = Estimator(mode=backend)
estimator.options.resilience_level = 1
estimator.options.default_shots = 5000
 
mapped_observables = [
    observable.apply_layout(isa_circuit.layout) for observable in observables
]
 
job = estimator.run([(isa_circuit, mapped_observables)])
 
print(f">>> Job ID: {job.job_id()}")