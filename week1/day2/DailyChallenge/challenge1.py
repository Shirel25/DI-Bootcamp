number = int(input("Please enter a number : "))
length = int(input("Please enter a length : "))

list_multiples = [number]
number_tmp = number
for i in range (length - 1):
    number_tmp += number
    list_multiples.append(number_tmp)

print(list_multiples)