# nom = input("Quel est votre nom? ")
# age = input("Quel âge avez-vous? ")


def demander_age():
    age_int = 0
    while age_int == 0:
        age_str = input("Quel âge avez-vous? ")
        try:
            age_int = int(age_str)
            if age_int <= 0:
                print("ERREUR: L'âge doit être un nombre positif.")
                age_int = 0
        except ValueError:
            print("ERREUR: Vous devez rentrer un nombre pour l'âge")
    return age_int

def demander_nom():
    nom_str = ""
    while nom_str == "":
        nom_str = input("Quel est votre nom? ").strip()
        if nom_str == "":
            print("ERREUR: Le nom ne peut pas être vide ou contenir uniquement des espaces.")
    return nom_str
# Demander le nom
nom = demander_nom()
# Demander l'âge
age = demander_age()
# Afficher le résultat
print("Vous vous appelez " + nom + ", vous avez " + str(age) + " ans.")
print("L'année prochaine vous aurez " + str(age + 1) + " ans.")

