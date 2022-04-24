'''
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
'''
TamanhoArea= float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))
#1l 3m
LataTinta = 18.0
LataTintaValor= 80.0
custo = TamanhoArea/3*4.44444444444
print ("Você terá o custo de {0:.2f} reais para comprar {1:.2f} latas de tinta.".format(custo,((TamanhoArea/3)/LataTinta)))