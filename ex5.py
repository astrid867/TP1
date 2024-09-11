#TODO: Analyser la chaîne de caractères saisie et compter le nombre de médailles.
#      Attention si la chaîne est invalide, un message d'erreur est attendu.

médaille_or= "G"
médaile_argent= "S"
médaille_bronze = "B"
pays = input("Pays concerné:")
chaine = input(" la chaîne représentant le résultat du pays:")
nb_or = chaine.count ("G")
nb_argent = chaine.count("S")
nb_bronze = chaine. count("B")
print("le nombre de médaille d'or est",nb_or)
print("le nombre de médaille d'agent est",nb_argent)
print("le nombre de médaille de bronze est",nb_bronze)
