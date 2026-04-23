nome_funcionário = input("digite seu nome: ")

cargos = {
        "1": "Gerente",
        "2": "Analista",
        "3": "Assistente",
        "4": "Estagiário"
    }
print("\n selecione seu cargo:")
print(" 1 - gerente")
print("2 - analista")
print("3 - assistente")
print("4 - estagiário")
cargo= input(print("selecione seu cargo: "))

salário_base= float(input(print(" Digite seu salario base:")))
horas_extras= input(print(" digite suas horas extras trabalhadas: "))
faltas_mes= input(print(" Digite suas faltas no mês: "))
bonus= input(print("Recebeu bonus esse mês? (sim/não): "))
if bonus == "sim":
  valor_bonus= input(print(" Digite o valor recebido: "))
else:
  print(" continuar ")

  valor_hora_extra = float(horas_extras) * (salário_base * 0.15)
  print(f" o valor ganho de horas extras: {valor_hora_extra}")

  desconto_falta = float(faltas_mes) * (salário_base * 0.2)
  print(f" o valor descontado por faltas no mes foi: {desconto_falta}")

  cargos_bonus = {
      "1": ["Gerente", 1000.00],
      "2": ["Analista", 500.00],
      "3": ["Assistente", 300.00],
      "4": ["Estagiário", 100.00]

  }

if cargo == 1:
  bonus1 = 1000
elif cargo == 2:
  bonus1 = 500
elif cargo == 3:
 bonus1 = 300
else:
  bonus1 = 100

print(f" o valor do salario bruto é: {salário_base}")

total_acrescimo = float(valor_hora_extra + bonus1)
print(f" o valor total de acrecimos de bonus no salario total é : {total_acrescimo}")

total_descontos= float(salário_base) - (desconto_falta)
print(f" o valor descontado por faltas do salário bruto foi: {total_descontos}")

salario_final = float (total_acrescimo) + (total_descontos)
print(f" o valor do salário recebido no final do mes foi: {salario_final}")