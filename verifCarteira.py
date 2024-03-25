
tipoCarteira = input("Digite o tipo da sua carteira de motorista (A, B, C, D ou E): ")

if tipoCarteira == 'A':
    print("Você pode dirigir motos e triciclos")
elif tipoCarteira == 'B':
    print("Você pode dirigir carros de passeio")
elif tipoCarteira == 'C':
    print("Você pode dirigir veículos de carga acima de 3,5 toneladas")
elif tipoCarteira == 'D':
    print("Você pode dirigir veículos com mais de oito passageiros")
elif tipoCarteira == 'E':
    print("Você pode dirigir veículos com unidade acoplada acima de 6 toneladas")
else:
    print("Inválido")