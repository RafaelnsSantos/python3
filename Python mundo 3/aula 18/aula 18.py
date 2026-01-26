#dados = ['pedro' , 19,'maria',20,'joao',32]
#pessoas = []
#pessoas.append(dados[:])
#ou
#pessoas = [['pedro' , 19],['maria',20],['joao',32]]
#print(pessoas[0][0])
#ou
#teste = []
#galera = []
#teste.append("rafael")
#teste.append("17")
#galera.append(teste[:])
#teste [0] = 'gustavo'
#teste [1] =  40
#galera.append(teste[:])
#print(galera)

# tambem:
galera = []
dados = []
#oque ta acontecendo e: o c ta repetindo . em quanto tiver repetindo o sistema vai pergunta nome e idade e vai jogar
#em dados depois dados e jogado em lista galera e logo em seguida dados toma clear resumo: leitura de dados

for c in range (3):
    dados.append(str(input("Nome: ")))
    dados.append(int(input("Idade: ")))
    galera.append(dados[:])
    dados.clear()
    
#aqui e analise de menor ou maior de idade:
for p in galera:
    if p[1] >= 18:
        print(f'{p[0]} e maior de idade')
    else:
        print(f'{p[0]} e menor de idade')