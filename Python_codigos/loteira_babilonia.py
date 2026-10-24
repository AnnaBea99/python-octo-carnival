# Construa um programa que realiza o sorteio de um número entre 1 e 15
# O usuário terá 3 chances de acertar o valor.
# A cada tentativa você deve informar se o chute é maior ou menor que o número sorteado.
# Caso o usuário acerte, dê os parabéns.
import random

def get_input():
    while True:
        try:
            chute_usuario = int(input('Informe um número entre 1 e 15: '))
        except ValueError as err:
            print('Valor inválido!')
            continue
        if 1 <= chute_usuario <= 15:
            return chute_usuario

        print('Valor inválido! Tem que ser um número entre 1 e 15')

def check_numbers(sorteio, usuario):
    if usuario == sorteio:
        print('Parabéns!')
        return True
    
    elif usuario > sorteio:
        print('O número informado é maior, tente um número mais baixo')
        return False
    
    else:
        print('Número muito baixo. Tente um número mais alto')
        return False

numero_sorteio = random.randint(1,15)

for i in range(3):

    chute_usuario = get_input()

    if check_numbers(sorteio=numero_sorteio, usuario=chute_usuario):
        break
        
    
else:
    print(f'Suas tentativas acabaram!\nNúmero sorteado: {numero_sorteio}')