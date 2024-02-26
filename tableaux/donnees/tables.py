import pygame

def affichage_table(T):
	
	# Paramètres de la fenêtre graphique
	taille_case = 50
	hauteur_fenetre = len(T) * taille_case
	largeur_fenetre = len(T[0]) * taille_case
	
	# Ouverture de la fenêtre graphique
	pygame.init()
	fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
	
	#Creation d'une police de caracteres
	pygame.font.init()
	police = pygame.font.SysFont('Courier New', 24)
	
	# Affichage d'un fond blanc
	fenetre.fill((255, 255, 255))
	
	if T[0][0] in ['+', '*']:
		pygame.draw.rect(fenetre, (150, 150, 150), (0, 0, largeur_fenetre, taille_case))
		pygame.draw.rect(fenetre, (150, 150, 150), (0, 0, taille_case, hauteur_fenetre))
	
	for l in range(len(T)):
		for c in range(len(T[l])):
			texte = police.render(str(T[l][c]), True, (0, 0, 0))
			fenetre.blit(texte, ((c+0.5)*taille_case - texte.get_width()//2, (l+0.5)*taille_case - texte.get_height()//2))
	pygame.display.flip()
	#pygame.image.save(fenetre, 'table.png')
