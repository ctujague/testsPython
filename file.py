

try:
    my_file = open("test.txt")
    #lignes= my_file.readlines()
    compteur=1
    ligne=my_file.readline()
    print("type " + str(type(ligne)))
    print("longueur " + str(len(ligne)))
    #for ligne in lignes:
    while ligne:
        print("Passage numero :" + str(compteur))
        print("Ligne -" + ligne)
        print("longueur " + str(len(ligne)))
        if ligne != "":
            print(ligne)
            my_tab = ligne.split()
            print("element 0 = " + my_tab[0])
        compteur=compteur+1
        ligne=my_file.readline()

except IndexError as my_erreur:
    print("Erreur : " + my_erreur.__str__())
finally:
    my_file.close()
