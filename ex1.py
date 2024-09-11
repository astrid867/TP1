# TODO: Cr�er un script permettant le formattage du livre des records des JO.

    # Demander la nationalit� de l'athl�te
    # Demander le nom de l'athl�te
    # Demander la date du record
    # Demander la discipline
    # Demander la cat�gorie, qui peut �tre nulle
    # Demander le record


country = input("De quelle nationalit� est l'athl�te ? (donner les 3 lettres correspondant au pays)\n\t>")
athlete = input("Quel est son nom ?\n\t>")
date = input("Date du record ? (jj/mm/aaaa)\n\t>")
discipline = input("Dans quelle discipline ?\n\t>")
category = input("Dans une catégorie spcifique ?\n\t>")
record = input("Quel est le record ?\n\t>")

print("\nNouveau Record :\n----------------")
if ("no" in category.lower()) or ("non" in category.lower()):
    print(date + " - " + discipline + " : ")
else:
    print(date + " - " + discipline + " - " + category + " :")
print("\t" + athlete + " (" + country + ")" + " - " + record + "\n\n")
    

