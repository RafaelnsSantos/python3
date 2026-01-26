#crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um 
# arquivo de texto simples. o sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar
#todas as pessoas cadastradas
import menu
import arquivo
import time

arq = "cursoemvideo.txt"
if not arquivo.arquivo_existe(arq):
      arquivo.criar_arquivo(arq)

      
while True:
    resultado = menu.menu(["Ver pessoas cadastradas","Cadastar nova pessoa","Sair do menu"])
    if resultado == 1:
        arquivo.lerArquivo(arq)
        time.sleep(0.5)
    elif resultado == 2:
            menu.cabeçalho("CADASTRAR NOVA PESSOA")
            nome = str(input("Nome: ")).strip()
            idade = menu.leiaint("Idade: ")
            arquivo.adicionarPessoas(arq,nome,idade)
            time.sleep(0.5)
    elif resultado == 3:
            menu.cabeçalho("Saindo do Sistema... Ate logo!")
            time.sleep(0.5)
            break
