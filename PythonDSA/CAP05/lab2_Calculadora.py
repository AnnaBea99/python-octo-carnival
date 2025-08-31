# Calculadora

# Tem que ter soma, subtração, multiplicação, divisão 
print('CALCULADORA')
print('----------------------------------------------')
operacao = int(input('Informe o número da operação desejada: \n 1 - Soma \n 2 - Subtração \n 3 - Multiplicação \n 4 - Divisão \n'))

def soma(num1,num2): return print(num1+num2)
def sub(num1,num2): return print(num1-num2)
def mult(num1,num2): return print(num1*num2)
def div(num1,num2): return print(num1/num2)

if operacao == 1:
    n1 = float(input('informe o primeiro numero: '))
    n2 = float(input('informe o segundo numero: '))
    soma(n1,n2)
elif operacao == 2:
    n1 = float(input('informe o primeiro numero: '))
    n2 = float(input('informe o segundo numero: '))
    sub(n1,n2)
elif operacao == 3:
    n1 = float(input('informe o primeiro numero: '))
    n2 = float(input('informe o segundo numero: '))
    mult(n1,n2)
elif operacao == 4:
    n1 = float(input('informe o primeiro numero: '))
    n2 = float(input('informe o segundo numero: '))
    div(n1,n2)
else:
    print('-------------------------------------------')
    print('operação não encontrada')

# if operacao == 1:
#     num1 = float(input('Informe o primeiro numero: '))
#     num2 = float(input('Informe o primeiro numero: '))
#     soma = num1 + num2
#     print(soma)
# elif operacao == 2:
#     num1 = float(input('Informe o primeiro numero: '))
#     num2 = float(input('Informe o primeiro numero: '))
#     sub = num1 - num2
#     print(sub)
# elif operacao == 3:
#     num1 = float(input('Informe o primeiro numero: '))
#     num2 = float(input('Informe o primeiro numero: '))
#     mult = num1 * num2
#     print(mult)
# elif operacao == 4:
#     num1 = float(input('Informe o primeiro numero: '))
#     num2 = float(input('Informe o primeiro numero: '))
#     divi = num1 / num2
#     print(divi)
# else:
#     print('operação não encontrada!')


