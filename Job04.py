class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def SePresenter(self):
        return f"Nom : {self.nom}, Prénom : {self.prenom}"


# Instanciation de plusieurs personnes
personne1 = Personne("Kazama", "Jin")
personne2 = Personne("Mishima", "Kazuya")

# Appel à la méthode SePresenter
print(personne1.SePresenter())
print(personne2.SePresenter())
