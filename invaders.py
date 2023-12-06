#

from turtle import Turtle
import time


class Invaders(Turtle): #Inheriting from the Turtle class to give this class additional functions

    def __init__(self):
        super().__init__()      #to create attributes from the inherited class
        self.all_invaders = []  # to put the invader object we created below
        self.first_row=90       #the y nwe want to start from
        self.x=-150             #the x we want to start and to increment from !
        self.color()            #the color attribute we inherited 
        self.x_move = 10
        self.y_move = 14
        self.move_speed=0.1
        
        
       

  
    def create_invaders(self):

      # creating all the bricks and positioning all the breakes !
      
      for n in range(0,24):
            
            invader = Turtle()
            invader.shape("inv.gif")

            invader.color('green')
            invader.tilt(270)
            invader.penup()
            
          # going up every 8 invaders and restarting from the begining of the row ! ! 
            if n%8==0:
              self.first_row+=45
              self.x=-150

            #to remove the starting bug
            invader.goto(self.x,self.first_row)
            
           
            self.x+=65
            self.all_invaders.append(invader)
   






  
 
    def update(self,hitted_invader):

      for invader in self.all_invaders:
        
        if invader==hitted_invader:
            pass
        else:
          hitted_invader.goto(invader.xcor(),invader.ycor())



                       
        #what we are doing here , is depending on the number of the invaders in the list , we are looping,
        #then we are checking each invader in the list , if its coordinate is equal to the coordinates of the hitted invader . then pass it 
        # , if not , take these coordinate 
        # , and let the brick(here we are using the hitted brick since it have turtle char no problem ) 
        # to go to the safe coordinate that we have checked 

        # So when the rocket collides with the invader , the invader will be destroyed ! 
        #what we are doing here is checking if the hitted invader in the invaders list 
        # then we pass it , and update the screen without it !








    def move_invaders(self):
        #moving
        for invader in self.all_invaders :
            new_x = invader.xcor() + self.x_move
            y = invader.ycor()
            invader.goto(new_x, y)
        #bouncing    
        for invader in self.all_invaders :    
           if  invader.xcor()==350 or invader.xcor()==-420 :  
                self.x_move *= -1


    def move_invaders_downward(self):
        for invader in self.all_invaders :
            x = invader.xcor() 
            new_y = invader.ycor() - self.y_move
            invader.goto(x, new_y)
           


       #what we are doing here is first moving every invader in the list of invaders by incremint to its prevoius xcor ,
       #then going to the new xcor after adding to it , and we are adding by an equal way to all of the invaders ,
       #  this will lead to a fair move betweem all of them  . how ever , we want the invaders to bounce left or right when they hit the boundries ,
       #  to do so , when all of them moves , we exit the move loop , then check if any of them is on the right boundries or in the left boundries ,
       #  if so , we multiply the incremnting number by -1 to let them move to the opposite way ,
       #  exiting the moving loop will solve any delay and prevent the bugs and over lapping between invaders 
        





    def reset(self):
        self.goto(0,-180)
        self.move_speed=0.1





