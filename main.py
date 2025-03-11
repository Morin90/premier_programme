# nom = input("Quel est votre nom? ")
# age = input("Quel âge avez-vous? ")
age = 0
nom = ""

while nom.strip() == "":
    nom = input("Quel est votre nom? ").strip()
    if nom == "":
        print("ERREUR: Le nom ne peut pas être vide ou contenir uniquement des espaces.")

# Vérifier si l'âge est correct
while age == 0:
    age_str = input("Quel âge avez-vous? ")
    try:
        age = int(age_str)
        if age <= 0:
            print("ERREUR: L'âge doit être un nombre positif.")
            age = 0
    except ValueError:
        print("ERREUR: Vous devez rentrer un nombre pour l'âge")

print("Vous vous appelez " + nom + ", vous avez " + str(age) + " ans.")
print("L'année prochaine vous aurez " + str(age + 1) + " ans.")
