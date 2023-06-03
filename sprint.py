#importando modulos 
import random
import string
import json

#binvenida
print("Bienvenido")
print(" ")

print("favor de ingresar los datos solicitados según paciente indicado")
print(" ")

#creación de usuarios en string "cadena"
usuarios = ["paciente1", "paciente2", "paciente3", "paciente4", "paciente5", "paciente6", "paciente7", "paciente8", "paciente9", "paciente10"]

#creacion de funcion para generar la clave 
def generar_clave():
    combinacion = string.ascii_letters + string.digits
    clave = ''.join(random.choice(combinacion) for _ in range(8))
    return clave
#combinacion entre string.ascii_letters (cadena de letras entre mayusculas y minusculas) + (cadena de digitos)
# uniendo al azar los anteriores en un rango de 8 caracteres ya sean numeros o letras  


#creacion de funcion para agregar el numero del celular
def agregar_celular(usuario):
    ingreso = 0
    while ingreso < len(usuarios):
        if usuarios[ingreso] == usuario:
            celular = input(f"Favor de ingresar el número de celular para el paciente {usuario}: ")
            if celular.isdigit() and len(celular) == 8:
                print(f"Número de celular asociado a paciente {usuario}.")
                return celular
            else:
                print("El número de celular debe tener 8 dígitos. Inténtelo de nuevo.")
                ingreso -= 1  # Retroceder el índice para repetir el ingreso para el mismo usuario
        ingreso += 1

#ingreso 0 es cuando al contar la lista de usuarios desde el ultimo hasta el primero los asigna 
#como -10 -9 asi sucesivamente hsata llegar al 0 cuando llega a 0 se detiene el bucle 
#dentro de el se solicita el ingreso del celular, luego asocia que si el caracter ingresado es digito (isdigit) 
# y ademas es igual a 8 digitos (len), si los dos son verdaderos lo asocia como numero de celular
# en caso de ser falso retrocede el indice para volver a solicitar el numero 
#se acaba cuando se ingresan todos los usuarios 


#creacion de cuentas
cuentas = {}

#clave, celular y usuario al diccionario asociado a usuario   
for usuario in usuarios:
    clave = generar_clave()
    celular = agregar_celular(usuario)
    if celular is not None:
        cuenta = {
            "contraseña": clave,
            "celular": celular
        }
        cuentas[usuario] = cuenta


print(" ")
print("se han asociado correctamente las claves internas y numeros personales de los pacientes")
print(" ")
print("reflejando usuario, contraseña y numero de celular de los usuarios")
print(" ")

#transformando a cadena
cadena_cuentas = json.dumps(cuentas)

#modificando para que se vea la Ñ
cuentas_cargadas = json.loads(cadena_cuentas)


#mostrando key y valores de lo asociado 
for usuario, datos in cuentas_cargadas.items():
    print("Usuario:", usuario)
    print("Contraseña:", datos["contraseña"])
    print("Celular:", datos["celular"])
    print(" ")

#imprimiendo listado como string
print(cuentas_cargadas)





