financiamento = float(input("Informe o valor do Financiamento:"))
qtde_prestacoes = int(input("Informe a quantidade de Prestações:"))
salario = float(input("Informe o seu salário:"))
valor_mensal = financiamento / qtde_prestacoes
limite = salario * 0.4
if valor_mensal > limite:
    print(f"Crédito Negado - Valor Mensal acima do limite")
else:
    print(f"Crédito Aprovado")
    