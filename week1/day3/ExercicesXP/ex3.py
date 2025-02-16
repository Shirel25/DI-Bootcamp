brand = {
    "name" : "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"], 
    "number_stores": 7000 ,
    "major_color": {
                    "France": "blue", 
                    "Spain": "red", 
                    "US": ["pink", "green"]
                 }
}

# q3
print("==== q3 ====")
print(f"=== Number of stores ===\nbefore : {brand['number_stores']}")
brand["number_stores"] = 2
print(f"=== Number of stores ===\nafter : {brand['number_stores']}")

# q4
print("\n==== q4 ====")
clients ="Zara's clothes are made for "
for clo in brand['type_of_clothes']:
    clients += clo + ', '

clients = clients.rstrip(", ")  # Remove the last comma and space
print(clients)    

# q5               
print("\n==== q5 ====")
brand['country_creation'] = 'Spain'
print(brand)

# q6
print("\n==== q6 ====")
if 'international_competitors' in brand:
    brand['international_competitors'].append("Desigual")

print(brand["international_competitors"])

# q7
print("\n==== q7 ====")
del brand["creation_date"]
print(brand)

# q8
print("\n==== q8 ====")
print(brand["international_competitors"][-1])

# q9
print("\n==== q9 ====")
print(brand['major_color']['US'])

# q10
print("\n==== q10 ====")
print(len(brand))

# q11
print("\n==== q11 ====")
print(brand.keys())

# q12
more_on_zara = {
    "creation_date": 1975, 
    "number_stores": 10000 
    }

# q13 
print("\n==== q13 ====")
brand.update(more_on_zara)
print(brand)

# q14
print("\n==== q14 ====")
print(brand["number_stores"])
# The number of stores had been updated
# Before q13, the number of stores was 2 (modified in q3), 
# after it was updated again to 10 000 from more_on_zara. 