
#--------------------------------------------Future improvement----------------------------------------------#

#again , we are inheriting from the turtle class ,
# where we are assigning many attributes related to the turtle class towards Ball class through super().__init__()
# , and here we are creating a new turtle object but with the shape of a missle ! 

from turtle import Turtle




class Rocket(Turtle): #inheriting from the Turtle Class !

  def __init__(self):
    super().__init__()  #assigning attributes from the turtle class to this class  

    self.fire_status=False
    self.y_move = 7
    self.positions=[]
    self.new_y=-220    #to let the rocket go from the top of the tank!
    self.n=-1 

    self.shape("square")  #the characteristics of our rocket !
    self.color("red")
    self.shapesize(1, 0.5)
    self.penup()
    self.hideturtle()
   
    
  

  def fire(self,tankx): 
    if self.fire_status==True:   
      self.showturtle() 
      self.new_y+=self.y_move
      self.positions.append(tankx) 
      self.goto(self.positions[0] , self.new_y) #add the new position of the tank ,
                                                 #and we wil only care about the first positon where the rocket is launched ,
                                                 #and even the tank moved ,
                                                 #  we will care only about the first position where the rocket is launched



  def reload(self,tankx) :
      self.fire_status=False
      self.hideturtle() 
      self.new_y=-220
      self.positions=[] 
      self.goto(tankx , self.new_y)
      self.fire(tankx)
      

       



#when we start the game , and when we press on the space key ,
#  we get the position of the paddle ,
#  and then let the rocket run from it , 
# but to avoid the rocket from following every step of the tank ,
#  we add every step to a list , then we only give the rocket the launch position to go from it !


# To allow multiple creation of the rockets ,
#  we create a rocket when we press space ,
#  then loop throgh them and let them go to a posittion ,
#  and to avoid the situation of every rocket following the other ,
# i separated the rockets from each other by letting the rocket moves to a new x ,
# under the order of the increased n aftyer pressing the space ! so that not all the rockets moves at the same time ,
#  only ones who are created after pressing space !
#In addition to that , to let every rocket takes a new x where the tank launches , 
#i set the positions list to be empty every time i press space ! 

