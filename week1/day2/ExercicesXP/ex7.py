print("Please enter your favorite fruit(s).")
print("If several, please separe the fruits with a single space.")
fav_fruits = list(input().split())
print(fav_fruits)

fruit = input("Enter a name of any fruit :")
if fruit in fav_fruits: 
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy")