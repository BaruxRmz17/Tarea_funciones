import sympy as sp
import numpy as np
import matplotlib as plt

#Definimos las variables simbolicas 
x,y = sp.symbols('x,y')

#Definir la funcion original
f = x**2 + 2*x + 1

#Calculamos la inversa de la funcion 
f_inv = sp.solve(f - y,x)

#Mostrar la funcion original y su inveraa
print(f"Funcion original: f(x) = {f}")
print(f"Funcion inversa: f_inv(y) = {f_inv}")

#Para graficar, convertimos las funciones en expresiones numericas
f_lambdified = sp.lambdify(x,f, 'numpy')
f_inv_lambdified = sp.lambdify(y, f_inv[0], 'numpy')

#Rango de valores a graficar.
x_vals = np.linspace(-10,10,20)
y_vals = f_lambdified(x_vals)
y_inv_vals = f_inv_lambdified(x_vals)