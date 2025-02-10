class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
    
    def bark(self):
        return f"{self.name} is barking"
    
    def run_speed(self):
        return (self.weight / (self.age*10))
    
    def fight(self, other_dog):
        if self.run_speed()*self.weight > other_dog.run_speed()*other_dog.weight :
            return f"{self.name} wins the fight against {other_dog.name}"
        else:
            return f"{other_dog.name} wins the fight against {self.name}"
        
    
dog1 = Dog("Joy", 5, 23)
dog2 = Dog("Oreo", 2, 19)
dog3 = Dog("Rocky", 3, 16)
    
dogs = [dog1, dog2, dog3]
for dog in dogs:
    print(dog.bark())
    print(dog.run_speed())

print(dog1.fight(dog2))
print(dog1.fight(dog3))
print(dog2.fight(dog3))
