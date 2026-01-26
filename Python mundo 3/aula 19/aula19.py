#dicionarios
#pessoas = {'nome':'gustavo', 'sexo': 'M' ,'idade': 22}
#print(f"O {pessoas['nome']}tem {pessoas['idade']} anos")
#dicinario sem usar o enumerate
#pessoas['peso'] = 100
#for k , v in pessoas.items():
    #print(f"{k} {v}")


#E
'''brasil = []
estado1 = {"uf" : 'SAO PAULO' , "sigla" : 'SP'}
estado2 = {"uf":'BAHIA' , "sigla" :'BA'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)'''

#um jeito mais facil para criar uma copia de um dicionario
estado = {}
brasil = []
for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
print(brasil)
#esse for vai mostrar cada dicionario dentro da lista brasil
'''for e in brasil:
    print(e)'''
#esse for vai mostrar cada chave e valor de cada dicionario dentro da lista brasil
'''for e in brasil:
    for k , v in e.items():
        print(f"O campo {k} tem valor {v}")'''
#ou pode ser feito assim
for e in brasil: #po  e ele vai ler cada dicionario dentro da lista brasil
    for v in e.values(): #e o v ele vai ler cada valor dentro do dicionario
        print(v, end=' ')
    print()