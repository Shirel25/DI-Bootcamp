family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

cost = ""
total_cost = 0

for person in family:
    if family[person] < 3:
        cost += f"{person} doesn't have to pay.\n"
        total_cost += 0
    elif 3 <= family[person] < 12:
        cost += f"{person} have to pay 10$.\n"
        total_cost += 10
    else:
        cost += f"{person} have to pay 15$.\n"
        total_cost += 15

print(cost)
print(f"The family's total cost for the movies is {total_cost}$.")


### Bonus ###
# We could use a function to avoid repeating the code. 
# But at that point in the course, we hadn't learned about functions yet. 
family2 = {}
members = int(input("How many members does your family have ? : "))

for i in range(members):
    name = input(f"What is the name n°{i+1} ? : ")
    age = int(input("How old his he ? : "))
    print("\n")
    family2[name] = age

print(f"Here is the family2 : \n{family2}")

cost2 = ""
total_cost2 = 0
for person in family2:
    if family2[person] < 3:
        cost2 += f"{person} doesn't have to pay.\n"
        total_cost2 += 0
    elif 3 <= family2[person] < 12:
        cost2 += f"{person} have to pay 10$.\n"
        total_cost2 += 10
    else:
        cost2 += f"{person} have to pay 15$.\n"
        total_cost2 += 15

print(cost2)
print(f"The family's total cost for the movies is {total_cost2}$.")
