valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))

print("1. Somar os dois valores")
print("2. Subtrair os dois valores")
print("3. Multiplicar os dois valores")
print("4. Dividir os dois valores")

opcao = int(input("Escolha a opção: "))

if opcao == 1:
    resultado = valor1 + valor2
elif opcao == 2:
    resultado = valor1 - valor2
elif opcao == 3:
    resultado = valor1 * valor2
elif opcao == 4:
    resultado = valor1 / valor2


print("Resultado:",resultado)