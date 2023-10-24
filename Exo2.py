
print("Bonjour, et bienvenue dans mon nouveau programme")
Prenom = input("Quel est votre prénom ? ")
Nom = input("Quel est votre nom de famille ? ")
Nom_En_Majuscule = Nom.upper()
Age = input("Quel âge avez vous ? ")
Taille = input("Combien mesurer vous ? ")
Fruits = input("Dite moi vos fruit préféré ! ")
Liste_Fruits = Fruits.split()
Nom_Produit = input("Entrer le nom d'un produit : ")
Prix_Produit = input("Quel est son prix ? ")
Description_Produit = input("Ajouter une description a votre produit ! ")

  
print("Voilà un récap de vos info !")
print("Vous vous appeler",Prenom, Nom_En_Majuscule, "Vous avez",Age,"ans, vous faite", Taille, "centimètre et vos fruit préféré sont les suivants : ", Liste_Fruits)
print("Voici le recap de voitre produit !")
print("Le nom de votre produit :", Nom_Produit, "il coute",Prix_Produit,"euros, et voici sa description : ", Description_Produit)
