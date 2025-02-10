class Family:
    def __init__(self, last_name):
        self.members = []
        self.last_name = last_name
    
    def born(self, **kwargs):
        self.members.append(kwargs)
        print("Congratulations for the new child !!")

    def is_18(self, name):
        for member in self.members:
            if member['name'] == name:
                return member['age'] >= 18
    
    def family_presentation(self):
        for member in self.members:
            print(f"Name :{member['name']}, Age : {member['age']}, Gender : {member['gender']}, isChild : {member['is_child']}")
    
family = Family("Cohen")    
family.members = [
    {'name':'Michael','age':35,'gender':'Male','is_child':False},
    {'name':'Sarah','age':32,'gender':'Female','is_child':False}
]

family.family_presentation()
print("\n================================================")

family.born(name = 'Samuel', age=0, gender = 'Male', is_child = True)

print("\n================================================")
for member in family.members:
    print(f"Is {member['name']} is 18 or older ?", family.is_18(member['name']))

print("\n================================================")
family.family_presentation()