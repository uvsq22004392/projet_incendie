######################################
# Groupe BI 2
# Lenny BACKORY
# Andrew BAYISSA
# Joris ANGAMAN
# Martin DIAMANT
# Amel LASSAL
# Thomas TURPIN
# https://github.com/uvsq22004392/projet_incendie
######################################

import random as rd

def etat_foret(nf):
    proba = nf * 0.1 * 100
    feu = rd.randint(0,100)
    if feu < proba:
        return "feu"
    
def terrain():
    a = rd.randint(0,2)
    if a == 0:
        return "foret"
    if a == 1:
        return "prairie"
    if a == 2:
        return "eau"

cases = [[[terrain()] for i in range(50)] for i in range(50)]

print(cases)
