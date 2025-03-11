# On demande le nom et l'âge de l'utilisateur
"""Print() pour écrire,
input() pour recevoir l'info de l'utilisateur
qui sera envoyé dans notre variable
nom = input("Quel est votre nom? ")
age = input("Quel âge avez-vous? ")
# la fonction in() pour passer la varaible en integer
# la fonction str() pour passer la variable en string (chaîne de caracteres)
# la fonction type() pour savoir le type de ma variable
try:
    age_prochain = int(age) + 1
except:
    print("ERREUR: Vous devez rentrer un nombre pour l'âge")
else:
# print(type(nom))
# print(type(age))
    print("Vous vous appelez" + " " + nom + ", vous avez "+ str(age) + " ans.")
    print("L'année prochaine vous aurez "+ str(age_prochain) + " ans.")
print("Merci, passez une bonne journée")
# print("ERREUR: Vous devez rentrer un nombre pour l'âge")"""

# Boucle while
# n = 0
# # print(n)
# # n = n + 1
# # print(n)
# print("Début de la boucle ")
# while n <= 10:
#     print("Valeur de n : " + str(n))
#     n = n + 1
# print("Fin de la boucle ")

# mot_de_passe = ""
# while not mot_de_passe == "TOTO":
#     mot_de_passe = input("Quel est votre mot de passe ? ")
# print("Mot de passe correct, vous avez accès au compte")