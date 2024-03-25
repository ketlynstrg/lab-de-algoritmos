
nmr1 = float(input("Digite o primeiro número: "))
nmr2 = float(input("Digite o segundo número: "))

if nmr1 == nmr2:
    print("Os números são iguais")
else:
    maior = max(nmr1, nmr2)
    menor = min(nmr1, nmr2)
    print(f"O maior número é {maior} e o menor número é {menor}.")
