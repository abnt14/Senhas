#Algoritmo senhas para fila
#Por Saulo de Freitas em 06/05/2022

import random

quantidade_pessoas_fila = random.randint(1,30)
posicao_fila = quantidade_pessoas_fila + 1
senha = posicao_fila

nome = input(' Insira  o seu nome:\n ')

if(posicao_fila > 30):
    print('\n Não há como entrar na fila, ela está lotada, aguarde para retirar outra senha.')

print('\n', nome.capitalize(), ', sua senha é: \n', senha)
