# https://python.developpez.com/exercices
##############
# Exercice 1 #
##############
"""
Écrivez un programme qui affiche les 20 premiers termes de la table de multiplication par 7, en signalant au passage 
(à l'aide d'une astérisque) ceux qui sont des multiples de 3.
Exemple : 7 14 21 * 28 35 42 * 49 56 63 * 70 77 84 * 91 98 105 * 112 119 126 * 133 140
"""

print("-----Ex 1-----")
nb = 0

while nb <= 7*20:
    if nb % 7 == 0:
        if nb % 3 == 0:
            print(str(nb) + " *")
        else:
            print(nb)
    nb += 1

##############
# Exercice 2 #
##############

"""
Écrivez un programme qui affiche une table de conversion de sommes d'argent exprimées en euros, en dollars canadiens. La progression des sommes de la table sera « géométrique », comme dans l'exemple ci-dessous :
1 euro(s) = 1.65 dollar(s)
2 euro(s) = 3.30 dollar(s)
4 euro(s) = 6.60 dollar(s)
8 euro(s) = 13.20 dollar(s)
etc. (S'arrêter à 16384 euros)
"""
print("-----Ex 2-----")
euro = 1
taux = 1.65

while euro <= 16384:
    dollar = taux * euro
    print(str(euro) + " euro(s) = " + str(dollar) + " dollar(s)")
    euro *= 2

##############
# Exercice 3 #
##############

"""
Exercice

Écrivez un programme qui affiche une suite de 12 nombres dont chaque terme est égal au triple du terme précédent.
"""
print("-----Ex 3-----")
i = 0
triple = 1

while i <= 12:
    triple = triple *3
    print(triple)
    i += 1