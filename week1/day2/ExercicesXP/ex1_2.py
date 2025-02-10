#exercice 1 
my_fav_numbers = {2, 5, 7}
print(my_fav_numbers)

my_fav_numbers.add(1)
my_fav_numbers.add(3)
print(my_fav_numbers)

last_element = list(my_fav_numbers)[-1]
my_fav_numbers.remove(last_element)
print(my_fav_numbers)

friend_fav_numbers = {1, 3, 6, 8}

our_fav_numbers = my_fav_numbers | friend_fav_numbers
print(our_fav_numbers)
print("\n================================")

# exercice 2
my_tuple = (1, 2, 5)
print(my_tuple)

# In Python, tuples are immutable, meaning that once
# they are created, their elements cannot be changed, 
# added, or removed.

