#!/usr/bin/python3
"""
Created on Tue Feb 18 01:35:41 2020

@author: felipe
"""

# Como selecionar 'wed' pelo indice?

# Como verificar o tipo de 'mon'?

# Como separar 'wed' até 'fri'?

# Quais as maneiras de selecionar 'fri' por indice?

# Qual eh o tamanho dos dias e days_list?

# Como inverter a ordem dos dias?

# Como inserir a palavra 'zero' entre 'a' e 1 de list?

# Como limpar list?

# Como deletar list?

# Como atribuir o ultimo elemento de list na variavel ultimo_elemento e remove-lo de list?


weekdays = ['mon','tues','wed','thurs','fri']
days_list = ['mon','tues','wed','thurs','fri','sat','sun']
list1 = ['a', 1, 3.14159265359]

# 1
print(weekdays[2])

#2
print(type(weekdays[0]))

#3
print(weekdays[2:])

#4
print(weekdays[4])
print(weekdays[4:])

#5
print(len(weekdays))
print(len(days_list))

#6
weekdays.reverse()
print(weekdays)

#7
list1.insert(1,'zero')
print(list1)

#8
#list1.clear()
#print(list1)

#10
ultimo_elemento = list1.pop()
print(ultimo_elemento)
print(list1)























