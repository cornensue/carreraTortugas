# Entender un poco cómo funciona PyGame

import pygame, sys

width = 640
height = 480

screen = pygame.display.set_mode((width, height))
screen.fill((66,244,223)) # Rellenar la pantalla con un color en RGB
pygame.display.set_caption("Ciclo básico de PyGame") # Título de la pantalla

pygame.font.init()

gameOver = False
while not gameOver:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         gameOver = True
   
   pygame.display.flip() # Refrescar la pantalla -- Siempre después de manipular el evento

pygame.quit()
sys.exit()