print("1. commandes de base")
print("1.1 utiliser while")
print("")

x=0
prenom="c"
nbPrenom=-1
while x < 5:
  if prenom == "$":
    print("Fin de programme")
    x=6
  else:
    prenom = input ("Entrez le prenom : ")
    nbPrenom=nbPrenom+1
    
    x= x+1
print("Vous avez saisi ",nbPrenom,"prénoms" )
  

print("")
print("1.2 Utiliser for")
print("")

t =["Mary","Patricia","Linda","Barbara","Elizabeth","Jennifer","Maria","Susan","Margaret"]

for element in t:
    print (element)

print("")
print("1.3 Utiliser un dictionnaire")
print("")

dico = {
'cdrom': 4, 'lib64': 4, 'root': 4, 'srv': 4, 'mnt': 8, 'snap': 8, 'lost+found': 16, 'tmp': 76, 'run': 2692,
'sbin': 15416, 'bin': 15872, 'home': 99992, 'boot': 108272, 'opt': 116300, 'etc': 191872, 'swapfile': 385840,
'lib': 616360, 'var': 647768, 'media': 1308416, 'usr': 3357908}

print(dico)
print("")

print("")
print("1.4 accéder aux éléments du dictionnaire")
print("")

for cle,valeur in dico.items():
  print("dossier",cle," : taille = ",valeur)
print("")

print("")
print("1.5 accéder aux éléments du dictionnaire avec filtrage de valeurs")
print("")

print("tailles supérieures à 10 000 et inférieures à 100 000 : ")
for cle,valeur in dico.items():
  if valeur > 10000 and valeur < 100000:
    print("dossier",cle," : taille = ",valeur)
  
print("")
print("1.6 Création d’un tableau")
print("")

tabSize=[]
for cle,valeur in dico.items():
  tabSize = valeur = [valeur]
  print(tabSize)

print("")
print("1.7 Fonction")
print("")

tableau = [4,4,4,4,8,8,16,76,2692,15416,15872,99992,108272,116300,191872,385840,616360,647768,1308416,3357908]

def totalSize(list):
  somme = 0
  longueur = len(tableau)
  for i in range(longueur):
    somme = somme + tableau[i]
  print ("La somme est de :",somme)

totalSize(tableau)
print("")
print("1.8 Lire un fichier")
print("")

import csv;
fichier= open (r"liste_etudiants_admin_sys.csv")
myReader = csv.reader(fichier)
for row in myReader:
 print(row)

 
with open(r"liste_etudiants_admin_sys.csv") as lignes:
  compter = sum(1 for line in lignes)
  print("")
  print("Il y a ",compter," lignes dans le fichier")

print("")
print("PARTIE 2")
print("1.9 Fonction 'makeStudentClass'")
print("")


nomFichier = "liste_etudiants_admin_sys.csv"
separateur = ";"

def makeStudentClass (nomFichier,separateur):
  reader = csv.reader(open(r"liste_etudiants_admin_sys.csv"))
  newTab = {}
  for row in reader: 
   newTab = print(row)






makeStudentClass(nomFichier,separateur)

  












