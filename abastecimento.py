print("SISTEMA DE CONTROLE DE ABASTECIMENTO")

litros = float(input("Quantidade de litros abastecidos: "))
preco = float(input("Preço por litro: "))

total = litros * preco

print(f"Valor total do abastecimento: R$ {total:.2f}")