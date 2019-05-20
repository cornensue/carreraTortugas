# ==============================================================================================================
# Carrera de torturas con la clase Turtle()
# Proyecto que muestra cómo utilizar objecto de tipo Turtle
# Tendremos una clase: Circuito que tendrá 2 propiedades: corredores (array) y pantalla y un método: competir()
# ==============================================================================================================

# Importamos turtle
import turtle

class Circuito():
   corredores = []
   __posStartY = (-30, -10, 1, 30)
   __colorTurtle = ('red', 'blue', 'green', 'orange')

   def __init__(self, width, height):
      self.__screen = turtle.Screen()    # Dejamos que screen sea privado, además usa el método screen de turtle
      self.__screen.setup(width, height)
      self.__screen.bgcolor('lightgray')
      self.__startLine = -width/2 + 20
      self.__finishLine = width/2 -20

      self.__createRunners()

   def __createRunners(self):
      for i in range(4):
         new_turtle = turtle.Turtle()
         new_turtle.color(self.__colorTurtle[i])
         new_turtle.shape('turtle')
         new_turtle.penup()
         new_turtle.setpos(self.__startLine, self.__posStartY[i])

         self.corredores.append(new_turtle)

   
# mirar desde donde se ejecuta
if __name__ == '__main__':
   circuito = Circuito(640, 480)

print(circuito)



