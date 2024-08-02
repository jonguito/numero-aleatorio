import random
numeros = [ 0,1,2,3,4,5,6,7 ]
numero_aleatorio = random.choice(numeros)
print('=-'*40)
print('VOU PENSAR EM UM NÚMERO DE 0 A 5.TENTE ADIVINHAR...')
print('=-'*40)
n = int(input('Em que número eu pensei?: '))

if n == numero_aleatorio:
    print('PARABÉNS!! VOCÊ CONSEGUIU ME VENCECR.')
else:
    print(f'GANHEI!! EU PENSEI NO NÚMERO {numero_aleatorio} E NÃO {n}')
