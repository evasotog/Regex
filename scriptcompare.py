#!/usr/bin/python3
#Script que compara 2 arrays uno de un archivo y otro de otro del que escoge el patron con regex y cuenta las coincidencias

import re
import numpy as np

def readFile(fileName):
        fileObj = open(fileName, "r") 
        words = fileObj.read().splitlines() #esta funcion pone el txt en un array
        fileObj.close()
        return words


with open ('pr2-21-22.txt',"r") as f:

    file=f.read()
    funcion= re.findall(r'(?<=] )(.*)(?=.DLL)', file) #funcion es una lista
  
    array = readFile("maliciosas.txt")
    listamal = np.array(array).tolist()
    print(listamal)

    results = {}
    for i in listamal:
        results[i] = funcion.count(i) 

print("###################################################################################################################################")
print(results)


f.close()


