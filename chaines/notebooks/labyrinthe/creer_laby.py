from turtle import speed, up, down, forward, left, right, goto, Screen, color, pensize, getcanvas
from time import sleep
from tkinter import Tk, Canvas
import pyscreenshot as ImageGrab

def enregistrer_fenetre_Tk(window, canvas, nom_de_fichier):
	x = canvas.winfo_rootx() #+window.winfo_rootx()
	y = canvas.winfo_rooty() #+window.winfo_rooty()
	x2 = x + canvas.winfo_width()
	y2 = y + canvas.winfo_height()
	image = ImageGrab.grab(bbox = (x, y, x2, y2))
	image.save(nom_de_fichier)

def pas(angle):
	left(angle)
	forward(avancee)
	right(angle)

def haut():
	pas(90)

def bas():
	pas(-90)
	
def droite():
	pas(0)
	
def gauche():
	pas(180)
	
def dessiner_laby(phrase):
	phrase = ascii(phrase)
	for car in phrase:
		if car == 'h':
			haut()
		elif car == 'b':
			bas()
		elif car == 'g':
			gauche()
		elif car == 'd':
			droite()

fenetre = Screen()
fenetre.setup(600, 600)

avancee = 40
speed('fastest')
up()
goto(-220, -220)
down()

pensize(3)
phrase = 'hhhhhdgbbdhdhhgdbdgbgbgbbbddhbddhhdhbgbbdddhbdddhbdhhggddhhhgbbghhgdbbggdbbd'
dessiner_laby(phrase)
up()
goto(-220,220)
down()
phrase = 'bbbbbhdddbdghhdgbggghhhhdbbhddgghdddddbggbggbgdhdddbbgdddhghbddhbdbhggbgbgbgbgdbggbgbhddbhghddhhdbdbbdgbgdhhhghhdhghhghddhdddbggbhddhddbbghbgdbhdbbbghbgghbgbgdbd'
dessiner_laby(phrase)
up()
goto(500,500)

enregistrer_fenetre_Tk(fenetre,  getcanvas(), 'laby.png')
