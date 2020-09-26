import pygame
import sys
import random
from time import sleep
from cobrinha import Cobra
from comida import Comida

#iniciar fonte 
pygame.font.init()
minha_fonte = pygame.font.SysFont('Comic Sans MS', 20)

# inicializar o pygame

pygame.init()
TAM_TELA =(300,400)
tela = pygame.display.set_mode(TAM_TELA)
tempo = pygame.time.Clock() # cronometro | tempo 
pontuacao = 0
cobra = Cobra()
comida = Comida()
posicao_comida = comida.posicao
# Iniciando o jogo 
while True:

    tela.fill((7,0,35)) # cor da tela RGB
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #interrompe pygame
            pygame.quit()
            #fecha o script (janela)
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                cobra.muda_direcao('DIREITA')
            if event.key == pygame.K_UP:
                cobra.muda_direcao('CIMA')
            if event.key == pygame.K_DOWN:
                cobra.muda_direcao('BAIXO')
            if event.key == pygame.K_LEFT:
                cobra.muda_direcao('ESQUERDA')

    posicao_comida = comida.gera_nova_comida()
    # se a cobra comer a comida
    if cobra.move(posicao_comida):
        comida.devorada = True
        pontuacao += 1

    if cobra.verifica_colisao():
        voce_perdeu = minha_fonte.render('SE FUDEU!', True, (255, 255, 255))
        tela.blit(voce_perdeu, (80,180))
        pygame.display.flip()
        sleep(2)
        pygame.quit()
        sys.exit()

    # texto da pontuação 
    pontos = minha_fonte.render(f'Pontuação: {pontuacao}', True, (255, 255 ,255))
    tela.blit(pontos, (10,10))
    #desenha a cobra
    for pos in cobra.corpo:
        pygame.draw.rect(tela, pygame.Color(255,204,0), # -> cor da cobra (amarela)
                            #esquerda, cima, largura, altura
                            pygame.Rect(pos[0], pos[1], 10, 10))

    #desenha comida
    pygame.draw.rect(tela, pygame.Color(255,0,0),# -> cor da comida
                           pygame.Rect(posicao_comida[0], posicao_comida[1], 10, 10))  



    # atualiza a tela a cada frame
    pygame.display.update()


    # Frames por segundo 
    tempo.tick(22)
