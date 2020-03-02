#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 12:47:26 2020

@author: felipe
"""

book1 = 'Homo Deus by Yuval Noah Harari, 2015'
book2 = 'Antifragile by Nassim Nicholas Taleb, 2012'
book3 = 'Fooled by Randomness by Nassim Nicholas Taleb, 2001'


palindrome_one = 'ovo'
palindrome_two = 'Natan'
palindrome_three = 'luz azul'
palindrome_four = 'caneta azul'

# 1) Extraia o titulo do livro da string
# 2) Salve o titulo de cada livro em uma variável
# 3) Quantos caracteres cada título tem?
# 4) Imprima com a formatacao: {Titulo} - {Autor}, {Ano}
# 5) Verifique se uma palavra é uma palindrome perfeita.
# Palindrome perfeito sao palavras que ao serem escritas em ordem reversa,
# resultam na mesma palavra.
# Ignore espacos e caixa alta

#1
print(book1[0:9])

#2
titleBook1 = book1[0:9]
print(titleBook1)

titleBook2 = book2[0:11]
print(titleBook2)

titleBook3 = book3[0:19]
print(titleBook3)

#3
print(len(titleBook1))
print(len(titleBook2))
print(len(titleBook3))

#4
title1 = book1[0:9]
author1 = book1[13:30]
year1 = book1[32:36]

print('{0} by {1}, {2}'.format(title1, author1, year1))

title2 = book2[0:11]
author2 = book2[15:36]
year2 = book2[38:42]

print('{0} by {1}, {2}'.format(title2, author2, year2))

title3 = book3[0:19]
author3 = book3[24:44]
year3 = book3[47:51]

print('{0} by {1}, {2}'.format(title3, author3, year3))

#5


print(palindrome_one == palindrome_one[::-1])
    
palindrome_two2 = palindrome_two.lower() 

print(palindrome_two2 == palindrome_two2[::-1])
    
palindrome_three2 = ''.join(palindrome_three.split())
    
print(palindrome_three2 == palindrome_three2[::-1])
    
palindrome_four2 = ''.join(palindrome_four.split())
    
print(palindrome_four2 == palindrome_four2[::-1])
    

    












