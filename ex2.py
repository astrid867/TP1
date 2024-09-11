# TODO: Créer un script pour calculer les ressources nécessaires pour assainir la Seine.
# TODO: Importer les modules nécessaires.

eau = input("Quelle quantité d'eau faut-il assainir?")
Filtre = float(eau)*(1/5)
Lampes= float(eau)*(3/5)
Chlore= float(eau)*(0.5/5)
print("Voici les éléments requis pour assiner",eau," L d'eau:")
print("         ","-",Filtre, "filtres")
print("         ","-",Lampes, "lampes UV")
print("         ","-",Chlore, "kg de chlore")
