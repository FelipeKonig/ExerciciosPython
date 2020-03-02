#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 21:38:42 2020

@author: felipe
"""
## Usando a lista: ['a','b','c']
# 1) Faca um loop para retornar: ['A','B','C']

lista = ['a','b','c']

for x in lista:
	print(x.upper())

    ## Usando os numeros: [0, 1, 3, 4, 5]
    # 2) Faca um loop para retornar a soma de todos os elementos da listas
    # 3) Faca um loop para retornar apenas os numeros impares

numeros = [0, 1, 3, 4, 5]

sum = 0
for x in numeros:
    sum += x
print(sum)

for x in numeros:
    if x % 2 != 0:
        print(x)

## usando a string: 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
# 4) Conte quantas palavras de tamanho >= 5 existe nessa string

string = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'

string2 = ''
cont = 0
for char in string:
    if char == ' ':
        if (len(string2) >= 5):
            print(string2)
            cont += 1
            print(cont)
        string2 = ''
    else:
        if char != ',' and char != '.':
            string2 += char

# 3) Usando list comprehension, crie uma lista com os multiplos de 3 de 0 ate 100

list = [i * 3 for i in range(100) if (i * 3) < 100]
print(list)
