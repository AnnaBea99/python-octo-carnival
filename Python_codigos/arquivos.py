# %%
nome_arquivo = './historia.txt'

# Abre o arquivo e formato de leitura
open_file = open(nome_arquivo)

#%%
# Lê o conteúdo do arquivo
conteudo = open_file.read()
print(conteudo)

#%%
# Fecha o arquivo, precisa sempre fechar para não corromper
open_file.close()

# %%

# Forma mais correta
# o with serve para quando o arquivo estiver aberto com ele quando sai o arquivo fecha automaticamente
with open(nome_arquivo) as open_file:
    conteudo = open_file.read()

print(conteudo)

# %%

# Escrever arquivos

# r -> leitura
# w -> escrita
# a -> adiciona a partir do último caracter

txt = 'adicionando nova linha no arquivo\n'

nome_arquivo = './historia2.txt'

with open(nome_arquivo, mode='a') as open_file:
    open_file.write(txt)

#%%

arquivo = './data.csv'

with open(arquivo) as open_file:
    lines = open_file.readlines()

for l in lines:
    print(l)
#%%

dados = dict()

chaves = lines[0].strip('\n').split(';')
for c in chaves:
    dados[c] = []

#%%

for l in lines[1:]:

    valores = l.strip('\n').split(';')

    for i in range(len(valores)):

        dados[chaves[i]].append(valores[i])

#%%

idades = []

for i in dados['idade']:
    idades.append(int(i))

media = sum(idades)/len(idades)
print(f'A média de idades é: {media}')