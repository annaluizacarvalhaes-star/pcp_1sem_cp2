print("Olá, sejá bem-vindo ao banco!")
print("Para iniciarmos a simulacao, presisarei de alguns dados")

nome_cliente = (input("Insira o seu nome completo:"))

idade = int(input("Qual a sua idade:"))

renda_mensal = float(input("Qual o valor da sua renda messal:"))

valor_emprestimo = float(input("Qual o valor do emprestimo:"))

numero_parcelas = int(input("Qual o numer de parcelas (de 3 a 24):"))

#Regras de aprovação

def pode_aprovar(idade, renda_mensal, valor):
    return idade > 18 and valor <= (renda_mensal * 20)

#Definir a taxa
def definir_taxa(numero_parcelas):
    if numero_parcelas <= 6:
        return 0.05 
    elif numero_parcelas <= 12:
        return 0.08
    else:
        return 0.10
    
#Calcular valor das parcelas
def calcular_parcela(valor_emprestimo, taxa, numero_parcelas):
    numerador = taxa * (1 + taxa)**numero_parcelas
    denominador = (1 + taxa)**numero_parcelas - 1
    pagamento = valor_emprestimo * (numerador / denominador)
    return pagamento

#Calcular total
def calcular_total(parcela, numero_parcelas):
    return parcela * numero_parcelas

def calcular_juros(total, valor_pagamento):
    return total - valor_pagamento

#Resposta aprovado
if pode_aprovar(idade, renda_mensal, valor_emprestimo):
    taxa_aplicada = definir_taxa(numero_parcelas)
    valor_pg = calcular_parcela(valor_emprestimo, taxa_aplicada, numero_parcelas)
    valor_total = calcular_total(valor_pg, numero_parcelas)
    juros_totais = calcular_juros(valor_total, valor_emprestimo)

    print("-" * 30)
    print(f"\n Empréstimo APROVADO para {nome_cliente}!")
    print(f"Valor financiado: R$ {valor_emprestimo:.2f}")
    print(f"Taxa de juros aplicada: {taxa_aplicada * 100:.0f}% ao mês")
    print(f"Valor da parcela: R$ {valor_pg:.2f}")
    print(f"Valor total a ser pago: R$ {valor_total:.2f}")
    print(f"Total de juros pagos: R$ {juros_totais:.2f}")
    print("-" * 30)

#Resposta negado    
else:
    print("-" * 30)
    print(f"\n Empréstimo NEGADO para {nome_cliente}.")
    print("Motivo: O cliente não atende aos requisitos de idade ou limite de crédito.")
    print("-" * 30)
