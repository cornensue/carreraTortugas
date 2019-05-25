# ==============================================================================================================
# Carrera de torturas con la librería PyGame
# Proyecto que muestra cómo utilizar la libreria PyGame para crear juegos en 2D
# Tendremos una clase: Game que tendrá 2 propiedades: corredores (array) y pantalla y un método: competir()
# ==============================================================================================================
import pygame 

class Game():
   corredores = []

   def __init__(self):
      self.__screen = pygame.display.set_mode((640, 480)) #Crear la pantalla y fijar su tamaño
      pygame.display.set_caption("Carrera de bichos")
      self.background = pygame.image.load("images/background.png")

      self.runner = pygame.image.load("images/smallball.png")
   
   def competir(self):

      x = 0
      hayGanador = False

      while True:
         # Coprobacion de los eventos
         for event in pygame.event.get():
            if event.type == pygame.QUIT:
               pygame.quit()
               sys.exit()

         # Refrescar / renderizar la pantalla
         self.__screen.blit(self.background, (0,0))
         self.__screen.blit(self.runner, (x, 240))
         pygame.display.flip()
         x += 3
         if x >= 250:
            hayGanador = True
         
      pygame.quit()
      sys.exit()


if __name__ == "__main__":
   pygame.init()
   game = Game()
   game.competir()

