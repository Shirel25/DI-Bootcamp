basket = ["Banana", "Apples", "Oranges", "Blueberries"]
print(basket)

basket.remove("Banana")
print(basket)

basket.remove("Blueberries")
print(basket)

basket.append("Kiwi")
print(basket)

basket.insert(0, "Apples")
print(basket)

count = 0
for fruit in basket:
    if fruit == "Apples":
        count += 1
print(f"The are {count} apples in the basket")

basket.clear()
print(basket)
