import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange


# Creamos el vector del ejemplo de clase
x = np.linspace(0, 2*np.pi, 17)

y = []
for i in x:
    y.append(np.sin(i))

y = np.array(y)


# Polinomio interpolante de Lagrange
Polinomio_Lagrange = lagrange(x, y)
print("Grado del polinomio de Lagrange:", Polinomio_Lagrange.order)


# Máximo usando el punto máximo y sus vecinos
indice_max = np.argmax(y)

x_parabola = x[indice_max-1:indice_max+2]
y_parabola = y[indice_max-1:indice_max+2]

Parabola = lagrange(x_parabola, y_parabola)

x_fino_parabola = np.linspace(x_parabola[0], x_parabola[-1], 1000)
y_fino_parabola = Parabola(x_fino_parabola)

indice_parabola = np.argmax(y_fino_parabola)

x_max_parabola = x_fino_parabola[indice_parabola]
y_max_parabola = y_fino_parabola[indice_parabola]



# 4. Derivada extrapolada del polinomio interpolante
h = 0.01

def F(x):
    return Polinomio_Lagrange(x)

def F_derivada_extrapolada(x, h):
    cd_half = (F(x + h/4) - F(x - h/4)) / (h/2)
    cd_full = (F(x + h/2) - F(x - h/2)) / h
    return (4*cd_half - cd_full) / 3


# 5. Método de punto fijo usando la derivada
def punto_fijo(x_inicial, iteraciones):
    x_actual = x_inicial

    for i in range(iteraciones):
        x_actual = x_actual + F_derivada_extrapolada(x_actual, h)

    return x_actual

x_max_punto_fijo = punto_fijo(0, 1000)
y_max_punto_fijo = F(x_max_punto_fijo)



# 6. Resultados
print("Resultado usando solo 3 puntos y el vector generador:")
print("x =", x_max_parabola)
print("y =", y_max_parabola)

print("\nResultado usando punto fijo con la derivada:")
print("x =", x_max_punto_fijo)
print("y =", y_max_punto_fijo)

print("\nDiferencia entre ambos resultados:")
print("Diferencia en x =", abs(x_max_parabola - x_max_punto_fijo))
print("Diferencia en y =", abs(y_max_parabola - y_max_punto_fijo))


# 7. Gráfica
x_fino = np.linspace(0, 2*np.pi, 1000)
y_fino = F(x_fino)

plt.plot(x_fino, y_fino, 'b', label='Polinomio de Lagrange')
plt.plot(x_fino_parabola, y_fino_parabola, 'r--', label='Parábola con tres puntos')

plt.scatter(x, y, color='black', label='Puntos originales')
plt.scatter(x_max_parabola, y_max_parabola, color='red', marker='x', label='Máximo parábola')
plt.scatter(x_max_punto_fijo, y_max_punto_fijo, color='blue', marker='o', label='Máximo punto fijo')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Comparación del máximo por parábola y punto fijo')
plt.legend()
plt.grid()
plt.show()