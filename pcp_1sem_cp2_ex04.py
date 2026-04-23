nome_funcionário = input("digite seu nome: ")

print("Selecione seu cargo: ")
print(" 1 - gerente ")
print("2 - analista ")
print("3 - assistente ")
print("4 - estagiário ")


cargo_input = int(input("Digite o número correspondente ao seu cargo: "))
bonus1 = 0

salário = float(input("Digite o seu salário: "))
horas_extras = int(input("Digite a quantidade de horas extras trabalhadas: "))
faltas = int(input("Digite a quantidade de faltas: "))
bonus_resposta = input("Você recebeu bônus? (sim/não): ").lower()

if bonus_resposta == "sim":
  if cargo_input == 1:
      bonus1 = 1000
      print("Seu bônus é de R$1000,00 \n")
  elif cargo_input == 2:
     bonus1 = 500
     print("Seu bônus é de R$500,00 \n")
  elif cargo_input == 3:
     bonus1 = 300
     print("Seu bônus é de R$300,00 \n")
  else:
     bonus1 = 100
     print("Seu bônus é de R$100,00 \n")
else:
  print("Você não recebeu bônus.\n")

def calculo_hora_extra (horas_extras, salário):
  return horas_extras * (0.015 * salário)

def calculo_faltas (faltas, salário):
  return faltas * (0.02 * salário)

print(f"Seu salário bruto é de: R$ {salário}")
print("Seu total de acrescimos é de:", calculo_hora_extra(horas_extras, salário))
print("Seu total de descontos é de:", calculo_faltas(faltas, salário))

# Calculo do salário total
salario_total = salário + bonus1 + calculo_hora_extra(horas_extras, salário) - calculo_faltas(faltas, salário)

print("Seu salário total é de: R$", salario_total)