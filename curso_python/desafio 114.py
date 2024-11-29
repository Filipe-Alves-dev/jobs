import requests


def verificarsite(url):
    try:
        resposta = requests.get(url)
        if resposta.status_code == 200:
            print(f'\033[92mO site {url} está funcionando normalmente.\033[m')
        else:
            print(f'\033[91mNão obtivemos resposta ao conectar ao site {url}, retorno: {resposta.status_code}\033[m')
    except requests.exceptions.RequestException as e:
        print(f'Ocorreu um erro ao tentar acessar o site {url}: {e}')


url = "http://www.pudim.com.br"
verificarsite(url)