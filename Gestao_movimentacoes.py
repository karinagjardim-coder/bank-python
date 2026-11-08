saldo = 1000.0
while True:
    menu = int(input("Digite 1 para realizar débito\nDigite 2 para realizar crédito\nDigite 3 para visualizar o saldo\nDigite 0 para encerrar"))
    if menu ==0:
        print("O programa está sendo encerrado")
        break
    elif menu ==1:
        debito = float(input("Digite o Valor para debitar: "))
        if debito <=0:
            print(f"Valor invalido")
        elif debito > saldo:
            print(f"Saldo insuficiente")
        else:
            saldo -= debito
            print(f"Saldo final: {saldo}")
    elif menu ==2:
        credito = float(input("Digite o valor para crédito: "))
        if credito <=0:
            print(f"Valor invalido")
        else:
            saldo += credito
            print(f"Saldo final: {saldo}")
    elif menu ==3:
        print(f"Seu saldo é de: {saldo}")
    else:
        print("Opção Invalida")