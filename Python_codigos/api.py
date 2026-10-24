#%%
import requests

ceps = [
    "01001000",  # Praça da Sé, São Paulo
    "01310100",  # Av. Paulista, São Paulo
    "20040020",  # Centro, Rio de Janeiro
    "70040010",  # Esplanada, Brasília
    "30130010",  # Centro, Belo Horizonte
    "80010000",  # Centro, Curitiba
    "40020000",  # Comércio, Salvador
    "90010000",  # Centro, Porto Alegre
    "88010000",  # Centro, Florianópolis
    "66010000",  # Campina, Belém
]

url = 'https://viacep.com.br/ws/{cep}/json/'

dados = []

for i in ceps:
    resposta = requests.get(url.format(cep=i))
    if resposta.status_code == 200:
        dados.append(resposta.json())

dados