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