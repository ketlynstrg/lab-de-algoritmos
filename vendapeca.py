valorPeca = float(input("Digite o valor da peça: R$ "))
opcaoPagamento = int(input("Escolha a forma de pagamento (1 - À vista, 2 - Duas vezes, 3 - Três vezes): "))

if opcaoPagamento == 1:
    valorParcela = valorPeca
elif opcaoPagamento == 2:
    valorParcela = valorPeca / 2
elif opcaoPagamento == 3:
    valorParcela = valorPeca / 3
else:
    print("Opção de pagamento inválida!")

print(f"O valor das parcelas será de R${valorParcela:} cada.")