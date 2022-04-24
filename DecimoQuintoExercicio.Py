'''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
'''
SalarioHora= float(input("Quanto você recebe por hora? "))
HorasTrabalhadas = float(input("Quantas horas trabalha no mês?"))
SalarioBruto=SalarioHora*HorasTrabalhadas
print("Seu salário bruto é: {:.2f} reais".format(SalarioBruto))

print("Você pagou ao INSS {:.2f}".format((SalarioBruto/100)*8))
print("Você pagou ao sindicato {:.2f}".format((SalarioBruto/100)*5))
SalarioLiquido = SalarioBruto-((SalarioBruto/100)*8)-((SalarioBruto/100)*5)-((SalarioBruto/100)*11)
print("Seu salário liquido é de {:.2f}".format(SalarioLiquido))