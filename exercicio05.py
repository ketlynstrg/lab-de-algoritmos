import datetime

ano_nascimento = int(input("Digite o ano de nascimento: "))
ano_atual = datetime.datetime.now().year
idade = ano_atual - ano_nascimento

print(f"A pessoa tem ou fará {idade} anos este ano.")
