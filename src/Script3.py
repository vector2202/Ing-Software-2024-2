import matplotlib.pyplot as plt
import numpy as np

# Define la función que deseas graficar
def mi_funcion(x):
    return x ** 2

# Genera valores x desde -10 hasta 10
x = np.linspace(-10, 10, 100)

# Calcula los valores y aplicando la función a los valores x
y = mi_funcion(x)

# Grafica la función
plt.plot(x, y)
plt.title('Gráfico de mi función')
plt.xlabel('Eje x')
plt.ylabel('Eje y')
plt.grid(True)
plt.show()
