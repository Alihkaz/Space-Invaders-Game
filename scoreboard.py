
# what we are doing here is drawing a score board using the turtle , the color of numbers is white ,the font is courier, then we hide who draw and keep only the drawing , then we make a function called update score , what that will make is get a variable called score  after increasing it through another function which keep it updated by saving the previous score and then increasing to it , and then write it in the drawing that the turtle have maded  

# the highest score is the present score , at the begining , it will be 0 , but in the second time , and after saving the first high score , if the second end score is bigger then the saved high score , the second high score will be the new highest score . . 


from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")



class Scoreboard(Turtle):

    def __init__(self):
      
        super().__init__()
      
        self.score = 0
      
        with open("data.txt") as data:
            self.high_score = int(data.read())

      #Creating the turtle that will write the score ! 
        self.color("white")
        self.penup()
        self.goto(0, 240)
        self.hideturtle()
        self.update_scoreboard()




#Updating the live score every time we increase the score !
  
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}",
                   align=ALIGNMENT,
                   font=FONT)

  
#updating the new highscore when the game is over ! 
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
          
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
              
        self.score = 0
        self.update_scoreboard()


#increasing the saved score by 1 each time we hit an invader
    def increase_score(self):
      
    
      self.score += 1   
      self.update_scoreboard()

      
     