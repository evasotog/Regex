#!/usr/bin/python3
#Script que compara 2 arrays uno de un archivo y otro de otro del que escoge el patron con regex y cuenta las coincidencias

import re
import numpy as np


with open ('pr2-21-22.txt') as f:

    file=f.read()
    funcion= re.findall(r'(?<=] )(.*)(?=.DLL)', "stringconelquecomparar" )
    
    funciones = np.array(funcion)

print(funciones.grep(Regexp.union(readFile("maliciosas.txt"))))

f.close()

def readFile(fileName):
        fileObj = open(fileName, "r") 
        words = fileObj.read().splitlines() #esta funcion pone el txt en un array
        fileObj.close()
        return words


