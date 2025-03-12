# nom = input("Quel est votre nom? ")
# age = input("Quel âge avez-vous? ")


def demander_age():
    age = 0
    while age == 0:
        age_str = input("Quel âge avez-vous? ")
        try:
            age = int(age_str)
            if age <= 0:
                print("ERREUR: L'âge doit être un nombre positif.")
                age = 0
        except ValueError:
            print("ERREUR: Vous devez rentrer un nombre pour l'âge")
    return age

def demander_nom():
    nom = ""
    while nom == "":
        nom = input("Quel est votre nom? ").strip()
        if nom == "":
            print("ERREUR: Le nom ne peut pas être vide ou contenir uniquement des espaces.")
    return nom
# Demander le nom
nom = demander_nom()
# Demander l'âge
age = demander_age()
# Afficher le résultat
print("Vous vous appelez " + nom + ", vous avez " + str(age) + " ans.")
print("L'année prochaine vous aurez " + str(age + 1) + " ans.")

