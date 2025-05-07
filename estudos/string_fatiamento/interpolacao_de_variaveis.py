nome = 'Anna'
idade = 24
profissao = 'Programadora'
linguagem = 'Python'

pessoa = {"nome": "Anna", "idade": 24, "profissao": "analista", "linguagem": "python"}

# Modo não utilizado mais %, deixa o código muito complexo por ter que escrever várias váriaveis
print("Olá me chamo %s. Eu tenho %d anos de idade, trabalho como %s e estou fazendo um curso de %s" %(nome, idade, profissao, linguagem))

# Método FORMAT exemplo muito parecido com o de %
print("Olá me chamo {}. Eu tenho {} anos de idade, trabalho como {} e estou fazendo um curso de {}".format(nome, idade, profissao, linguagem))

print("Olá me chamo {3}. Eu tenho {2} anos de idade, trabalho como {1} e estou fazendo um curso de {0}".format(linguagem, profissao, idade, nome))

print("Olá me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou fazendo um curso de {linguagem}".format(nome=nome, idade=idade, profissao=profissao, linguagem=linguagem))

print("Olá me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou fazendo um curso de {linguagem}".format(**pessoa))

# Método F-STRING melhor método para ser utilizado, o código fica mais limpo
print(f"Olá me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou fazendo um curso de {linguagem}")

#EXEMPLO 2

PI = 3.14159
print(f"valor de PI: {PI:.2f}")
print(f"valor de PI: {PI:10.2f}")