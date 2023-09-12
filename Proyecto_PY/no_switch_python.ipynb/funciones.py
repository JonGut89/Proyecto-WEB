"""Este modulo implementa funciones de uso general
- es_entero(str_numero)
- es_flotante(str_numero)
- es_entero_entre(str_numero)
- es_flotante_entre(str_numero)"""

from os import system

def titulo(texto:str)->str:
        return f"{'-'*80}\n{texto.title().center(80)}\n{'-'*80}\n"

def menu(str_opciones:str)->int:
        lista_opciones = str_opciones.replace('\n','').split(';')
        system('cls')
        for index, opcion in enumerate(lista_opciones):
                if index == 0: #titulo
                        print(titulo(opcion))
                else:
                        print(f"({index}) - {opcion}")
        print(f"({index+1}) - Terminar")
        return leer_entero_entre("ingrese una opcion: ", 1, index+1)

def es_entero(str_numero):
        try: #intento
                int(str_numero)
        except: #Si hay error
                return False
        else: #Si no hay error
                return True

def es_flotante(str_numero):
        try: #Intento
                float(str_numero)
        except: #si hay error
                return False
        else: #Si no hay error
                return True
def es_numero(cartel_para_el_usuario):
        todo_ok=False
        while not todo_ok: # Mientras error
                cadena = input(cartel_para_el_usuario)
                if es_entero(cadena):
                        todo_ok = True
                else:
                        print("Error: Tiene que ingresar un numero entero.")
        numero = int(cadena)
        return numero

def leer_numero(cartel_para_el_usuario):
        while True:
                cadena = input(cartel_para_el_usuario)
                if es_entero(cadena):
                        return int(cadena)
                elif es_flotante(cadena):
                        return float(cadena)
                else:
                        print("Error: tiene que ingresar un nunmero.")

def leer_flotante(cartel_para_el_usuario):
        todo_ok = False
        while not todo_ok: #mientras error
                cadena = input(cartel_para_el_usuario)
                if es_flotante(cadena):
                        todo_ok = True
                else: 
                        print("Error: tiene que ingresar un numero float.")
        numero = float(cadena)
        return (numero)

def leer_entero_entre(cartel_para_el_usuario, desde, hasta):
        todo_ok = False
        while not todo_ok: #mientras error
                cadena = input(cartel_para_el_usuario)
                if es_entero(cadena):
                        numero = int(cadena)
                        if desde <= numero <= hasta: #if numero >= desde and numero <= hasta
                                todo_ok = True
                        else:
                                print(f"Error: el numero no esta en el rango: [{desde}..{[hasta]}].")
                else:
                        print("Error: Tiene que ingresar un numero entero.")
        return(numero)

def leer_flotante_entre(cartel_para_el_usuario, desde, hasta):
        todo_ok = False
        while not todo_ok: # mientras error
                cadena = input(cartel_para_el_usuario)
                if es_flotante(cadena):
                        numero = float(cadena)
                        if desde <= numero <= hasta: #if numero >= desde and numero <= hasta
                                todo_ok = True
                        else:
                                print(f"Erorr: el numero no esta en el rango: [{desde}..{hasta}].")
                else:
                        print("Error: Tiene que ingresar un numero float.")
        return(numero)

def test_funciones():
        print(f"El nombre es: {__name__}")
        cantidad_patas_perro = leer_entero_entre("Ingrese la cantidad de patas que tiene su perro: ", 1, 4)
        dia = leer_entero_entre("Dia: ", 1, 31)
        mes = leer_entero_entre("Mes: ", 1, 12)
        print(leer_flotante_entre("Importe: ", 1, 999999.99))

if __name__ == '__main__':
        test_funciones()