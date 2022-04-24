altura = float(input("Digite sua altura: "))
sexo = input(("Qual seu sexo?"))
if sexo == "h":
    print ("Seu peso ideal é: {:.2f} kg".format((72.7*altura)-58))
else:
    print ("Seu peso ideal é: {:.2f} kg".format((62.1*altura) - 44.7))