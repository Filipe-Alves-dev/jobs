from datetime import date

dados = dict()
ano_atual = date.today().year

print('\033[1;33m-\033[m'* 40)    
dados["nome"] = str(input('Nome: '))
dados["idade"] = ano_atual - int(input('Ano de nascimento: ')) 
dados["ctps"] = int(input('Número CTPS: '))

if dados["ctps"] == 0:
    for k, v in dados.items():
        print(f'{k} tem o valor {v}')
        
else:
    if dados["ctps"] != 0:
        dados["contratação"] = int(input('Ano de contratação: '))
        dados["salário"] = float(input('Salário: R$ '))
        dados["aposentadoria"] = (35 - (ano_atual - dados["contratação"])) + dados["idade"]
    print('\033[1;33m-\033[m'* 40)     
    for k, v in dados.items():
        print(f'{k} tem o valor : {v}')
    print('\033[1;33m-\033[m'* 40)
    