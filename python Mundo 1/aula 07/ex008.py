#escreva um programa que leia um valor em metros e a exiba convertido em centimetros e milimetros
print("="*30)
print("|    conversor  de M para cm e mm   |")
print("="*30)
metros = float(input("digite o valor em metros: "))
km = metros/1000
hm = metros/100
dam = metros/10
dm = metros * 10
cm = metros*100
mm = metros * 1000 
print("o valor de {} Metros em: \n km: {} \n  hm: {} \n dam {} \n dm {} \n cm {} \n mm {}".format(metros,km,hm,dam,dm,cm,mm))
