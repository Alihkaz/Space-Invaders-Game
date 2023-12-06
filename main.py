#imports

from turtle import Screen , Turtle 
from tank import Tank
from rocket import Rocket
from invaders import Invaders
from scoreboard import Scoreboard
import time
from PIL import ImageTk, Image


#-------------------------Setting up classes--------------------------#

screen=Screen()
tank=Tank((0,-220))

rocket=Rocket()
invaders=Invaders()
scoreboard=Scoreboard()

screen.register_shape("inv.gif")
screen.register_shape("space.gif")
tank.shape("space.gif")

#-------------------------Creating the bricks and preparing the setup -----------------------------------------#

#-------------------------Setting up the Screen--------------------------#


screen.setup(width=500,height=500)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Space Invaders")


# img = ImageTk.PhotoImage(Image.open('download3333.jpg'))


# screen.bgpic(img)





#----------------------------starting the game--------------------------------------------------------------------------#

#----------------------------moving paddle and ball module while listening-----------------------#

invaders.create_invaders()


fire_timer=0

def start_fire_timer(): 
  
   global fire_timer
   
   if fire_timer<6:
     rocket.fire_status=False

   if fire_timer>6: 
     rocket.fire_status=True
     fire_timer=0




screen.listen()
screen.onkey(tank.go_right,"Right")
screen.onkey(tank.go_left,"Left")
screen.onkey(start_fire_timer," ")
  


n=0 #counter for invaders

game_is_on=True
while game_is_on:

  n+=1
  
  time.sleep(0.3) #wait some time before executing the next code , we write it to slow down the progress !
  fire_timer+=1
  screen.update()
  invaders.move_invaders()
  

  if n%60==0:
     invaders.move_invaders_downward()

    
  rocket.fire(tank.xcor())

  #if the rocket hits the top , reload the tank!
  if  rocket.ycor()>220 :
      rocket.reload(tank.xcor())


      
  #checking the collision with the invaders and updating the status of the invader and if its destroyed or not.
  # if its hitted , it will be removed and the tank will be reloaded ! 
  for invader in invaders.all_invaders:
    if rocket.distance(invader)<50  :

      rocket.reload(tank.xcor())
      invaders.update(invader)
      scoreboard.increase_score()


  #if the invaders hit the tank , then it's game over ! 
  for invader in invaders.all_invaders:
    if invader.ycor()<-220  :
      
      game_is_on=False




screen.exitonclick()

#----------------------------------------------------------------------------------------------------------------------#

  
  

  













# Notes:
#1) game_is_on=True
# while game_is_on:

#   time.sleep(ball.move_speed)
#   screen.update()
#   ball.move()
#what we are doing with the ball is instead of going straightly towards the position , we will make take steps while going , instead of going in a flash way , and we will stop the screen wrt to its speed , where if its speed is 10 , then we wait 10 seconds then let it move at every step , and we increase the speed but the effect will be the saame ! 



# 2) #if it hits the paddle , let it bounce up !
# if ball.distance(paddle)<25  and ball.ycor()<-160  :
#    ball.bounce_y()
#what we are doing here is that the paddle is at -190 , the height is 25 , so the coordinates of the top of the paddle is 
#165 , and we give a buffer = to 5 , so when its less then 160 and have a distance equal to 25 between paddle and ball , let it bounce ! distance is equal to the top of the paddle to the bottom of it ! 



# 3)fire_timer=0
# def start_fire_timer(): 
   
#    global fire_timer
#    if fire_timer>6:
#      rocket.fire()
#      fire_timer=0
#    if fire_timer<6:
#      pass

# when the game start , the fire counter starts ,
#  and to prevent a consicutive firing ,
#  we will only allow to fire when the timer exceds the 6 seconds ,
#  then we restart the counter to 0 ,
#  if he press the fire button when the time is less then 6 seconds , we dont fire the rocket !