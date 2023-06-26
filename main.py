from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet",prompt="Which turtle will win the race?. Enter the color: ")
colors = ["red","orange" ,"blue", "yellow", "green", "purple"]

all_turtle_list = []
step = 0
for i in range(6):
  new_turtle = Turtle("turtle")
  new_turtle.color(colors[i])
  new_turtle.penup()
  new_turtle.setpos(x=-240, y= -150+step)
  step += 60
  all_turtle_list.append(new_turtle)

isRaceOn = False
if user_bet:
  isRaceOn = True

while isRaceOn == True:
  for turtle in all_turtle_list:
    if turtle.xcor() >= 240:
      isRaceOn = False
      if user_bet == turtle.pencolor():
        print(f"You've won. The {turtle.pencolor()} color is winning turtle")
      else:
        print(f"You've lost. The {turtle.pencolor()} color is winning turtle")
    rand_distance = random.randint(0,10)
    turtle.forward(rand_distance)
    
  
