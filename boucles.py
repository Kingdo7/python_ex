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

##############
# Exercice 4 #
##############

"""
Exercice

En utilisant une boucle while, entrez un prix HT (entrez « 0 » pour terminer) et affichez sa valeur TTC.
"""
print("-----Ex 4-----")
"""
HT = 10

while HT != 0:
    HT = float(input("Entrer un prix hors taxes (0 pour arrêter) : "))
    TTC = HT * 1.2
    if(HT == 0):
        break
    print(f"Le prix TTC de {HT:.2f}€ est {TTC:.2f}€")
"""
##############
# Exercice 5 #
##############
print("-----Ex 5-----")

"""
Exercice

Calculez la somme d'une suite de nombres positifs ou nuls. 
Comptez combien il y avait de données et combien étaient supérieures à 100.
Entrer un nombre inférieur ou égal à 0 indique la fin de la suite.
"""

ex5 = int(input("Entrer un nombre : (0 ou moins pour arrêter) : "))
ex5_somme = 0
ex5_total = 0
plus100 = 0


while ex5 > 0:
    if ex5 <= 0:
        break

    if ex5 > 100:
        plus100 += 1
    
    ex5_somme += ex5
    ex5_total += 1
    ex5 = int(input("Entrer un nombre : (0 ou moins pour arrêter) : "))

print(f"Il y a {ex5_total} nombre(s) au total, dont {plus100} sont supérieur a 100, le total est égal a {ex5_somme}")

