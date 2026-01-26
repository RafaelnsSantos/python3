#faça um progrma que tenha uma funçao chamada notas() que pode receber várias notas de alunos e vai 
# retornar um dicionário com as seguintes informações:
# - Quantidade de notas 
# - A maior nota
# - A menor nota
# - A média da turma
# - A situação (opcional)
#adicione também as docstrings da funçao.
def notas(*valores,sit=True):
        """
        notas(*n , sit=false)
        fuçao e analisar notas e situaçao de varios alunos:
        :param n: aceita varios valores 
        :param sit: valor opcional, indicado se deve ou nao mostra situaçao do aluno.
        :return: dicionario com varios informaçoes sobre a turma
        """
        media = 0
        cont = 0
        lista = []
        dicionario = {}
        lista.append(dicionario.copy())
        dicionario["total"] = len(valores)

        #c e numero em valores: 
        for c in valores:
            #maior e menor :
            cont += 1
            if cont == 1:       
                dicionario["maior"] = c
                dicionario["menor"] = c
            elif c > dicionario["maior"]:
                dicionario["maior"] = c
            elif c < dicionario["menor"]:
                dicionario["menor"] = c
            media += c
        media = media / cont
        dicionario["media"] = media
        if sit == False:
            return dicionario
        else:
             if sit == True:
                if dicionario["media"] < 5:
                    dicionario["situaçao"] = "RUIM"
                    return dicionario
                elif 5 <= dicionario["media"] < 7:
                    dicionario["situaçao"] = "RAZOAVEL"
                    return dicionario
                elif dicionario["media"] >= 7:
                    dicionario["situaçao"] = "APROVADO"
                    return dicionario
            
#programa principal
resp = notas(5.5,9.5,10,6.5,sit=True)
print(resp)