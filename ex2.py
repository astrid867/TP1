# TODO: Créer un script pour calculer les ressources nécessaires pour assainir la Seine.
# TODO: Importer les modules nécessaires.

eau = input("Quelle quantité d'eau faut-il assainir?\n\t>")
Filtre = float(eau)*(1/5)
Lampes= float(eau)*(3/5)
Chlore= float(eau)*(0.5/5)
print("Voici les éléments requis pour assainir",eau,"L d'eau:")
print("\t-",Filtre, "filtres")
print("\t-",Lampes, "lampes UV")
print("\t-",Chlore, "kg de chlore")
