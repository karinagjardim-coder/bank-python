saldo = float(input("Digite o seu Saldo"))
credito = float(input("Digite o valor do Crédito"))
if credito <= 0:
    print(f"valor invalido")
else:
    saldo += credito
    print(f"saldo final:{saldo}")

