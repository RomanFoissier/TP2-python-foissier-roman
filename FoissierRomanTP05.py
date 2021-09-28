print("1.Gestion de fichiers")
print("1.1 Génération de tables de multiplication")
print("")

nomFichier = input("Veuillez entrer le nom du fichier:")

obFichier = open(nomFichier+'.txt', "w")

   # -- coding: utf-8 --
for n in range(1,10):
    #insert separator
  for i in range(1,10):
    resultat = str(i) + " x "+ str(n)+ " = "+str(i*n)+" | "
    obFichier.write(resultat)
  obFichier.write("\n")

obFichier.close()
