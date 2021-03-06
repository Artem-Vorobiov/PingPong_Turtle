# 	Turtle Graphics Game

import turtle 
import time 
import math
import random
import os

# Set up the Screen
def screen_here():
	global wn
	global score_1
	global score_2
	global pen

	pen = turtle.Turtle()
	pen.hideturtle()
	score_1 = 0
	score_2 = 0

	wn = turtle.Screen()
	wn.setup(width=0.7, height = 0.7)
	wn.bgcolor('lightgreen')
	wn.tracer(3)  
# 	print(wn.window_height())
# 	print(type(wn.window_height()))
# 	print(wn.window_width())
# 	print(type(wn.window_width()))
	# print(wn.screensize()[0])
	# print(type(wn.screensize()[0]))


# Main object
class Player(turtle.Turtle):
	def __init__(self, spriteshape, color, startx, starty):
		turtle.Turtle.__init__(self, shape = spriteshape)
		self.shapesize(stretch_wid = 6, stretch_len = 1.5 , outline = None)
		self.color(color)
		self.penup()
		self.goto(startx, starty)
		self.speed(0)
		# self.fd(0)
		# self.speed = 1

	def hop_up(self):
		self.sety(self.ycor()+40)

	def hop_down(self):
		self.sety(self.ycor()-40)

class Target(turtle.Turtle):
	def __init__(self, spriteshape, color, startx, starty):
		turtle.Turtle.__init__(self, shape = spriteshape)
		self.shapesize(stretch_wid = 1, stretch_len = 1 , outline = None)
		self.color(color)
		self.penup()
		self.goto(startx, starty)
		self.speed(0)
		head = [random.randint(0, 45), random.randint(135, 180), random.randint(180, 225), random.randint(315, 360)]
		self.setheading(random.choice(head))
		self.status = 'ready'

	def move(self):
		self.fd(6)




def boundary_checking(ship):
	global score_1
	global score_2

	if ship.ycor() > wn.screensize()[1] - 10:
		if ship.heading() > 90:
			ship.right(180 + 2*abs(90 - ship.heading()))
		else:
			ship.right(180 - 2*abs(90 - ship.heading()))

	elif ship.ycor() < - wn.screensize()[1] + 10:
		if ship.heading() > 90:
			ship.right(180 + 2*abs(90 - ship.heading()))
		else:
			ship.right(180 - 2*abs(90 - ship.heading()))

	if ship.xcor() > wn.screensize()[0] + 100:
		ship.goto(0,0)
		time.sleep(2)

		head = [random.randint(0, 45), random.randint(135, 180), random.randint(180, 225), random.randint(315, 360)]
		ship.setheading(random.choice(head))

		score_2 += 100
		show_up_score(score_1, score_2)

	if ship.xcor() < - wn.screensize()[0]-100:
		ship.goto(0,0)
		time.sleep(1)

		head = [random.randint(0, 45), random.randint(135, 180), random.randint(180, 225), random.randint(315, 360)]
		ship.setheading(random.choice(head))

		score_1 += 100
		show_up_score(score_1, score_2)


def if_collision(pl1, pl2, ball):
	dis_1 = pl1.distance(ball.xcor(), ball.ycor())
	dis_2 = pl2.distance(ball.xcor(), ball.ycor())
	print('\n\t\t DISTANCE = ' ,dis_1)

	if dis_1 <= 30.0 and ball.status == 'ready':
		ball.status = 'reflected'
		if ball.heading() >= 90:
			ball.right(180 + 2*abs(180 - ball.heading()))
		else:
			ball.right(180 - 2*abs(180 - ball.heading()))
		ball.color('black')

	if dis_2 <= 30.0 and ball.status == 'ready':
		ball.status = 'reflected'

		if ball.heading() >= 90:
			ball.right(180 + 2*abs(180 - ball.heading()))
		else:
			ball.right(180 - 2*abs(180 - ball.heading()))
		ball.color('yellow')

	if dis_1 > 100.0:
		ball.status = 'ready'


def show_up_score(score_1, score_2):
	pen.undo()
	pen.hideturtle()
	pen.penup()
	msg = 'Player 1: %s VS Player 2: %s' %(score_1,score_2)
	# pen.goto(-(wn.screensize()[0])/2,(wn.screensize()[1])-20)
	pen.goto(-wn.window_width()/2+10, wn.window_height()/2.2)
	pen.write(msg, font=("Arial", 20, "normal"))




screen_here()
player_1  = Player('square', 'white', -450, 0)
player_2  = Player('square', 'white', 450, 0)
ball      = Target('circle', 'red', 0, 0)



turtle.listen()
turtle.onkey(player_1.hop_up, 'Up')
turtle.onkey(player_1.hop_down, 'Down')
turtle.onkey(player_2.hop_up, 'w')
turtle.onkey(player_2.hop_down, 's')

while True:
	turtle.update()
	time.sleep(0.02)
	ball.move()
	boundary_checking(ball)
	if_collision(player_1, player_2, ball)
	# print(ball.status)

time.sleep(5)