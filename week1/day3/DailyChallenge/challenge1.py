word = input("Please enter a word : ")

dict = {}
valid = True

for index, letter in enumerate(word):
    if not letter.isalpha():
        print("The word must only contain letter (string)")
        print(f"{letter} n'est pas valide.")
        valid = False
        break
    
    if letter in dict:
        dict[letter].append(index)
    else:
        dict[letter] = [index]

if valid:
    print(dict)







