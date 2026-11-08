estoque_inicial = 50
estoque = estoque_inicial
movimentacoes = []

while True:
    menu = int(input("Digite 1 para registrar entrada de produtos\nDigite 2 para registrar saída de produtos\nDigite 3 para consultar estoque\nDigite 4 para visualizar movimentações\nDigite 0 para encerrar\nEscolhe uma Opção:"))

    if menu ==0:
        print("Encerrar")
        break

    elif menu ==1:
        entrada = int(input("Informe a quantidade de entrada do Produto: "))
        if entrada <= 0:
            print("Quantidade Invalida")
        else:
            estoque += entrada
            movimentacoes.append(f"Entrada: +{entrada}")
            print(f"Estoque Final: {estoque}")


    elif menu ==2:
        saida = int(input("Informe a quantidade de saida do Produto: "))
        if saida <= 0:
            print("Quantidade Invalida")
        elif saida > estoque:
            print("Estoque Insuficiente")
        else:
            estoque -= saida
            movimentacoes.append(f"Saída: -{saida}")
            print(f"Estoque Final: {estoque}")
    
    elif menu ==3:
        print(f"Estoque: {estoque}")
   
    elif menu ==4:
        print("\n=====ENTRADA E SAÍDA====")
        print(f"Estoque Inicial: {estoque_inicial}")

        if len(movimentacoes) ==0:
            print("Sem Movimentação")
        else:
            print("\nMovimentação")
            for movimentacao in movimentacoes:
                print(movimentacao)

            print("-------------------------------------")
            print(f"Estoque {estoque}")
            print("=====================================")  

    else:
        print("Opção Invalida")
