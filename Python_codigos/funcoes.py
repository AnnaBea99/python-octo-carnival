# %%

# Relembrando dicionarios
livros = [
    {"nome": "As crônicas de Nárnia",
    "pages": "1300",
    "ano_lancamento": "1876"},

    {"nome": "Jogos Vorazes",
    "pages": "300",
    "ano_lancamento": "2006"}
]
for livro in livros:
    print(f'{livro['nome']}, {livro['pages']}, {livro['ano_lancamento']}')

# %%
def call_name(nome):
    print(f"Olá {nome}")

nome = input("Informe seu nome")
call_name(nome)

# %%
def f(x):
    resultado = 1 + x
    return resultado

f(10)

# %%
# Juros compostos

def juros_compostos(aporte:float, taxa:float, anos:int):
    """
    juros_compostos serve para calcular o retorno financeiro a partir de um aporte.
    Deve-se considerar o valor, a taxa de juros atual e o tempo (em anos) para cálculo do valor a ser retornado.
    
    aporte: 
        Um número float, que representa o valor em R$

    taxa:
        Um numero floa entre 0 e 1 que represente o valor da taxa de juros
    
    anos:
        Um número inteiro >= 1 que representa o tempo que o investimento terá
    """
    return aporte * (1 + taxa) ** anos

aporte = float(input("Quanto irá guardar? "))
taxa = float(input("Qual a taxa do banco? (Infome em decimais, valor entre 0 e 1)"))
anos = int(input("Quantos anos ficará guardado no banco?"))
juros_compostos(aporte, taxa, anos)

# %%

# Função que não retorna 
def ola_mundo():
    print("Olá Mundo!")

ola_mundo()

# %%

# treinando

def par_impar(numero:int):
    if numero % 2 == 0:
        return "par"
    else:
        return "ímpar"

numero = int(input('Informe um número: '))

resultado = par_impar(numero)
print(f'o {numero} é {resultado}')

#%%

def soma(a: float, b:float):
    return a + b

def media(a: float, b: float)->float:
    return soma(a,b)/2

a = float(input('informe um valor'))
b = float(input('informe um valor'))

print('Média', media(a,b))

# %%

# Argumentos não nomeados

def soma1(*args):
    return sum(args)

def media1(*args)->float:
    return soma1(*args)/ len(args)

numeros = []

while True:
    entrada = input('Digite um número ou fim para sair: ')
    if entrada == "fim":
        break
    numeros.append(float(entrada))

if numero:
    print(f'Média: {media1(*numeros)}')
    print(numeros)
else:
    print('Nenhum número informado!')

#%%

# quando coloca um parametro =0.03, faz com que ele se torne opcional na hora de preencher o argumento
# Argumentos nomeados
def calc_imposto(preco:float, tx_base=0.03, **kwargs):
    imposto = preco * tx_base

    for i in kwargs:
        print(i, kwargs[i])
        imposto += preco * kwargs[i]

    return imposto


# %%
impostos_gerais = {
    'muni': 0.01,
    'est': 0.005,
    'naci': 0.001
}
total = calc_imposto(100, 0.03, **impostos_gerais)
print(f'O total com impostos é: {total}')