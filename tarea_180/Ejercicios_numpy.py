# 1. Crea un vector entre 7 y 66.
import numpy as np

vector = np.arange(7,67)
print(vector)

# 2. Invierte el vector generado anteriormente.
vector_invertido = vector[::-1]
print(vector_invertido)

# 3. Matriz de 4x4 con valores entre 0 y 15.
matriz4x4 = np.arange(16).reshape(4,4)
print(matriz4x4)

# 5. Crea la matriz identidad de 5x5.
matriz_indentidad = np.eye(5)
print(matriz_indentidad)

# 6. Crea una matriz de 5x5 donde la posición central y todas las posiciones que conforman el marco valgan 1 y el resto 0.
matriz_6 = np.zeros((5, 5))

# Asignar 1s al marco
matriz_6[0, :] = matriz_6[-1, :] = matriz_6[:, 0] = matriz_6[:, -1] = 1

# Asignar 1 al centro
matriz_6[2, 2] = 1
print(matriz_6)

# 7. Matriz de 4x4 donde cada fila valga entre 3 y 0. Valores in crescendo.
# Crear la matriz con valores en crescendo
valores = np.array([0, 1, 2, 3])

# Repetir la fila para crear una matriz 4x4
matriz_7 = np.tile(valores, (4, 1))

print(matriz_7)

# 8. Crea un array de ceros de 2x7.
matriz_8 = np.zeros((2, 7))
print(matriz_8)

# 9. Crea un array de ceros de 5x4 excepto toda la primera fila que valga 1.
matriz_9 = np.zeros((5, 4))
matriz_9[0, :] = 1
print(matriz_9)

# 10. Crea un array que represente una tabla de ajedrez. Negras 1 y blancas 0.
# Crear una matriz de 8x8 llena de 0s
ajedrez = np.zeros((8, 8), dtype=int)

# Asignar 1s a las casillas alternas
ajedrez[1::2, ::2] = ajedrez[::2, 1::2] = 1

print(ajedrez)
