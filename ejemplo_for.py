"""
Leer 10 nunmeros y mostrar la suma.


print(range(10))
print(len(range(10)))
print(list(range(10)))
"""
suma = 0
for n in range(10):
        #         print(n,end=' ')
        numero = int(input(f"Ingrese el numero {n+1} de 10: "))

        suma += numero
print('suma: ', suma)