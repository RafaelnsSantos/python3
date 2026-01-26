#crie um codigo em python que teste se o site pudim esta acessivel pelo computador usado
import urllib.request
def testar_site(a):
    try:
        valor = urllib.request.urlopen(a)
    except:
        print("\033[0;31msite fora do ar \033[m")
    else:
        print("\033[0;32mO site esta acessivel \033[m")
        #print(valor.read())

testar_site("http://pudim.com.br")