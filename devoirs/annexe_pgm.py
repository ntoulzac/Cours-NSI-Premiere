try:
    from PIL import Image
except ModuleNotFoundError:
    raise ModuleNotFoundError("Installer le module PIL !")

dico = {"pbm": {"tete": "P1", "max": 1, "code": lambda r, g, b: f"{round((0.2126*r+0.7152*g+0.0722*b)/255)} "},
        "pgm": {"tete": "P2", "max": 255, "code": lambda r, g, b: f"{round(0.2126*r+0.7152*g+0.0722*b)} "},
        "ppm": {"tete": "P3", "max": 255, "code": lambda r, g, b: f"{r} {g} {b} "}}

def extraire_pixels(nom_fichier):
    """
    Renvoie le tableau de pixels contenu dans un fichier image au format PGM.
    - Entrée : nom_fichier (chaine, nom d'un fichier image au format PGM)
    - Sortie : tab_pixels (tableau à deux dimensions)
    """
    extension = nom_fichier.split(".")[1]
    with open(nom_fichier, "r", encoding="utf-8") as fichier:
        chaine = fichier.read()
    chaine_liste = chaine.split("\n")
    code_extension = chaine_liste[0]
    assert code_extension == dico[extension]["tete"], "Problème de fichier PGM"
    largeur, hauteur = chaine_liste[1].split(" ")
    largeur = int(largeur)
    hauteur = int(hauteur)
    tab_pixels = []
    for L in range(hauteur):
        if extension == "pgm":
            liste = chaine_liste[L+3].split(" ")[:largeur]
            ligne = [int(x) for x in liste]
        elif extension == "pbm":
            liste = chaine_liste[L+3].split(" ")[:largeur]
            ligne = [int(x) for x in liste]
        else:
            liste = chaine_liste[L+3].split(" ")[:3*largeur]
            ligne = []
            for n in range(largeur):
                ligne.append((int(liste[3*n]), int(liste[3*n+1]), int(liste[3*n+2])))
        tab_pixels.append(ligne)
    return tab_pixels

def afficher(nom_fichier):
    """
    Affiche dans le carnet une image au format PGM.
    - Entrée : nom_fichier (chaine, nom d'un fichier image au format PGM)
    Effet de bord : ouverture de l'image dans une fenêtre
    """
    extension = nom_fichier.split(".")[1]
    tab_pixels = extraire_pixels(nom_fichier)
    largeur, hauteur = len(tab_pixels[0]), len(tab_pixels)
    image = Image.new('RGB', (largeur, hauteur))
    for C in range(largeur):
        for L in range(hauteur):
            if extension == "pgm":
                r = tab_pixels[L][C]
                g, b = r, r
            elif extension == "pbm":
                r = 255*tab_pixels[L][C]
                g, b = r, r
            else:
                r, g, b = tab_pixels[L][C]
            image.putpixel((C, L), (r, g, b))
    return image

def creer_image(tab_pixels, nom_fichier):
    """
    Crée un fichier image au format PNM à partir d'un tableau de pixels.
    - Entrée : tab_pixels (tableau à deux dimensions),
               nom_fichier (chaine, nom d'un fichier image au format PGM)
    Effet de bord : écriture dans un fichier PGM
    """
    extension_cible = nom_fichier.split(".")[1]
    largeur, hauteur = len(tab_pixels[0]), len(tab_pixels)
    chaine_pnm = f"""{dico[extension_cible]["tete"]}\n{largeur} {hauteur}\n{dico[extension_cible]["max"]}"""
    for L in range(hauteur):
        chaine_pnm += "\n"
        for C in range(largeur):
            if extension_cible in ["pbm", "pgm"]:
                chaine_pnm += f"{tab_pixels[L][C]} "
            else:
                R, V, B = tab_pixels[L][C]
                chaine_pnm += f"{R} {V} {B} "
    with open(nom_fichier.split(".")[0] + "." + extension_cible, "w", encoding="utf-8") as fichier:
        fichier.write(chaine_pnm)