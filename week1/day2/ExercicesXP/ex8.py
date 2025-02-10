topping = []
top = ""
price = 10

while top != "quit":
    top = input("Please enter a topping (type 'quit' to stop):")
    if top != "quit":
        topping.append(top)
        print(f"I'll add {topping[-1]} on your pizza.")
        price+= 2.5

print("Here are your toppings : ", topping)
print("Total price : ", price)