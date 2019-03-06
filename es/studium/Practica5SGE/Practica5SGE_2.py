# coding: utf-8
'''
Created on 6 mar. 2019

@author: Rafael Molino
'''
import statistics

colum1=[]
colum2=[]
colum3=[]
colum4=[]
colum5=[]

nombreFichero = input("Introduzca el nombre del fichero: ")

try:
    f = open(nombreFichero,"r") # Abrir fichero para leer
except Exception:
    exit()
fin = False # Variable para controlar fin del bucle
line=str(f.readline())
while not fin: # Bucle para recorrer fichero  
        if not line: # Comprobar si hemos llegado a fin de fichero
            fin = True
        else:            
        
            line=str(f.readline())
            line = line.replace("\n", "")
            lineSplit=(line.split(' '))
            if '' not in lineSplit:
                colum1.append(lineSplit[0])
                colum2.append(lineSplit[1])
                colum3.append(lineSplit[2])
                colum4.append(lineSplit[3])
                colum5.append(lineSplit[4])        
        
print("Media Característica 1:")
print(statistics.mean(list(map(int,colum1))))
print("Media Característica 2:")
print(statistics.mean(list(map(int,colum2))))
print("Media Característica 3:")
print(statistics.mean(list(map(int,colum3))))
print("Media Característica 4:")
print(statistics.mean(list(map(int,colum4))))
print("Media Característica 5:")
print(statistics.mean(list(map(int,colum5))))
print("-----------------------")
print("-----------------------")
print("-----------------------")
print("Moda Característica 1:")
print(statistics.mode((colum1)))
print("Moda Característica 2:")
print(statistics.mode(colum2))
print("Moda Característica 3:")
print(statistics.mode(colum3))
print("Moda Característica 4:")
print(statistics.mode(colum4))
print("Moda Característica 5:")
print(statistics.mode(colum5))
print("-----------------------")
print("-----------------------")
print("-----------------------")
print("Máximo Característica 1:")
print(max(list(map(int,colum1))))
print("Máximo Característica 2:")
print(max(list(map(int,colum2))))
print("Máximo Característica 3:")
print(max(list(map(int,colum3))))
print("Máximo Característica 4:")
print(max(list(map(int,colum4))))
print("Máximo Característica 5:")
print(max(list(map(int,colum5))))
print("-----------------------")
print("-----------------------")
print("-----------------------")
print("Mínimo Característica 1:")
print(min(list(map(int,colum1))))
print("Mínimo Característica 2:")
print(min(list(map(int,colum2))))
print("Mínimo Característica 3:")
print(min(list(map(int,colum3))))
print("Mínimo Característica 4:")
print(min(list(map(int,colum4))))
print("Mínimo Característica 5:")
print(min(list(map(int,colum5))))
print("-----------------------")
print("-----------------------")
print("-----------------------")
print("Varianza Característica 1:")
print(statistics.variance(list(map(int,colum1))))
print("Varianza Característica 2:")
print(statistics.variance(list(map(int,colum2))))
print("Varianza Característica 3:")
print(statistics.variance(list(map(int,colum3))))
print("Varianza Característica 4:")
print(statistics.variance(list(map(int,colum4))))
print("Varianza Característica 5:")
print(statistics.variance(list(map(int,colum5))))

f.close()