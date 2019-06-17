# Tutorial 2 - Generación de números realmente aleatorios en un computador cuántico
# Asier Arranz (www.youtube.com/asierarranz)
 
  
from qiskit import *

IBMQ.save_account('8e79592723ee023d8b81cad5036817920ce8a8d24715c9fe3088d977f7843e69081dea1e72b959e40605a6940ca1cd68b5e0500292a123209b3e91547cb6c708')
IBMQ.load_accounts()

q = QuantumRegister(5)
c = ClassicalRegister(5)
qcircuit = QuantumCircuit(q, c)

qcircuit.h(q[0])
qcircuit.h(q[1])
qcircuit.h(q[2])
qcircuit.h(q[3])
qcircuit.h(q[4])

qcircuit.measure(q,c)

print(qcircuit)
print("Ahora paciencia! Espera unos segundos hasta recibir el resultado desde el chip cuántico real...")
#backend=BasicAer.get_backend('qasm_simulator')
backend=IBMQ.get_backend('ibmqx4')

shot = execute(qcircuit, backend, shots=1)
counts=shot.result().get_counts()
print(counts)
decimal=int(list(counts)[0],2)

print ("Tu número aleatorio del 0 al 31 es el: " + str(decimal))