from turtle import speed, up, down, forward, left, right, goto, color, pensize, Screen, dot, hideturtle

def pas(angle):
	left(angle)
	forward(40)
	right(angle)
	dot(16)

def haut():
	pas(90)

def bas():
	pas(-90)
	
def droite():
	pas(0)
	
def gauche():
	pas(180)

def demarrer_labyrinthe():
	fenetre = Screen()
	fenetre.setup(600, 600)
	fenetre.bgpic('Images/laby.png')

	up()
	goto(-238, -2)
	down()

	pensize(3)
	color('red')
	speed('fast')
	hideturtle()
	droite()
