# BASIC VALUE TYPES

# print("Hello world") #string, sequences of chars

# print(8 + 2) #numbers: 2 options- integers (not decimal), float (decimal numbers)

# print(5.75 + 3.10)

# print(type(5.35))
# print(type(10))
# print(type('Hello'))

# discover and print the type of the following values:

# 5 
# 2.54
# 'Good Morning'

# print(type(False))

# print( 5 < 7)
# print( 5 > 7)
# print ('5' == 5)

# Value Types: Integers, Floats, Strings and Booleans

#Strings functions/methods

# string = sequence of chars. So I can use indexing

# name = 'juliana'

# print(name[3])
# print(name[4:7])

# # len() = discover the length of the string
# print(len('Harry Potter'))
# print(name[4:len(name)])
# print(name[4:])
# print(name[:])

#exercise: create a variable called my_name. asign it to your name as a string
# print the middle letter of your name
# print just the second letter os your name
# print just the 3 or 2 last letters of your name

# name = 'JULIANA schmidt'

# print(name.capitalize())
# print(name.title())
# print(name.lower())

# my_hp_name = name.replace('schmidt', 'Granger')
# print(my_hp_name)

# user_name = '!John Doe!'
# cleaned_user_name = user_name.strip('!')
# print(cleaned_user_name)

# price = '$100'
# cleaned_price = price.strip('$')
# print(cleaned_price)
# print(price)

# Numbers
# print(4 + 3)
# print(4 - 2)
# print(4 * 2)
# print(4**2)
# print(4/2)
# print(5%2)
# print(5%2)

name = 'Ju'
name += 'u'
# print(name)

# name[0] = 'L' #gives an error because strings are imutable

# user_age = input('What is your age?') # the output is a string by default
my_height = '1.69'

#Type Casting (changing the type of a value)
# user_age_int = int(user_age)
my_height_float = float(my_height)

# print(user_age_int)
# print(float(1))

print('hello world \n' * 4)
print ('Hello' + ' World')

first_name = 'Juliana'
last_name = 'Schmidt'
full_name = 'Hello, my name is ' + first_name + ' ' + last_name

#string.format()

print(full_name)

# f-string

print(f'Hello, my name is {first_name} {last_name}')

