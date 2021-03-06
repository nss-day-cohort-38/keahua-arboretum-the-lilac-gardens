from animals import Animal
from interfaces import IFlying, ITerrestrial, IEnviroChar 

class Opeapea(Animal, IFlying, ITerrestrial, IEnviroChar):

    def __init__(self):
        Animal.__init__(self, "Ope'ape'a")
        IFlying.__init__(self)
        ITerrestrial.__init__(self)
        IEnviroChar.__init__(self)
        self.__prey = {"Insects and Vegetation"}
        self.hospitable_sunlight.append("Partial")
        self.hospitable_sunlight.append("Shady")
        self.hospitable_altitude.append("Low")
        self.hospitable_altitude.append("High Elevation")
        self.hospitable_rainfall.append("Rainy")

    @property
    def prey(self):
        return self.__prey

    def feed(self, prey):
        if prey in self.__prey:
            print(f'The Opeapea ate {prey} for a meal')
        else:
            print(f'The Opeapea rejects the {prey}')

    def __str__(self):
        return f'Ope\'ape\'a ({str(self.id).split("-")[0]}). is Ope\'ape\'aing around!'