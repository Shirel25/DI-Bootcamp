sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", 
                   "Avocado sandwich", "Pastrami sandwich", 
                   "Egg sandwich", "Chicken sandwich", 
                   "Pastrami sandwich"]

while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")

print("Sorry, the deli is run out of Pastrami sandwich")
print(f"Remaining sandwich orders: {sandwich_orders}")   

print("\n================================================")
finished_sandwiches = []

while sandwich_orders :
    print(f"finished_sandwiches : {finished_sandwiches}")
    print(f"sandwich_orders : {sandwich_orders}")
    sandwich = sandwich_orders.pop(0)
    finished_sandwiches.append(sandwich)
    print("-----------")
print(f"finished_sandwiches : {finished_sandwiches}")
print(f"sandwich_orders : {sandwich_orders}")
        
print("\n================================================")
for sandwich in finished_sandwiches:
    print(f"I made you {sandwich}")        