my_city = 'Tel Aviv'

if my_city != 'Ramat Gan':
    print(f'I love {my_city}')

print('Finish')

#Syntax of if statement

#if (keyword) + (condition) + :
     #indentation + block of code


#exercise
# take the name of the user using an input()
# check if the name is the same as yours 
# if so, print 'we have the same name!'

# user_name = input('Whats your name?')

# if user_name.lower() == 'juliana':
#     print('We have the same name!')
# elif user_name == 'Daniel':
#     print('Beautiful name!')
# else:
#     print('We have different names')


number = int(input('enterna number between 1 - 100: '))

if number%3 == 0 and number%5 == 0:
    print('FizzBuzz')
elif number%5 == 0:
    print('Buzz')
elif number%3 == 0:
    print('Fizz')