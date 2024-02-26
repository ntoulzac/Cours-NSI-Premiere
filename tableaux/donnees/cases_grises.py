import pygame
#from pygame.locals import *

nb_cases = 20
taille_case = 40

def ouverture_fenetre():
	# Paramètres de la fenêtre graphique
	hauteur_fenetre = taille_case
	largeur_fenetre = nb_cases * taille_case
	# Ouverture de la fenêtre graphique
	pygame.init()
	fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
	# Affichage d'un fond blanc
	fenetre.fill((255, 255, 255))
	pygame.display.flip()
	return fenetre

def affichage_cases(fenetre, L):
	if type(L) != list:
		raise TypeError('le paramètre doit être un tableau')
	for k in range(len(L)):
		if type(L[k]) != int:
			raise TypeError('les éléments du tableau doivent être des entiers')
		if L[k] not in range(256):
			raise ValueError('les éléments du tableau doivent être compris entre 0 et 255')
		pygame.draw.rect(fenetre, (L[k], L[k], L[k]), (k*taille_case, 0, taille_case, taille_case))
	pygame.display.flip()
