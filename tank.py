# what we are doing here is inheriting from the class Turtle ,and giving methods from turtle to paddle class ,and then we called  super().__init__() to give the mthods from turtle to paddle , and we are initializing ,the attributes to paddle after inheriting them from turtle ! 
#position is an attribute as a form of an argument that will be provided when we call the class ! 
#first we create a turtle object , give it shape , color , shapesize , which are the characteristics of that class , then we give methods to the class were once called , they will be applied on the turtle objects 


from turtle import Turtle
class Tank(Turtle) :
  
   def __init__(self,position):
      super().__init__()
      self.shape("square")
      self.color("blue")
      self.shapesize(4,1)
      self.tilt(90)
      self.penup()
      self.goto(position)


   def go_left(self):
       new_x=self.xcor()-70
       self.goto(new_x,self.ycor())

   def go_right(self):
       new_x=self.xcor()+70
       self.goto(new_x,self.ycor())