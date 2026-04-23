# Leitura dos três valores de ponto flutuante
lados = list(map(float, input("Digite os três lados do triângulo (separados por espaço): ").split()))

# Ordenação decrescente: o maior valor será atribuído a A
lados.sort(reverse=True)
a, b, c = lados

# 1. Verificação se os lados formam um triângulo
if a >= (b + c):
    print("NAO FORMA TRIANGULO")
else:
    # 2. Classificação quanto aos ângulos
    # Usamos o Teorema de Pitágoras como base de comparação
    a2 = a**2
    bc2 = b**2 + c**2

    if a2 == bc2:
        print("TRIANGULO RETANGULO")
    elif a2 > bc2:
        print("TRIANGULO OBTUSANGULO")
    else:
        print("TRIANGULO ACUTANGULO")

    # 3. Classificação quanto aos lados
    if a == b == c:
        print("TRIANGULO EQUILATERO")
    elif a == b or b == c or a == c:
        print("TRIANGULO ISOSCELES")
