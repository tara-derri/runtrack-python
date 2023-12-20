def distance_to_toilettes(nombre_marches, hauteur_marche):
    distance_par_marche = hauteur_marche * 2 / 100
    distance_totale = nombre_marches * distance_par_marche * 2 * 5 * 7
    
    print(f'Pour {nombre_marches} marches de {hauteur_marche} cm, le gardien parcourt {distance_totale:.2f} m par semaine.')

nombre_marches = 10
hauteur_marche = 20
distance_to_toilettes(nombre_marches, hauteur_marche)
