# TODO: Calculer la distance qu'un poids peut atteindre en utilisant la formule de la portée d'un projectile.
# TODO: Importer les modules nécessaires.

import math
vitesse = input ("Quelle est la vitesse initiale de la balle?(en m/s)\n\t> ")
angle = input ("quel est l'angle de lancement?(en degrés)\n\t> ")
distance = ((float(vitesse)**2)*(math.sin(2*(math.radians(float(angle))))))/9.81
print("La distance maximale en x est :", round(distance,2), "m")
