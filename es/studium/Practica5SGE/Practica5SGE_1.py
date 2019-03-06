# coding: utf-8
'''
Created on 19 feb. 2019

@author: Álvaro Muñoz
'''
import random

nombreFichero = input("Introduzca el nombre del fichero: ")
f = open(nombreFichero,"a") # Abrir fichero para leer

caracteristica1 = input("Introduzca la característica1: ")
rango1_1 = int(input("Introduzca el rango inferior de " + caracteristica1 + ":" + " " ))
rango1_2 = int(input("Introduzca el rango superior de " + caracteristica1 + ":" + " " ))
caracteristica2 = input("Introduzca la característica2: ")
rango2_1 = int(input("Introduzca el rango inferior de  " + caracteristica2 + ":" + " "))
rango2_2 = int(input("Introduzca el rango superior de  " + caracteristica2 + ":" + " "))
caracteristica3 = input("Introduzca la característica3: ")
rango3_1 = int(input("Introduzca el rango inferior de  " + caracteristica3 + ":" + " "))
rango3_2 = int(input("Introduzca el rango superior de  " + caracteristica3 + ":" + " "))
caracteristica4 = input("Introduzca la característica4: ")
rango4_1 = int(input("Introduzca el rango inferior de  " + caracteristica4 + ":" + " "))
rango4_2 = int(input("Introduzca el rango superior de  " + caracteristica4 + ":" + " "))
caracteristica5 = input("Introduzca la característica5: ")
rango5_1 = int(input("Introduzca el rango inferior de  " + caracteristica5 + ":" + " "))
rango5_2 = int(input("Introduzca el rango superior de  " + caracteristica5 + ":" + " "))

cadena= caracteristica1 + " "   + caracteristica2 + " " + caracteristica3 + " " + caracteristica4 + " " + caracteristica5 + "\n"

f.write(cadena) 
     
for i in range (1000):
   
    cadena1 = random.randrange(rango1_1, rango1_2)
    cadena2 = random.randrange(rango2_1, rango2_2)
    cadena3 = random.randrange(rango3_1, rango3_2)
    cadena4 = random.randrange(rango4_1, rango4_2)
    cadena5 = random.randrange(rango5_1, rango5_2)
    
    cadenaFinal= str(cadena1) + " "   + str(cadena2) + " "   + str(cadena3) + " "   + str(cadena4) + " "   + str(cadena5)+ "\n"
    f.write(str(cadenaFinal))
     
f.close() # Cerrar