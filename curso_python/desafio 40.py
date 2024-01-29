nota1 = float(input('Digite a primeira nota do aluno : ')) 
nota2 = float(input('Digite a segunda nota do aluno : '))
if (nota1 + nota2) / 2 < 5:
    print(f'Com as notas {nota1} e {nota2} a média é {(nota1 + nota2) / 2}\nReprovado')
elif(nota1 + nota2) / 2 > 5 and (nota1 + nota2) / 2 <= 6.9:
    print(f'Com as notas {nota1} e {nota2} a média é {(nota1 + nota2) / 2}\nRecuperação')     
elif(nota1 + nota2) / 2 >= 7:
    print(f'Com as notas {nota1} e {nota2} a média é {(nota1 + nota2) / 2}\nAprovado ')