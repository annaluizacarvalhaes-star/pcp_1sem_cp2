cp1 = float(input(print("Digite a nota do checkpoint 1: ")))
cp2 = float(input(print("Digite a nota do checkpoint 2: ")))
cp3 = float(input(print("Digite a nota do checkpoint 3: ")))
sp1 = float(input(print("Digite a nota do sprint 1: ")))
sp2 = float(input(print("Digite a nota do sprint 2: ")))
gs = float(input(print("Digite a nota do Global Solution: ")))

if cp1< cp2 or cp1<cp3:
    caso1= (((cp2 + cp3 + sp1 + sp2)/ 4) * 0.4) + gs * 0.6
    media1 = caso1 * 0.40
    print(f'Sua média final é {caso1} \n')
    print(f'Sua média com peso é: {media1} ')

elif cp2< cp1 or cp2<cp3:
    caso2= (((cp1 + cp3 + sp1 + sp2)/ 4) * 0.4) + gs * 0.6
    media2 = caso2 * 0.40
    print(f'Sua média final é {caso2} \n')
    print(f'Sua média com peso é: {media2} ')


elif cp3<cp1 or cp3<cp2:
    caso3 = (((cp2 + cp3 + sp1 + sp2)/ 4) * 0.4) + gs * 0.6
    media3 = caso3 * 0.40
    print(f'Sua média final é {caso3} \n')
    print(f'Sua média com peso é: {media3} ')


elif cp1 == cp3 or cp1 == cp2 or cp3 == cp1:
    caso4 = (((cp2 + cp3 + sp1 + sp2) / 4) * 0.4) + gs * 0.6
    media4 = caso4
    print(f'Sua média final é {caso4} \n')
    print(f'Sua média com peso é: {media4} ')

else:
    print("Notas inválidas")


