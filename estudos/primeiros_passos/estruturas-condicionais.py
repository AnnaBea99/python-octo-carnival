# IF
saldo = 2000.0

saque = float(input("Informe valor do saque: "))

if saldo >= saque:
  print("Realizando saque!")

if saldo < saque:
  print("Saldo insuficiente!")

# IF ELSE

if saldo >= saque:
  print("Realizando saque!")
else:  
  print("Saldo insuficiente!")

# ELIF permite verificar múltiplas condições sequencialmente. Se a condição do if for falsa, o Python verifica a condição do elif subsequente, e assim por diante

opcao = int(input("Informe uma opção: [1] Sacar \n[2] extrato: "))

if opcao == 1:
  valor = float(input("Informe a quantia para o saque: "))
elif opcao == 2:
  print("Exibindo o extrato....")
else:
  print("Opção inválida")

# EXEMPLO 2

MAIOR_IDADE = 18
IDADE_ESPECIAL = 12

idade = int(input("Informe sua idade:"))

if idade >= MAIOR_IDADE:
  print("Maior de idade, pode tirar a CNH")

if idade >= MAIOR_IDADE:
  print("Maior de idade, pode tirar a CNH")

if idade >= MAIOR_IDADE:
  print("Maior de idade, pode tirar a CNH")
else:
  print("Maior de idade, pode tirar a CNH")

if idade >= MAIOR_IDADE:
  print("Maior de idade, pode tirar a CNH")
elif idade == IDADE_ESPECIAL:
  print("Pode assistir aula teórica, mas não pode aula prática")
else:
  print("Ainda não pode tirar a CNH")

# IF ANINHADO

conta_normal = True
conta_universitaria = True

saldo = 2000
saque = 2500
cheque_especial = 450

if conta_normal:
  if saldo >= saque:
    print("Saque bem sucedido")
  elif saque <= (saldo + cheque_especial):
    print("Saque usando cheque especial")
elif conta_universitaria:
  if saldo >= saque:
    print("Saque bem sucedido")
  else:
    print("saldo insuficiente")

# IF TERNÁRIO = IF DE UMA LINHA SÓ

status = "Sucesso" if saldo >= saque else "Falha"

print(f"{status} ao realizar o saque!")