saldo:float = 3000
debito = float(input("Digite o valor para debitar:"))
if debito <= 0:
    print(f"valor invalido")
elif debito > saldo:
    print(f"valor insuficiente")
else:
    #saldo = saldo - debito (é a regra de calculo da linha nove)
    saldo -= debito
    print(f"saldo final é:{saldo}")