""""
ingresar dos numeros enteros, donde a es <= b
mostrar: suma de los pares entre a y b
el producto de los numeros impares entre a y b

1-Ingrese un numero: 9
2-Ingrese un numero: 13
9,10,11,12,13,
Suma de pares: 22
Producto de impares: 1287

"""

a = int(input("1-Ingrese un numero: "))
b = int(input("2-Ingrese un numero: "))

while a > b: #Error
        print(f"Error: {a} tiene que ser menor <= {b}")
        b = int(input("2-Ingrese un numero: "))
        #si los datos son validos continua el programa

suma = 0
producto = 1

for numero in range(a,b+1):
        print(numero,end=',')
        if numero %2 == 0:
                suma += numero
                
        else: 
                producto *= numero

print()                
print(f"Suma de pares: {suma}")
print(f"Producto de impares: {producto}")


"""
while a%2 == 0 and b%2 == 0 and a <= b:
        suma = a + b
        print(f"Suma: ", suma)
        break

while a%2 !=0 and b%2 !=0 and a <= b:
        producto = a * b
        print(f"La multiplicación es: ", producto)
        break
"""