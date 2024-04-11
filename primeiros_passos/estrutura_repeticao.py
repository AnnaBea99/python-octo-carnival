# EXEMPLO 1

texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
  if letra.upper() in VOGAIS:
    print(letra, end="")

print()

#  FUNÇÃO RANGE
# range(stop) -> range object
# range(start, stop[, step]) -> range object
# list(range(4))

for numero in range(0,11):
  print(numero, end=" ")

print()

#tabuada do 5
for numero in range(0,51,5):
  print(numero, end=" ")

# WHILE / else
opcao = -1

while opcao != 0:
  opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))

  if opcao == 1:
    print("Sacando")
  elif opcao == 2:
    print("EXIBINDO EXTRATO ...")
else:
  print("Obrigado por usar nossso sistema bancário, até logo!")