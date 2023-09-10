numero1=0
numero2=0
operacao=0

numero1=int(input("Digite o primeiro valor: "))
operacao=int(input("Escolha a operção:  1(+) 2(-) 3(*) 4(/): "))
numero2=int(input("Digite o segundo valor: "))

if operacao == 1:
    print("Resultado: ", numero1+numero2)
elif operacao == 2: 
    print("Resultado: ", numero1-numero2)
elif operacao == 3:
    print("Resultado: ", numero1*numero2)
elif operacao == 4:
    if numero2 == 0:
        print("Não é possivel divisão por 0 ")
    elif numero2 > 0:
        print("Resultado: ", numero1/numero2)