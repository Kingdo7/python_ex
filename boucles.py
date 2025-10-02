#Exercice

#Écrivez un programme qui affiche les 20 premiers termes de la table de multiplication par 7, en signalant au passage 
#(à l'aide d'une astérisque) ceux qui sont des multiples de 3.
#Exemple : 7 14 21 * 28 35 42 * 49 56 63 * 70 77 84 * 91 98 105 * 112 119 126 * 133 140

nb = 0

while nb <= 7*20:
    if nb % 7 == 0:
        if nb % 3 == 0:
            print(str(nb) + " *")
        else:
            print(nb)
    nb += 1