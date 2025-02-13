# Importamos las librerías necesarias
import numpy as np  # Para manejar arreglos numéricos y operaciones matemáticas
import matplotlib.pyplot as plt  # Para graficar funciones matemáticas

# Definimos la función f(x), que representa una ecuación cuadrática
def f(x):
    return x**2 - 4*x + 3  # Calculamos el valor de la función para un valor dado de x

# Generamos un conjunto de valores para x en el rango de -2 a 2
# np.linspace(-2, 2, 100) genera 100 valores equidistantes entre -2 y 2
x = np.linspace(-2, 2, 100)

# Calculamos los valores de f(x) evaluando la función en cada valor de x
y = f(x)

# Imprimimos los valores de x y f(x) para ver los resultados numéricos
print("Valores de x y f(x): ")
for i in range(len(x)):  # Iteramos sobre cada valor de x
    print(f"x = {x[i]:.2f}, f(x) = {y[i]:.2f}")  # Imprimimos x con 2 decimales y su correspondiente f(x)

# Graficamos la función
plt.plot(x, y, label="f(x) = x**2 - 4*x + 3")  # Dibujamos la curva y añadimos una etiqueta

# Configuramos la gráfica
plt.title("Gráfica de f(x) = x**2 - 4*x + 3")  # Título de la gráfica
plt.xlabel("x")  # Etiqueta del eje X
plt.ylabel("f(x)")  # Etiqueta del eje Y

# Añadimos líneas en los ejes X y Y para referencia
plt.axhline(0, color='black', linewidth=1)  # Línea horizontal en y=0
plt.axvline(0, color='black', linewidth=1)  # Línea vertical en x=0

# Mostramos la cuadrícula para facilitar la lectura de valores
plt.grid(True)

# Mostramos la leyenda de la función
plt.legend()

# Finalmente, mostramos la gráfica
plt.show()