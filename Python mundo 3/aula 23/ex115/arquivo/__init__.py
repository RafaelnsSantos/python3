from menu import cabeçalho
def arquivo_existe(nome):
    try:
        arquivo = open(nome,'rt')#vai abrir em read e test
        arquivo.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criar_arquivo(nome):
    try:
        arquivo = open(nome,"wt+")#se caso existir ele vai poder escrever e se nao existir o + vai criar
        arquivo.close()
    except:
        print("Houve um ERRO na criaçao do arquivo")
    else:
        print(f"arquivo {nome} criado com sucesso!")


def lerArquivo(nome):
    try:
        arquivo = open(nome,"rt")
    except:
        print("Houve um erro na leitura do arquivo")    
    else:
        cabeçalho("PESSOAS CADASTRADAS")
        for linha in arquivo:
            dado = linha.split(",")
            dado[1] = dado[1].replace('\n',"")
            print(f"{dado[0]:<30}{dado[1]:>3} anos")
    finally:
        arquivo.close()
    
def adicionarPessoas(arq , nome="Desconhecido",idade=0):
    try:
        arquivo = open(arq,'at')
    except:
        print("Houve um poblema no momento de abrir o arquivo")
    else:
        try: 
            arquivo.write(f"{nome},{idade}\n")
        except:
            print("Houve um erro na hora de escrever os dados!")
        else:
            print(f"novo registro de {nome} adicionado. ")
            arquivo.close()