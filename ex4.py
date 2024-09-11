# TODO: Écrire un programme qui demande le pourcentage de charge actuel de la batterie du bateau,
#        calcule la distance restante en km en fonction de ce pourcentage,
#        et affiche le résultat au format "XX km".
#        Assurez une gestion du pourcentage valide au cours de votre programme (% toujours dans [0 ; 100]).

pourcentage_batterie = input("Quel est le pourcentage de la battrie du bateau?")
if 50 < float(pourcentage_batterie) <= 100:
    distance = (float(pourcentage_batterie) - 50) * 2 + (25*0.5) + (15*1) + (5*2.5)+(5*6)
elif 25 < float(pourcentage_batterie) <= 50:
    distance = (float(pourcentage_batterie) - 25) * 0.5 + (15*1) + (5*2.5)+(5*6)
elif 10 < float(pourcentage_batterie) <= 25:
    distance = (float(pourcentage_batterie) - 10) * 1 + (5*2.5)+(5*6)
elif 5 <  float(pourcentage_batterie) <= 10:
    distance =  (float(pourcentage_batterie) - 5) * 2.5 + (5*6)
elif 0 <=  float(pourcentage_batterie) <= 5:
    distance =  float(pourcentage_batterie) * 6
else :
    print (" La valeur entrée n'est pas valide.") 

print("La distance possible avec",pourcentage_batterie, "%", "batterie est d'environ,",round(distance), "km.")