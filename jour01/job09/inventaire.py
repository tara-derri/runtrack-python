nom_produit = "Television"
prix_unitaire = 680.0
quantite_en_stock = 50


print("Informations sur le produit :")
print("Nom du produit :", nom_produit)
print("Prix unitaire :", prix_unitaire)
print("Quantité en stock :", quantite_en_stock)


quantite_acheter = int(input("Entrez la quantité de produits que vous souhaitez acheter : "))
quantite_en_stock_apres_achat = quantite_en_stock - quantite_acheter


prix_unitaire *= 1.10  

print("\nInformations sur le produit après la mise à jour :")
print("Nom du produit :", nom_produit)
print("Nouveau prix unitaire :", prix_unitaire)
print("Nouvelle quantité en stock :", quantite_en_stock_apres_achat)

