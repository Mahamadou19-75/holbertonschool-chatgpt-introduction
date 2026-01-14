#!/usr/bin/python3
import sys

def factorial(n):
    """
    Description de la fonction :
        Calcule la factorielle d'un entier non négatif en utilisant une approche récursive.

    Paramètres :
        n (int) : L'entier dont on souhaite calculer la factorielle.
                  Doit être un entier supérieur ou égal à 0.

    Retourne :
        int : La valeur de la factorielle du nombre n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Lecture de l'argument en ligne de commande, calcul de la factorielle et affichage
f = factorial(int(sys.argv[1]))
print(f)
