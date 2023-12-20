def remplacer_element_par_somme(liste, index):
    if index > 0 and index < len(liste) - 1:
        somme_voisins = liste[index - 1] + liste[index + 1]
        liste[index] = somme_voisins

L = [1, 2, 3, 4, 5]

deuxieme_valeur = L[1]
print(f"Deuxième valeur de la liste : {deuxieme_valeur}")

remplacer_element_par_somme(L, 3)

print("Liste après la modification : ", L)

derniere_valeur = L[-1]
print(f"Dernière valeur de la liste : {derniere_valeur}")
