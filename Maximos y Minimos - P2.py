import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange

arreglo = [10, 95, 110, 90, 40]

x = np.arange(len(arreglo))
y = np.array(arreglo)

polinomio = lagrange(x, y)
print("Grado del polinomio:", polinomio.order)

pos_max = np.argmax(y)

x_vecino = x[pos_max-1:pos_max+2]
y_vecino = y[pos_max-1:pos_max+2]

parabola = lagrange(x_vecino, y_vecino)

x_parabola = np.linspace(x_vecino[0], x_vecino[-1], 1000)
y_parabola = parabola(x_parabola)

pos_parabola = np.argmax(y_parabola)

x_max_parabola = x_parabola[pos_parabola]
y_max_parabola = y_parabola[pos_parabola]

x_grafica = np.linspace(x[0], x[-1], 1000)
y_grafica = polinomio(x_grafica)

pos_polinomio = np.argmax(y_grafica)

x_max_polinomio = x_grafica[pos_polinomio]
y_max_polinomio = y_grafica[pos_polinomio]

print("Resultado usando el polinomio de Lagrange:")
print("x =", x_max_polinomio)
print("y =", y_max_polinomio)

print("\nResultado usando parábola con tres puntos:")
print("x =", x_max_parabola)
print("y =", y_max_parabola)

print("\nDiferencia entre ambos métodos:")
print("Diferencia en x =", abs(x_max_polinomio - x_max_parabola))
print("Diferencia en y =", abs(y_max_polinomio - y_max_parabola))

plt.plot(x_grafica, y_grafica, 'b', label='Polinomio de Lagrange')
plt.plot(x_parabola, y_parabola, 'r--', label='Parábola con tres puntos')

plt.scatter(x, y, color='black', label='Puntos originales')
plt.scatter(x_max_polinomio, y_max_polinomio, color='blue', marker='o', label='Máximo polinomio')
plt.scatter(x_max_parabola, y_max_parabola, color='red', marker='x', label='Máximo parábola')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Comparación del máximo del polinomio y la parábola')
plt.legend()
plt.grid()
plt.show()