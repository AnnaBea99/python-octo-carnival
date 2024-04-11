def sacar(valor):
  saldo = 500

  if saldo >= valor:
    print("valor sacado!")
    print("retire o seu dinheiro")
  
  print("Obrigado por ser nosso cliente")

def depositar(valor):
  saldo = 500
  saldo += 500
  print("teste",valor)

sacar(1000)
depositar(10000)
