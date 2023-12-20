def my_sort(liste):
    n = len(liste)
    coups = 0
    
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            coups += 1
            
            if liste[j] > liste[j + 1]:
                liste[j], liste[j + 1] = liste[j + 1], liste[j]

    print("Nombre total de coups nécessaires :", coups)

    return liste

ma_liste = [64, 34, 25, 12, 22, 11, 90]
liste_triee = my_sort(ma_liste.copy())
print("Liste triée :", liste_triee)
