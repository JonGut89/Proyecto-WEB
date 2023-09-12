"""Leer un grupo de datos enteros, terminado con 0 (marca de fin de datos).
Mostrar la suma.

g1 = 13648759788,0
g2 = 1,2,54,0
gi = 0
"""

#ANTES (para todos los datos)
numero = int(input("Numero: "))
suma = 0
while numero != 0:
        #DURANTE (para cada dato)
        suma += numero # suma = suma + numero
        numero =int(input("Numero: "))

#DESPUES (totales)

print(f"Suma: {suma}")