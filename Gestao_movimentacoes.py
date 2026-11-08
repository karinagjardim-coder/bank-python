saldo_inicial = 1000.0
saldo = saldo_inicial
movimentacoes = []

while True:
    menu = int(input("Digite 1 para realizar débito\nDigite 2 para realizar crédito\nDigite 3 para visualizar o saldo\nDigite 4 para visualizar o extrado\nDigite 0 para encerrar\nEscolha uma opção: "))
    
    if menu ==0:
        print("O programa está sendo encerrado")
        break
   
    elif menu ==1:
        debito = float(input("Digite o Valor para debitar: "))
        if debito <=0:
            print("Valor invalido")
        elif debito > saldo:
            print("Saldo insuficiente")
        else:
            saldo -= debito
            movimentacoes.append(f"Débito: -R$ {debito:.2f}")
            print(f"Saldo final: R$ {saldo:.2f}")
    
    elif menu ==2:
        credito = float(input("Digite o valor para crédito: "))
        if credito <=0:
            print(f"Valor invalido")
        else:
            saldo += credito
            movimentacoes.append(f"Crédito: +R$ {credito:.2f}")
            print(f"Saldo final: R$ {saldo:.2f}")

    elif menu ==3:
        print(f"Seu saldo é de: R$ {saldo:.2f}")

    
    elif menu ==4:
        print("\n====== EXTRATO BANCÁRIO ======")
        print(f"Saldo inicial: R$ {saldo_inicial:.2f}")

        if len(movimentacoes) ==0:
            print("Nenhuma movimentação realizada")
        else:
            print("\nmovimentacoes:")
            for movimentacao in movimentacoes:
                print(movimentacao)

        print("-------------------------------------")
        print(f"Saldo final: R$ {saldo:.2f}")
        print("=====================================")

    else:
        print("Opção inválida")