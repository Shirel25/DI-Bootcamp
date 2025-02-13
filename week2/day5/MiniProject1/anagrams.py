from anagram_checker import * # AnagramChecker, file_path

def main():
    print("\n============= Menu =============") 
    while True:
        users_word = input("Enter a word (w) or exit (q) :")
        users_word = users_word.strip() # .strip() removes spaces before and after the word

        if users_word == "q":
            print("Goodbye !")
            break

        # Checking the validity of the word
        if " " in users_word: 
            print("Error : Only a single word is allowed.")
            continue
        if not users_word.isalpha():
            print("Error : Only alphabetic characters are allowed.")
            continue

        # valided word
        print(f"YOUR WORD : {users_word.upper()}")
        checker = AnagramChecker(file_path)
        if checker.is_valid_word(users_word):
            print("This is a valid English word.")
            print(f"Anagrams for your word : {checker.get_anagrams(users_word)}")
        else:
            print("Sorry your word is not a valid English word.")
        




if __name__ == '__main__':
    main()