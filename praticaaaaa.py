import requests

r= requests.get('https://viacep.com.br/ws/59184000/json/').json()
dados = r['cep']

print(dados)