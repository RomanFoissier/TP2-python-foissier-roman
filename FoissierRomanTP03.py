print("")
print("1.Listes")
print("1.1 Modifier une liste")
print("")

print("1.1.1 Supprimez les trois derniers éléments un par un, dans un premier temps")
print("")

annee = ['Janvier','Février','Mars','Avril','Mai','Juin','Juillet','Août','Septembre',10,11,12]

x=0

while x <3:
  annee.remove(len(annee))
  x+=1
  print(annee)
  print("")

print("1.1.2 Puis rajoutez les mois 'Octobre', 'Novembre', 'Décembre' à la fin")
print("")

annee.append("Octobre")
annee.append("Novembre")
annee.append("Décembre")
print(annee)
print("")

print("1.1.3 Supprimez les trois derniers éléments un par un, dans un premier temps")
print("")

annee = ['Janvier','Février','Mars','Avril','Mai','Juin','Juillet','Août','Septembre',10,11,12]
x=0

while x <3:
  annee.remove(len(annee))
  x+=1
  print(annee)
  print("")

a="Octobre"
b= "Novembre"
c= "Décembre"
print("Remplacez les 3 derniers éléments par le nom du mois correspondant")
print("")

annee.extend([a,b,c])
print(annee)
print("")

print("1.1.4 Pour aller plus loin : la liste 'en compréhension'")
print("")

x = [1, 2, 3, 4, 3, 5, 3, 1, 3, 2]
resultat = [y+1 for y in x]
print(resultat)
print("")

print("2.Tuples")
print("2.1 Accès aux éléments d'un tuple")
print("")

moisDeLannee = ('Janvier','Février','Mars','Avril','Mai','Juin','Juillet','Août','Septembre','Octobre','Novembre','Décembre')

quatriemeElement = moisDeLannee [4]
print(quatriemeElement)
print("")

print("2.2 Vérifier la présence d’un élément dans un tuple")
print("")

trouver = 'Mars' in moisDeLannee
print("Mars est-il dans la liste ?")
print(trouver)
print("")

print("3. Dictionnaires")
print("3.1 Ajoutez des éléments au dictionnaire")
print("")

age = {"Pierre" : 35 , "Paul" : 32 , "Jacques" : 27 , "Andre" : 23}

age2 = {"David" : 22 , "Veronique": 21 , "Sylvie" : 30,"Damien" :37}

age.update(age2)
print(age)
print("")

print("3.3 Accéder à une valeur à partir d’une clé")
print("")
print("L'age de Sylvie est :")
print(age["Sylvie"])
print("")

print("3.3 Accéder à une valeur à partir d’une clé")
print("")

if 'Jean' in age:
  print("Jean est dnas la liste")

else:
  print("Jean n'est pas dans la liste")
print("")

print("3.4 Gérer des valeurs multiples")
print("")

club = {
  "Pierre Durand" :(1986,1.72,70),
  "Victor Dupont" :(1987,1.89,57),
  "Paul Dupuis" :(1989,1.60,92),
  "Jean rieux" :(1985,1.88,77)
}
print("")
print("3.5 Afficher les données d’un sportif")
print("")

prenom = input("Entrez le prénom de votre choix :")

nomSportif = prenom
dateNaissSportif = club[prenom][0]
poidsSportif = club[prenom][2]
tailleSportif = club[prenom][1]

phrase = 'Le sportif nommé est %s, il est né en %s , sa taille est de %sm et son poids est de %s Kg'

print(phrase % (nomSportif,dateNaissSportif,tailleSportif,poidsSportif))
print("")

print("4.1 Club sportif : variante")
print("")

