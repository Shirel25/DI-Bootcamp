class Farm:
    def __init__(self, name):
        self.name = name 
        self.animals = {}


    def add_animal(self, animal, number = 1):
        if animal not in self.animals:
            self.animals[animal] = number
        else:
            self.animals[animal] += number

    def get_info(self):
        info = f"{self.name}'s farm\n\n"
        for animal, number in self.animals.items():
            info+= f"{animal} : {number}\n"
        info+= "\n\tE-I-E-I-0!"
        return info

    def get_animal_types(self):
        return sorted(self.animals.keys())

    def get_short_info(self):
        res = f"{self.name}'s farm has "
        for animal in list(self.animals.keys())[:-1]:
            res += f"{animal}s, "
        last_animal = list(self.animals.keys())[-1]
        res += f"and {last_animal}s."
        return res


macdonald = Farm("McDonald")
macdonald.add_animal('cow',5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())

print(macdonald.get_animal_types())
print(macdonald.get_short_info())