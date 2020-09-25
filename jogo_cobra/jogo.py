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

    tela.fill((27,27,27)) # cor da tela RGB
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #interrompe pygame
            pygame.quit()
            #fecha o script
            sys.exit()

    pygame.display.update()