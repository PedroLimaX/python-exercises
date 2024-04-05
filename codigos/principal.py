from ID3_C import ID3_C
import numpy as np

datos = np.genfromtxt('futbol.csv', delimiter=",", dtype="str")

X     = datos[:, :-1]
Y     = datos[:, -1]

arbol = ID3_C()

arbol.entrenar(X, Y)

salida = arbol.predecir(X)
print('Porcentaje de aciertos: ', 100 * sum(Y == salida)/X.shape[0])
