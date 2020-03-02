#!/usr/bin/python3

# 1) Implemente o metodo define_default_city de acordo com a docstring definida no inicio da funcao. Utilize a clausula else no loop implementado.
# 2) Remova do arquivo capitais-BR.csv todas capitais dos estados do sudeste e teste se sua funcao estah robusta o suficiente.
# 3) Faca uma funcao que le o arquivo lista-cpf.txt, retorne a quantidade de CPF unicos (sem repeticao) e os escreva em um arquivo lista-cpf-unicos.txt. Eh necessario descompactar o arquivo lista-cpf.txt.tar.gz primeiro.


professor1 = {'id': 42, 'name': 'Alexandre Abreu', 'age': 30, 'state_origin': 'Minas Gerais', 'city_origin': 'Belo Horizonte', 'courses': ['Inteligência Artificial', 'Mineração de Dados', 'Programação para Internet I', 'Programação para Internet II']}

deleteCities = ['Vitória', 'São Paulo', 'Rio de Janeiro', 'Belo Horizonte']

def define_default_city(state):
# # 	''' Define a capital do estado de origem como city_origin para um professor existente no arquivo. Retorna True se a capital do estado de origem existe no arquivo capitais-BR.csv e False, caso contrario.

# # 	Keyword arguments:
# # 		state -- O estado de origem do professor
# # 	'''
	f = open("capitais-BR.csv")
	for string in f:
		if state in string:
			cidadeBuscada = string.split(';')[1]
			if cidadeBuscada[:-1] == professor1.get('city_origin'):
				print(True)
				print('A capital buscada está no arquivo ')
				break
	else:
		print(False)
		print('A capital buscada não está no arquivo ')
	f.close()

print('A cidade buscada é ' + professor1.get('city_origin'))
define_default_city(professor1.get('state_origin'))

def apagarCapitaisSudeste(deleteCities):

	print(deleteCities)
	f = open("capitais-BR.csv")
	f2 = open('arquivoLimpo.txt', 'w+')

	for line in f:
	    for word in deleteCities:
	    	line = line.replace(word,"")

	    f2.write(line)

	f.close()
	f2.close()

	f = open("capitais-BR.csv",'w+')
	f2 = open('arquivoLimpo.txt')

	for line in f2:
		f.write(line)
		print(line)

	f.close()
	f2.close()

apagarCapitaisSudeste(deleteCities)

def cpfsUnicos():

	file = open('listacpf.txt', 'r')
	file2 = open('lista-cpf-unicos.txt', 'w+')

	cpfs = []


	for cpfsFile in file:
		cpfs.append(cpfsFile)

	for indice in range(len(cpfs)):
		cont = 0

		# print('Indice1 cpf: ' + cpfs[indice] + '\n')
		
		for indice2 in range(indice, len(cpfs)):

			# if indice2 == len(cpfs)-1:
			# 	if cpfs[indice] == cpfs[len(cpfs)-1]:
			# 		cont+=1

			if cpfs[indice] == cpfs[indice2]:	
				cont += 1
		
		if cont >= 2:
			# print(cpfs[indice]) 
			file2.write(cpfs[indice])


	file.close()
	file2.close()

	f = open("lista-cpf-unicos.txt",'r')

	for line in f:
		print(line)

	f.close()

cpfsUnicos()

