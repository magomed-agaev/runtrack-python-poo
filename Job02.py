class Operation:
    def __init__(self, nombre1=0, nombre2=0):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def __str__(self):
        return f"Operation: nombre1 = {self.nombre1}, nombre2 = {self.nombre2}"


# Instanciation de la classe
operation = Operation(10, 20)

# Impression de l'objet en console
print(operation)
