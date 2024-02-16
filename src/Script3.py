import matplotlib.pyplot as plt
import numpy as np

def function(x):
    return x ** 3

x = np.linspace(0, 20, 100)

def main():
    y = function(x)
    plt.plot(x, y)
    plt.title('Ejemplo Matplot')
    plt.xlabel('Eje x')
    plt.ylabel('Eje y')
    plt.grid(True)
    plt.show()
main()
