from qiskit import QuantumCircuit
from qiskit import transpile
from qiskit_aer import Aer


from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

def grover_oracle():
    """Oracle marquant l'état cible |11>"""
    oracle = QuantumCircuit(2)
    oracle.cz(0, 1)  # Applique une porte CZ pour marquer |11>
    return oracle

def grover_diffuser():
    """Diffusion de Grover : amplification des probabilités"""
    diffuser = QuantumCircuit(2)
    diffuser.h([0, 1])
    diffuser.x([0, 1])
    diffuser.cz(0, 1)
    diffuser.x([0, 1])
    diffuser.h([0, 1])
    return diffuser

def grover_algorithm():
    """Exécution complète de Grover sur 2 qubits (N=4)"""
    qc = QuantumCircuit(2, 2)
    
    # Initialisation en superposition
    qc.h([0, 1])
    
    # Application de l'oracle
    qc.append(grover_oracle().to_gate(), [0, 1])
    
    # Diffusion de Grover
    qc.append(grover_diffuser().to_gate(), [0, 1])
    
    # Mesure
    qc.measure([0, 1], [0, 1])
    
    return qc

# Exécuter la simulation
backend = Aer.get_backend("qasm_simulator")
circuit = grover_algorithm()
new_circuit = transpile(circuit, backend)
job = backend.run(new_circuit)

# Afficher les résultats
result = job.result()
counts = result.get_counts()
print(f"Résultat : {result}")
print(f"Valeur : {counts}")

# Afficher en histogram
plot_histogram(counts)
plt.show()
