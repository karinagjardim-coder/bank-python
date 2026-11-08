lista = ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Curitiba", "Florianopolis", "Porto Alegre"]
lista.append("Cuiaba")
print(lista[2])
lista.pop(3)
lista.remove("Porto Alegre")
print(lista[4])
print(lista[0:2])
print(lista[2:])
for cidade in lista:
    print(cidade)
    if "Curitiba" == cidade:
        print("Curitiba existe nesta lista")
    