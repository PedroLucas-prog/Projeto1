from math import pow

NumINT = int(input("Digite um numero inteiro: "))
NumINT2 = int(input("Digite outro numero inteiro: "))
NumREAL = float(input("Digite um numero real: "))

print ("O produto do dobro do primeiro com metade do segundo equivale a: {}".format((NumINT*2)*(NumINT2/2)))
print("A soma do triplo do primeiro com o terceiro: {}".format((NumINT*3)+NumINT2))
print ("O terceiro elevado ao cubo: {}".format(pow(NumREAL,3)))