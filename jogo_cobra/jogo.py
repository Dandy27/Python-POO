import pygame
import sys
from cobrinha import Cobra

# inicializar o pygame

pygame.init()
TAM_TELA =(300,400)
tela = pygame.display.set_mode(TAM_TELA)
cobra = Cobra()

# Iniciando o jogo 
while True:

    tela.fill((7,0,35)) # cor da tela RGB
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #interrompe pygame
            pygame.quit()
            #fecha o script (janela)
            sys.exit()
        

    #desenha a cobra
    for pos in cobra.corpo:
        pygame.draw.rect(tela, pygame.Color(255,204,0),
                            #esquerda, cima, largura, altura
                            pygame.Rect(pos[0], pos[1], 10, 10))



    # atualiza a tela a cada frame
    pygame.display.update()