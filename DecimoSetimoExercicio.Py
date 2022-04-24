'''
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
'''

from math import floor, ceil

AreaPintada = float(input("Digite o tamanho em metros quadrados da area a ser pintada: "))
LitroPorMetro = AreaPintada/6
LitrosLata = 18
CustoLata = 80
LitrosGalao = 3.6
CustoGalao = 25

#calculo para a lata
ApenasLata = ceil(LitroPorMetro/LitrosLata)
CustoApenasLata = ApenasLata*CustoLata
print("Você irá precisar de {} latas, pelo custo de {} reais".format(ApenasLata, CustoApenasLata))

#calculo para o galao
ApenasGalao = ceil(LitroPorMetro/LitrosGalao)
CustoApenasGalao = ApenasGalao*CustoGalao
print ("Você irá precisar de {} galoes, pelo custo de {} reais".format(ApenasGalao, CustoApenasGalao))

#calculo para a mistura economica
ApenasLata1 = floor(LitroPorMetro/LitrosLata)
CustoApenasLata1 = ApenasLata1*CustoLata

resto = LitroPorMetro%LitrosLata
GalaoNecessario = ceil(resto/LitrosGalao)

print ("Voce vai precisar de {} latas e {} galoes, pelo custo de {} reais".format(ApenasLata1, GalaoNecessario, CustoLata*ApenasLata1+GalaoNecessario*CustoGalao))

resto= input("Envie para sair")