from random import randint
from time import sleep

login = True

while login:
    print('='*20)
    print('Eu sou o computador...')
    sleep(1)
    print('Escolha um número entre 1 a 10')
    sleep(1)
    print('O que você acha?')
    sleep(1)
    print('='*20)
    
    cont = 0
    computer = randint(0, 10)
    
    x = False
    
    while not x:
            player = int(input('Qual número o computador escolheu: '))
    
            cont += 1
    
            if 1 <=  player <= 10:
                x = False
    
                if player == computer and cont == 1:
                    x = True
                    print('Você acertou!')
                    sleep(1)
                    print('E ganhou 10 pontos pelo acerto de primeira tentativa!')
    
                elif player == computer and cont == 2:
                    x = True
                    print('Você acertou!')
                    sleep(1)
                    print('E ganhou 05 pontos pelo acerto de segunda tentativa!')
    
                elif player == computer and cont == 3:
                    x = True
                    print('Você acertou!')
                    sleep(1)
                    print('E ganhou 02 pontos pelo acerto de terceira tentativa!')
    
    
                elif cont == 3:
                    x = True
                    print('Já foram 3 tentativas.')
                    sleep(1)
                    print('Ganhando assim 0 pontos.')
    
    
    
            else:
                print('Você digitou um número fora da faixa permitida, por favor digite novamente!')
                sleep(1)
                x = False
                cont = 0
                
    aux = int(input('Você deseja continuar jogando? (1=Sim/2=Não)'))
    
    if aux == 2:
        print("Que pena, até a proxima")
        login = False


