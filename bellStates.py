# Tutorial 1 - Ejecución del Bell State en el simulador
# Asier Arranz (www.youtube.com/asierarranz)
 
  
from qiskit import *


# Creamos los Qubits
q = QuantumRegister(2)
# Creamos los bits clásicos
c = ClassicalRegister(2)
qcircuit = QuantumCircuit(q, c)

# Añadimos una puerta dfe Hadamard en el primero
qcircuit.h(q[0])
# Y una CNOT entre el primer y segundo Qubit
qcircuit.cx(q[0], q[1])
# Medismos los Qubits
qcircuit.measure(q, c)

# Visualizamos el circuito
print (qcircuit)

# Para simularlo, vamos a utilizzar el QASM simulator
simulator = BasicAer.get_backend('qasm_simulator')

# Ejecutamos la simulación
job = execute(qcircuit, simulator)
result = job.result()

# Mostramos el conteo final de los resultados
counts = result.get_counts(qcircuit)
print (counts)