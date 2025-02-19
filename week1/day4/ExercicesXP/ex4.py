import random 

def random_number(num):
    rand_num = random.randint(1, 100)

    if num == rand_num:
        print("Your number won!")
    else:
        print("Sorry... your number was not drawn...")
        print(f"Your number : {num}")
        print(f"The number drawn : {rand_num}")

random_number(2)
random_number(5)
random_number(67)
random_number(87)