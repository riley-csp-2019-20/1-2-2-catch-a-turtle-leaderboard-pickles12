# a121_catch_a_turtle.py
  
#-----import statements-----
import turtle as trtl
import random    
import leaderboard as lb
#leaderboard variables
leaderboard_file_name = "a112_leaderboard.txt"
leader_names_list = []
leader_scores_list = []
user_name = input("What is your name?")
#-----game configuration----
shape = "arrow"
size =  random.randint(1, 30)
color = "purple"
score = 0
font_setup = ("Arial", 20, "normal")
timer = 5
counter_interval = 1000   #1000 represents 1 second


timer_up = False
shapelist = ["square", "triangle", "classic", "turtle", "circle"]
#-----initialize turtle-----
joe = trtl.Turtle()
momma = trtl.Turtle(shape = shape)
joe.color(color)
joe.shapesize(size) 
joe.speed(0)
momma.color("black")
momma.ht()
momma.penup()
momma.goto(-370,270)
momma.speed(0)
counter =  trtl.Turtle()
counter.ht()
counter.penup()
counter.goto(350,300)
#-----game functions--------        DE  VR  TB cvx
def turtle_clicked(x,y):
    global joe
    print("joe was clicked")
    change_position()
    score_counter()
    changesize()
    changeturtle()

def change_position():
    joe.penup()
    joe.ht()
    new_xpos = random.randint(-400,400)
    new_ypos = random.randint(-300,300)
    joe.goto(new_xpos, new_ypos)
    joe.st()
def score_counter():
    global score
    score += 1
    print(score)
    momma.clear()
    momma.write(score, font=("Ariel", 80, "normal"))
def countdown():
  global timer, timer_up
  counter.clear()                       
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    joe.ht()
    joe.goto(1000,100)
    timer_up = True
    manage_leaderboard()    
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 
def changesize():
  size = random.randint(1, 30)
  joe.shapesize(size) 
def changeturtle():
  global shapelist
  shape = random.choice(shapelist)
  joe.shape(random.choice(shapelist))

# manages the leaderboard for top 5 scorers
def manage_leaderboard():
  
  global leader_scores_list
  global leader_names_list
  global score
  global joe

  # load all the leaderboard records into the lists
  lb.load_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list)

  # TODO
  if (len(leader_scores_list) < 5 or score > leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, user_name, score)
    lb.draw_leaderboard(leader_names_list, leader_scores_list, True, joe, score)

  else:
    lb.draw_leaderboard(leader_names_list, leader_scores_list, False, joe, score)

#-----events-------------
joe.onclick(turtle_clicked)
wn = trtl.Screen()
wn.bgcolor("green")
wn.ontimer(countdown, counter_interval) 
wn.mainloop()