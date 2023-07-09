import pygame
from time import sleep
from random import randint

VERT = (0, 255, 0)
ROUGE = (255, 0, 0)
JAUNE = (255, 255, 0)
NOIR = (0, 0, 0)
BLANC = (255, 255, 255)

def illustration_dichotomie(tab, v):

	def afficher():
		for k in range(len(tab)): 
			pygame.draw.rect(fenetre, couleur[k], (k*taille_case, 0, (k+1)*taille_case, taille_case))
			texte = police.render(str(tab[k]), True, NOIR if couleur[k] != NOIR else BLANC)
			fenetre.blit(texte, ((k+0.5)*taille_case - texte.get_width()//2, 0.5*taille_case - texte.get_height()//2))
		pygame.display.flip()

	def clignoter(pos):
		for _ in range(4):
			couleur[pos] = BLANC
			afficher()
			sleep(0.25)
			couleur[pos] = NOIR
			afficher()
			sleep(0.25)

	# Paramètres et ouverture de la fenêtre graphique
	taille_case = 25
	largeur_fenetre = len(tab) * taille_case
	pygame.init()
	fenetre = pygame.display.set_mode((largeur_fenetre, taille_case))
	pygame.font.init()
	police = pygame.font.SysFont('Courier New', 12)

	# Recherche dichotomique
	trouve = False
	g = 0
	d = len(tab) - 1
	while g <= d and not trouve:
		couleur = [ROUGE for _ in range(g)] + [VERT for _ in range(g, d+1)] + [ROUGE for _ in range(d+1, len(tab))]
		afficher()
		sleep(1)
		m = (g + d) // 2
		couleur[m] = JAUNE
		afficher()
		sleep(1)
		if tab[m] < v:
			g = m+1
		elif tab[m] > v:
			d = m-1
		else:
			clignoter(m)
			trouve = True
	if not trouve:
		couleur = [ROUGE for _ in range(len(tab))]
		afficher()	
	sleep(1)
	pygame.quit()
