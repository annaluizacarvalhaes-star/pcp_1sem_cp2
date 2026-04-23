
print("Ola, seja bem-vindo ao nosso sistema!")

codigo_estado = int(input("Insira o codigo do estado de origem da carga: "))

peso_toneladas = int(input("Informe o peso de sua carga em toneladas: "))

codigo_carga = int(input("Informe o codigo de sua carga: "))

# Cálculos
# Peso convertido em Kg
peso_em_kg = peso_toneladas * 1000

print(f"Peso convertido: {peso_em_kg} Kg")

# Preço da carga do caminhão por Kg
if 10 <= codigo_carga <= 20:
    preco_p_kg = 100
elif 21 <= codigo_carga <= 30:
    preco_p_kg = 250
elif 31 <= codigo_carga <= 40:
    preco_p_kg = 340
else:
    preco_p_kg = 0
    print("Codigo de carga nao encontrado!")

#Preço total da carga
preco_carga = peso_em_kg * preco_p_kg

#Valor do imposto
if codigo_estado == 1:
    porcentagem_imposto = 0.35
elif codigo_estado == 2:
    porcentagem_imposto = 0.25
elif codigo_estado == 3:
    porcentagem_imposto = 0.15
elif codigo_estado == 4:
    porcentagem_imposto = 0.05
else:
    porcentagem_imposto = 0.00

valor_imposto = preco_carga * porcentagem_imposto
valor_total = preco_carga + valor_imposto


print("-" * 30)
print(f"Peso em quilos: {peso_em_kg} kg")
print(f"Preço da carga: R$ {preco_carga:.2f}")
print(f"Valor do imposto: R$ {valor_imposto:.2f}")
print(f"Valor total: R$ {valor_total:.2f}")
print("-" * 30)


