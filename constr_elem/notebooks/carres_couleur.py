import turtle

NOIR = (0, 0, 0)
GRIS = (200, 200, 200)
BLANC = (255, 255, 255)
BLEU = (0, 0, 255)
ROUGE = (255, 0, 0)

def dessiner_carre(x, y, taille, couleur):
    turtle.hideturtle()
    turtle.speed('fastest')
    turtle.colormode(255)
    turtle.up()
    turtle.goto((x, y))
    turtle.down()
    turtle.color(NOIR, couleur)
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(taille)
        turtle.left(90)
    turtle.end_fill()
