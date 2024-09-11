# TODO: Créer un script permettant le formattage du livre des records des JO.

    # Demander la nationalité de l'athlète
    # Demander le nom de l'athlète
    # Demander la date du record
    # Demander la discipline
    # Demander la catégorie, qui peut être nulle
    # Demander le record


country = input("De quelle nationalité est l'athlète ? (donner les 3 lettres correspondant au pays)\n\t>")
athlete = input("Quel est son nom ?\n\t>")
date = input("Date du record ? (jj/mm/aaaa)\n\t>")
discipline = input("Dans quelle discipline ?\n\t>")
category = input("Dans une catégorie spécifique ?\n\t>")
record = input("Quel est le record ?\n\t>")

print("\nNouveau Record :\n----------------")
if ("no" in category.lower()) or ("non" in category.lower()):
    print(date + " - " + discipline + " : ")
else:
    print(date + " - " + discipline + " - " + category + " :")
print("\t" + athlete + " (" + country + ")" + " - " + record)
    

