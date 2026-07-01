import numpy as np
import matplotlib.pyplot as plt

# 1. Funcion Analitica
# Cambia esta función si quieres usar otra

def f(x):
    return np.sin(x)*np.exp(-0.2*x)


# 2. Derivada de la Funcion Escogida (cualquier función f(x))

def derivada(f, x, h=1e-5):
    return (f(x + h) - f(x - h)) / (2*h)


# 3. Aplicamos el metodo de bisección f'(x)=0

def biseccion_derivada(f, a, b, tolerancia=1e-8, max_iter=100):

    fa = derivada(f, a)
    fb = derivada(f, b)

    if fa * fb > 0:

        print("No se puede aplicar bisección en este intervalo.")
        print("La derivada no cambia de signo entre a y b.")

    else:

        for i in range(max_iter):

            m = (a + b) / 2
            fm = derivada(f, m)

            if abs(fm) < tolerancia:
                return m

            if fa * fm < 0:
                b = m
                fb = fm
            else:
                a = m
                fa = fm

        return (a + b) / 2


# 4. Definimos el intervalo de búsqueda

a = 0
b = 15

x_max = biseccion_derivada(f, a, b)

y_max = f(x_max)

print("Máximo encontrado:")
print("x =", x_max)
print("f(x) =", y_max)


# 5. Gráfica

x = np.linspace(a, b, 500)
y = f(x)

plt.plot(x, y, label="f(x)")
plt.scatter(x_max, y_max, color="red", label="Máximo")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Máximo de una función analítica usando bisección")
plt.legend()
plt.grid()
plt.show()