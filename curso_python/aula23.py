try: 
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a/b
except Exception as erro:
    print(f'Problema encontrado foi {erro.__class__}')
# except (ValueError, TypeError):
#     print('tivemos um problema com os tipos de dados que você digitou!')
# except ZeroDivisionError:
#     print('Erro, o número não pode ser dividido por zero!')
except KeyboardInterrupt:
    print('O usuário não informou os dados!')
# except Exception as erro:
#     print(f'O erro encontrado foi {erro.__cause__}')
else:
    print(f'O resultado é {r:.2f}')
finally:
    print('Volte sempre! Muito obrigado!')