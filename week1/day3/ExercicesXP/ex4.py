users = ["Mickey","Minnie","Donald","Ariel","Pluto"]

# q1
print("==== q1 ====")
# dic1 = {}
# for index, u in enumerate(users):
#     dic1[u] = index

dic1 = {u: index for index, u in enumerate(users)}
print(dic1)

# q2
print("==== q2 ====")

dic2 = {u : index for u, index in enumerate(users)}
print(dic2)

# q3
print("==== q3 ====")

print(dict(sorted(dic1.items())))


# q4
print("==== q4 ====")
print("1. ")
print({u : index for index, u in enumerate(users) if "i" in u.lower()})

print("2. ")
print({u : index for index, u in enumerate(users) if u[0].lower() == "m" or u[0]. lower() == "p"})