multa = 4.0
PesoPeixe = float(input("Quantos kg de peixe? "))
if PesoPeixe>50:
    multa = (PesoPeixe-50)*multa
    print ("Sua multa é de {} reais".format(multa))
else:
    print ("Não é cabível multa.")