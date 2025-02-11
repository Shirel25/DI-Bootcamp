from ex4 import Family

class TheIncredibles(Family):
    def __init__(self, last_name):
        super().__init__(last_name)

    def use_power(self, name):
        for member in self.members:
            if member['name'] == name:
                if member['age'] >= 18:
                    print(f"{name} has the power of {member['power']}.")
                else:
                    raise Exception(f"{name} is not over 18 years old.")

    def incredible_presentation(self):
        print("Here is our powerful family :")
        print(f"=== {self.last_name} family ===")
        super().family_presentation()
        # print("\n=== Additionnal incredible details : ===")
        # for member in self.members:
        #     print(f"{member['name']} : Power : {member['power']}, Incredible Name : {member['incredible_name']}")



swift = TheIncredibles("Swift")
swift.members = [
        {'name':'Michael','age':35,'gender':'Male','is_child':False,'power': 'fly','incredible_name':'MikeFly'},
        {'name':'Sarah','age':32,'gender':'Female','is_child':False,'power': 'read minds','incredible_name':'SuperWoman'},
        {'name':'Samuel','age':12,'gender':'Male','is_child':True,'power': 'breath under water','incredible_name':'Samsam'}
        ]
try:
    swift.use_power("Sarah") 
    swift.use_power("Michael")
    swift.use_power("Samuel")
except Exception as e:
    print(e)
print("\n================================================")

swift.incredible_presentation()

swift.born(name = 'Jack', age=0, gender = 'Male', is_child = True, power = 'Unkown', incredible_name = 'Jacky')
swift.born(name = 'Perl', age=0, power = 'Unkown')
swift.incredible_presentation()
