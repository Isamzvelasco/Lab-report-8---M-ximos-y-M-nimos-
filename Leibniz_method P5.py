import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# 1. Cantidad de términos
N_max = 100000
n = range(N_max)

# 2. Serie de Leibniz
contador = 0
puntos = []

for i in n:
    if i % 2 == 0:
        termino = 1 / (2*i + 1)
    else:
        termino = -1 / (2*i + 1)

    contador = contador + termino
    puntos.append(4 * contador)

puntos = np.array(puntos)
N = np.array(list(n)) + 1

# 3. Posibles valores de pi infinito
PI_inf = np.linspace(3.0, 3.2, 2000)

R2_valores = []
pendientes = []

# 4. Zona usada para estudiar la convergencia
mask_zona = (N > 100) & (N < 8000)

N_pt = N[mask_zona]
puntos_pt = puntos[mask_zona]

# 5. Probamos cada posible pi infinito
for pi_inf in PI_inf:

    F = np.abs(pi_inf - puntos_pt)

    mask = F > 0

    logN = np.log(N_pt[mask])
    logF = np.log(F[mask])

    slope, intercept, r_value, p_value, std_err = stats.linregress(logN, logF)

    logF_ajuste = slope * logN + intercept

    # R^2 clásico
    promedio = np.mean(logF)
    ss_res = np.sum((logF - logF_ajuste)**2)
    ss_tot = np.sum((logF - promedio)**2)

    R2 = 1 - ss_res/ss_tot

    R2_valores.append(R2)
    pendientes.append(slope)

R2_valores = np.array(R2_valores)
pendientes = np.array(pendientes)

# 6. Valor de pi infinito con R^2 máximo
indice_max = np.argmax(R2_valores)

pi_infinito_estimado = PI_inf[indice_max]
R2_maximo = R2_valores[indice_max]
pendiente_mejor = pendientes[indice_max]

# 7. Error usando el mejor pi infinito
F_mejor = np.abs(pi_infinito_estimado - puntos)

# 8. Resultados
print("Último dato de Leibniz:", puntos[-1])
print("Pi infinito estimado:", pi_infinito_estimado)
print("Diferencia entre pi infinito estimado y el último dato:", F_mejor[-1])
print("Pendiente del ajuste:", pendiente_mejor)
print("R^2 máximo:", R2_maximo)

# 9. Gráfica pi(N) vs N
plt.figure()
plt.plot(N, puntos, '--', label=r'$\pi(N)$')
plt.axhline(np.pi, linestyle='--', color='r', label=r'$\pi$ real')
plt.xscale('log')
plt.xlabel('N')
plt.ylabel(r'$\pi(N)$')
plt.title(r'Aproximación de $\pi$ mediante la serie de Leibniz')
plt.legend()
plt.grid()
plt.show()

# 10. Error F(N)
plt.figure()
plt.plot(N, F_mejor, 'o', markersize=2)
plt.xscale('log')
plt.yscale('log')
plt.xlabel('N')
plt.ylabel(r'$F(N)=|\pi_{\infty}-\pi(N)|$')
plt.title(r'Error respecto a $\pi_{\infty}$ estimado')
plt.grid()
plt.show()

# 11. R^2 vs pi infinito
plt.figure()
plt.plot(PI_inf, R2_valores)
plt.xlabel(r'$\pi_{\infty}$')
plt.ylabel(r'$R^2$')
plt.title(r'Coeficiente de determinación para posibles valores de $\pi_{\infty}$')
plt.grid()
plt.show()

# 12. Ajuste log-log final usando solo la zona lineal
N_pt = N[mask_zona]
F_pt = F_mejor[mask_zona]

mask = F_pt > 0

logN = np.log(N_pt[mask])
logF = np.log(F_pt[mask])

slope, intercept, r_value, p_value, std_err = stats.linregress(logN, logF)
logF_fit = slope * logN + intercept

plt.figure()
plt.plot(logN, logF, 'o', markersize=2, label="Datos")
plt.plot(logN, logF_fit, '-', label="Ajuste lineal")
plt.xlabel(r'$\log(N)$')
plt.ylabel(r'$\log(F)$')
plt.title('Ajuste log-log para estudiar la convergencia')
plt.legend()
plt.grid()
plt.show()