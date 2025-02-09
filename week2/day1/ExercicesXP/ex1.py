class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

#Instantiate three Cat objects using the code provided above.
cat1 = Cat("Shadow", 3)
cat2 = Cat("Thunder", 6)
cat3 = Cat("Sugar", 7)

#Outside of the class, create a function that finds the oldest cat and returns the cat.
def find_oldest_cat(cats):
    oldest = cats[0]
    for cat in cats:
        if cat.age > oldest.age:
            oldest = cat
    return oldest


#Print the following string: “The oldest cat is <cat_name>, and is <cat_age> years old.”. 
#Use the function previously created.
cats = [cat1 , cat2 , cat3] 
oldest_cat = find_oldest_cat(cats)

print(f"The oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old.")