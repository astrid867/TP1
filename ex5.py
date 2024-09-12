#TODO: Analyser la chaîne de caractères saisie et compter le nombre de médailles.
#      Attention si la chaîne est invalide, un message d'erreur est attendu.

# médaille_or= "G"
# médaile_argent= "S"
# médaille_bronze = "B"
pays = input("Pays concerné:\n\t> ")
chaine = input(" la chaîne représentant le résultat du pays:\n\t> ")
nb_argent = nb_bronze = nb_or = 0
erreur = False
for i in range(len(chaine)):
    if "G" == chaine[i]:
        nb_or += 1
    elif "S" == chaine[i]:
        nb_argent += 1
    elif "B" == chaine[i]:
        nb_bronze += 1
    else:
        erreur = True
if not erreur:
    print("\t\t--",nb_or,"or")
    print("\t\t--",nb_argent,"argent")
    print("\t\t--",nb_bronze,"bronze")
else:
    print("Chaine invalide!!!")
