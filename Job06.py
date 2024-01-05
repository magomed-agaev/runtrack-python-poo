class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""

    def vieillir(self):
        self.age += 1


a = Animal()
print(a.age)  # Affiche : 0
a.vieillir()
print(a.age)  # Affiche : 1


class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""

    def vieillir(self):
        self.age += 1

    def nommer(self, prenom):
        self.prenom = prenom


a = Animal()
a.nommer("Fido")
print(a.prenom)  # Affiche : Fido
