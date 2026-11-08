print("SISTEMA DE CONTROLE DE ABASTECIMENTO")

litros = float(input("Quantidade de litros abastecidos: "))
preco = float(input("Preço por litro: "))
km = float(input("Quilometragem percorrida: "))

total = litros * preco
consumo = km / litros

print(f"Valor total: R$ {total:.2f}")
print(f"Consumo médio: {consumo:.2f} km/l")