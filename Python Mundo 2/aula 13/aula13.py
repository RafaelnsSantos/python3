"""for c in range (1,10):
    print("o9")"""

#para conta para tras 
#               inicio fim  pulo
#for c in range (10    ,0,   -1):
    #print(c)
s = 0
n1 = int(input("digite um numero de vezes que quer soma: "))
for c in range (0,n1):
    n = int(input("digite um valor para somar "))
    s += n
print("o somatario dos numeros foi {}".format(s)) 
