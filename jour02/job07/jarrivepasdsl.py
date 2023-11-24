chaine = "abcdefghijklmnopqrstuvwxyz" * 10

nombre_lignes = 26

compteur = 0

for i in range(2, nombre_lignes + 2):
    caracteres = chaine[compteur:compteur + i]
    print(caracteres, end="\033[K\n" if i != nombre_lignes + 1 else "")
    compteur += i

