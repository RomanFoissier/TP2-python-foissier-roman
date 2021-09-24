print ("1. Chaine de caractère")
print ("1.1 accès aux éléments d'une chaine")
print ("")


ch = "Esope reste ici et se repose"
print ("Longueur de la chaine : ")
print (len(ch))
print("")

print ("1.1.2 afficher le deuxième mot de la chaine ch en utilisant les crochets et une plage [x :y]")
print("")

print ("Deuxième mot de la chaine : ")
print(ch[6:12])
print("")

print ("1.1.3 afficher le dernier mot de la chaine ch en utilisant les crochets et une plage [x :y]")
print("")

print ("Dernier mot de la chaine :")
print (ch[22:28])
print("")

print("1.1.4 afficher le dernier mot de la chaine ch en utilisant les crochets et une plage [x :]")
print("")

print ("Dernier mot de la chaine avec une plage [x:]")
print(ch[22:])
print("")

print("1.1.5 afficher le caractère ‘c’ de deux manières différentes")
print("")

print("Première méthode :")
print(ch[13:14])
print("Deuxieme méthode :")
print(ch[-15])
print("")


print("1.2 Utilisation combinée de chaines et de variables")
print("")

print("")
print("1.2.1 Initialiser les chaines suivantes")
print("")

meteo = 'aujourd’hui, il fait %s , la vitesse du vent est %s ,l’humidité est %s'
tempDeg = "24°"


VitesseVent = "12Km/h"
Humidite = "45%"

print(meteo % (tempDeg,VitesseVent,Humidite))

print("1.2.2 Variante")
print("")

d = 'aujourd’hui, il fait beau , la vitesse du vent est faible ,l’humidité est correcte'

temp = "beau"
VitesseVent2 = "faible"
Humidite2 = "correcte"

print(meteo % (temp,VitesseVent2,Humidite2))
print("")
print("1.2.3 Initialiser les chaines suivantes")

chaineA = "cette chaine "
chaineB = "contient %s caractères "
chaineC = "par contre "
chaineD = "celle-ci "

chaineEntiere1 = chaineA + chaineB 
chaineEntiere2 = chaineD + chaineB + chaineC

print("")

print(chaineEntiere1 % (len(chaineEntiere1)))
print(chaineEntiere2 % (len(chaineEntiere2)))
print("")

print("1.2.4 Autre méthode de formatage de chaines")
print("")

chaineBnew = chaineB.replace("%s","{}")
chaineF= chaineD + chaineBnew + chaineC
chaineE = chaineA + chaineBnew

print(chaineE.format (len(chaineE)))

