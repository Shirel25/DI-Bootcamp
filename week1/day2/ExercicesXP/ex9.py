price = 0
family = {}

nb = int(input("How many person do you want to register ? :"))
for i in range(nb):
    name = input(f"What's the name of the {i+1} person ? :")
    age = int(input("How old is she ? :"))
    family[name] = age

for name, age in family.items():
    if age < 3:
        price += 0
    elif 3 <= age < 12:
        price += 10
    else:
        price += 15

print(f"Total ticket price for the family : {price} $.")

print("\n================================================")
names = ["Shirel", "Avi", "Lea", "Samuel", "Yael"]
allowed_names = []

for name in names:
    age = int(input(f"How old are you {name} ? :"))
    if (16 <= age <= 21):
        print(f"Sorry {name}, that movie is restricted for you.")    
    else:
        allowed_names.append(name)

print(f"final allowed list :{allowed_names}")



