def nom_departement(num):
    """
    Renvoie le nom du département d'Île-de-France dont le numéro est num
    - Entrée : num (entier égal à 75, 77, 78, 91, 92, 93, 94 ou 95)
    -- Assertion : ERREUR si num n'est pas un numéro de département d'IdF
    - Sortie : une chaîne de caractères
    """
    assert (75 <= num <= 78 and num != 76) or (91 <= num <= 95), 'Département hors Île-de-France !'
    dep = {75 : 'Paris', 77 : 'Seine et Marne', 78 : 'Yvelines', 91 : 'Essonne', 92 : 'Hauts de Seine',
          93: 'Seine Saint Denis', 94 : 'Val-de-Marne', 95 : 'Val d\'Oise'}
    return dep[num]

def prefecture(num):
    """
    Renvoie le chef-lieu du département d'Île-de-France dont le numéro est num
    - Entrée : num (entier égal à 75, 77, 78, 91, 92, 93, 94 ou 95)
    -- Assertion : ERREUR si num n'est pas un numéro de département d'IdF
    - Sortie : une chaîne de caractères
    """
    assert (75 <= num <= 78 and num != 76) or (91 <= num <= 95), 'Département hors Île-de-France !'
    pref = {75 : 'Paris', 77 : 'Melun', 78 : 'Versailles', 91 : 'Evry', 92 : 'Nanterre',
          93: 'Bobigny', 94 : 'Créteil', 95 : 'Pontoise'}
    return pref[num]
