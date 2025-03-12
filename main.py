# nom = input("Quel est votre nom? ")
# age = input("Quel âge avez-vous? ")
age = 0
# global age sert à dire à la fonction que
# la variable age est déterminée en dehors de celle-ci
# donc c'est une variable globale
def demander_age():
    global age
    while age == 0:
        age_str = input("Quel âge avez-vous? ")
        try:
            age = int(age_str)
            if age <= 0:
                print("ERREUR: L'âge doit être un nombre positif.")
                age = 0
        except ValueError:
            print("ERREUR: Vous devez rentrer un nombre pour l'âge")

# avec la vriable donné dans la focntion
def demander_nom():
    reponse_nom = ""
    while reponse_nom == "":
        reponse_nom = input("Quel est votre nom? ").strip()
        if reponse_nom == "":
            print("ERREUR: Le nom ne peut pas être vide ou contenir uniquement des espaces.")
    return reponse_nom


# Demander le nom
nom = demander_nom()
# Demander l'âge
demander_age()
# Afficher le résultat
print("Vous vous appelez " + nom + ", vous avez " + str(age) + " ans.")
print("L'année prochaine vous aurez " + str(age + 1) + " ans.")

