#faça um pograma que leia uma frase pelo teclado e mostre Quantas vezes aparecem  a letra ''A'' 
# em que posiçao ela aparece a 1 vez , em que posiçao aparece na ultima vez.
frase = str(input("Digite uma frase: ")).strip().lower()
print("A letra A aparece {} vezes na frase.".format(frase.count("a")))
print("A 1 Letra A apareceu na posiçao {} ".format(frase.find('a')+1))
print("A ultima letra A Apareceu na posiçao {} ".format(frase.rfind('a')+1))