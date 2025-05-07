while True:
  numero = int(input("Informe um número: "))

  if numero == 10:
    break

  print(numero)

for numero in range(100):
  if numero % 2 == 0:
    # ele não vai exibir o número 10
    continue
    #break

  print(numero, end=" ")