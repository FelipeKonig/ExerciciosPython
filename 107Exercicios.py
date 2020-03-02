# 1) Imprima os metodos disponiveis para uma lista e para uma tupla.
# 2) Faca um metodo para retornar apenas as diferencas entre as duas de metodos
# 3) Adicione as coordenadas (latitude, longitude) para os dicts professor1, professor2 e professor3. Copie os dicts do arquivo 106.py

professor1 = {'id': 42, 'name': 'Alexandre Abreu', 'age': 30, 'state_origin': 'Minas Gerais', 'courses': ['Inteligência Artificial', 'Mineração de Dados', 'Programação para Internet I', 'Programação para Internet II']}

professor2 = {'id': 37, 'name': 'Denilson Barbosa', 'age': 40, 'state_origin': 'Paraná', 'courses': ['Inteligência Artificial', 'Banco de Dados I', 'Banco de Dados II', 'Programação para Internet I']}

professor3 = dict(id=28, name='Jorge Armino', idade=37)

lista = (dir(list))

tupla = (dir(tuple))

print(lista)
print(tupla)

print(set(lista).symmetric_difference(tupla))

professor1["latitude"] = 10
professor1["longitude"] = 11

professor2["latitude"] = 12
professor2["longitude"] = 13

professor3["latitude"] = 14
professor3["longitude"] = 15

print(professor1['latitude'], professor1['longitude'])

print(professor2['latitude'], professor2['longitude'])

print(professor3['latitude'], professor3['longitude'])
