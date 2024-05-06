import random
import time
rangoancho = range(80)
rangoalto = range(20)
i = 0
fondo = (" ", " ", ".", " ", " ", "*"," ", " ", "´", " "," ")
respuesta = input("¿Desea generar un fondo? responda con si o no: ")
if respuesta == "si":
 for i in rangoalto:
    espacio=""
    for i in rangoancho:
        espacio=espacio+random.choice(fondo)
    print(espacio)
elif respuesta == "no":
    print("Saliendo del programa...")
    time.sleep(2)
else:
    print("Por favor, ingrese una respuesta valida")
    time.sleep(2)
#Matias Vargas Barrientos