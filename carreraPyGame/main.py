# ==============================================================================================================
# Carrera de torturas con la librería PyGame
# Proyecto que muestra cómo utilizar la libreria PyGame para crear juegos en 2D
# Tendremos una clase: Game que tendrá 2 propiedades: corredores (array) y pantalla y un método: competir()
# ==============================================================================================================
import pygame 

class Game():
   corredores = []

   def __init__(self):
      self.__screen = pygame.display.set_mode(640, 480) #Crear la pantalla y fijar su tamaño
      pygame.display.set_caption("Carrera de bichos")
      self.background = pygame.image.load("images/background.png")

if __name__ == "__main__":
   pygame.init()
   game = Game()

print(game)
