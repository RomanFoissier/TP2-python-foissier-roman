print ("1. Structures de contrôle : boucle for")
print("1.1 Ecrire un programme qui écrit 50 fois facile!")


for x in range(50):
  print("Facile !")
  print("")

print("1.2 Afficher 25 étoiles « * » sur une ligne (avec une boucle )")
for x in range (25):
  print("*",end="")

print("")

print("1.3 Afficher tous les entiers de 21 à 145 avec une boucle for")
print("")

for x in range(21,145):
  print(x)

print("")

print("1.4 Afficher le carré de i avec i variant de 1 à 40 et affiche « le carre de 1 = 1 », « le carre de 2=4 »... « le carré de 40 = 1600 »")
print("")

a = 0
resultat =0
phrase = "Le carré de %s est %s"
for i in range (1,41):
  a=a+1
  resultat= a**2
  print(phrase % (a,resultat))

print("1.5 Calculer la somme de tous les entiers de 21 à 145 puis l’afficher")
print("")


addition=0
somme =0

for i in range(21,145):
 somme=somme+i
 print(somme)

print("")
print("1.6 Calculer 35! (factorielle).")
print("")

#nbr = int(input('Entrez un nombre : '))
#fact = 1
#for i in range(1, nbr+1):
  #fact = fact * i
#print (nbr,'! = ',fact)

print("")
print("1.7 Afficher un triangle rectangle composé d'étoiles « * » dont la largueur du côté est 15 * :")
print("")

for x in range (15):
  print("*")

  for y in range(x+1):
    print("*",end="")

print("")
print("")
print("2. Structures de contrôle : boucle while")
print("2.1 Remplissage de dictionnaire")

dico = {
  "computer" :("ordinateur"),
  "mouse" :("souris"),
  "keyboard" :("clavier"),
  "screen" :("ecran")
}

reset= "o"
while (reset=="o"):

  mot= input ("Entrez le mot du dico : ")

  computeur = dico[mot]
  mouse = dico[mot]
  keyboard = dico[mot]
  screen = dico[mot]

  phrase = "Le mot est %s"
  print(phrase % (dico[mot]))
  reset = input("Voulez vous continuer ? o/n  :  ")
    
  print(len(dico[mot]))
  


