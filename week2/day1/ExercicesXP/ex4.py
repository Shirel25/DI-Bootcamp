class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []
    
    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal) 
        else:
            print(f"{new_animal} is already in the zoo !")

    def get_animals(self):
        for a in self.animals:
            print(a)
    
    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
        else:
            print(f"{animal_sold} does not exist in the zoo")

    def sort_animals(self):
        self.animals.sort()
        
    def get_groups(self):
        animal_groups = {}
        for animal in self.animals:
            first_letter = animal[0].upper()
            if first_letter not in animal_groups:
                animal_groups[first_letter] = []
            animal_groups[first_letter].append(animal)
        for letter, group in animal_groups.items():
            print(f"{letter}:{group}")


ramat_gan_safari = Zoo("ramat_gan_safari")

print("\n==== Animals in the Zoo ====")
ramat_gan_safari.add_animal("zebra")
ramat_gan_safari.add_animal("elephant")
ramat_gan_safari.add_animal("lion")
ramat_gan_safari.add_animal("parrot")
ramat_gan_safari.add_animal("turtle")
ramat_gan_safari.add_animal("wolf")
ramat_gan_safari.add_animal("zebra")

ramat_gan_safari.get_animals()

print("\n==== Sell an Animal ====")
ramat_gan_safari.sell_animal("lion")
ramat_gan_safari.get_animals()
ramat_gan_safari.sell_animal("cougar")

print("\n==== Sorted Animals ====")
ramat_gan_safari.sort_animals()
ramat_gan_safari.get_animals()

print("\n==== Animal groups ====")
ramat_gan_safari.get_groups()

