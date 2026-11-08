saldo_inicial = 500.0
saldo = saldo_inicial
movimentacoes = []

while True:
    caixa_loja = int(input("\nDigite 1 para registrar uma venda\nDigite 2 para registrar uma despesa\nDigite 3 para consultar o saldo\nDigite 4 para visualizar o extrato\nDigite 0 para encerrar\nEscolha uma opção: "))    

    if caixa_loja ==0:
        print("Processo Encerrado")
        break

    elif caixa_loja ==1:
        venda = float(input(f"Valor do Produto: R$ "))
        if venda <=0:
            print("Valor Invalido")
        else:
            saldo += venda
            movimentacoes.append(f"Venda: +R$ {venda:.2f}")
            print(f"Saldo final: R$ {saldo:.2f}")

    elif caixa_loja ==2:
        despesa = float(input(f"Valor Despesa: R$ "))
        if despesa <=0:
            print("Valor Invalido")
        elif despesa > saldo:
            print("Saldo Indisponível")
        else:
            saldo -= despesa
            movimentacoes.append(f"Despesa: -R$ {despesa:.2f}")
            print(f"Saldo final: R$ {saldo:.2f}")

    elif caixa_loja ==3:
        print(f"Saldo: R$ {saldo:.2f}")

    elif caixa_loja ==4:
        print("=======Visualizar Extrato======")
        print(f"Saldo Inicial: R$ {saldo_inicial:.2f}")

        if len(movimentacoes) ==0:
            print("Nenhuma Movimentação Realizada")
        else:
            print("\nmovimentacoes:")
            for movimentacao in movimentacoes:
                print(movimentacao)

        print("-------------------------------------")
        print(f"Saldo final: R$ {saldo:.2f}")
        print("=====================================")

    else:
        print("Opção invalida")
        
