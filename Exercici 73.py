from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, especie: str, edat: int):
        self.especie = especie
        self.edat = edat

    @abstractmethod
    def xerrar(self):
        pass

    @abstractmethod
    def mourem(self):
        pass

    def quisoc(self):
        print(f"Som un {self.especie} de {self.edat} anys.")

class Cavall(Animal):
    def xerrar(self):
        print("Hiiiiii!")

    def mourem(self):
        print("Corro amb quatre potes.")

class Dofi(Animal):
    def xerrar(self):
        print("Cliiick cliiick!")

    def mourem(self):
        print("Ned per la mar.")

class Abella(Animal):
    def xerrar(self):
        print("Bzzzzzz!")

    def mourem(self):
        print("Volo d'una flor a l'altra.")

    def picar(self):
        print("T'he picat!")

class Huma(Animal):
    def __init__(self, nom: str, edat: int):
        super().__init__("Humà", edat)
        self.nom = nom

    def xerrar(self):
        print(f"Hola, som {self.nom}.")

    def mourem(self):
        print("Camin amb dues cames.")

class Fiet(Huma):
    def __init__(self, nom: str, edat: int, pares: list["Huma"]):
        super().__init__(nom, edat)
        self.pares = pares

    def nompares(self):
        noms = [pare.nom for pare in self.pares]
        print("Els meus pares són:", ", ".join(noms))

class Centaure(Cavall, Huma):
    def __init__(self, nom: str, edat: int):
        # Tractam la especie com "Centaure"
        Animal.__init__(self, "Centaure", edat)
        self.nom = nom

    def xerrar(self):
        print(f"Som en {self.nom}, un centaure.")

    def mourem(self):
        print("Corro com un cavall i pens com un humà.")

class Xou:
    def xerrar(self):
        print("Som un Xou, però també xerr.")

    def mourem(self):
        print("Em moc d'una manera estranya.")

    def quisoc(self):
        print("Som una classe Xou sense relació amb Animal.")

if __name__ == "__main__":
    pare1 = Huma("Joan", 40)
    pare2 = Huma("Maria", 38)

    elements = [
        Cavall("Cavall", 5),
        Dofi("Dofí", 8),
        Abella("Abella", 1),
        Huma("Pere", 30),
        Fiet("Toni", 8, [pare1, pare2]),
        Centaure("Quiró", 120),
        Xou()
    ]

    for e in elements:
        print("-----")
        e.xerrar()
        e.mourem()
        if hasattr(e, "quisoc"):
            e.quisoc()
        if isinstance(e, Abella):
            e.picar()
        if isinstance(e, Fiet):
            e.nompares()
