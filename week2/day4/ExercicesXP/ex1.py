import os
import random

script_dir = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(script_dir, "word_list.txt")

def get_words_from_file(file):
    with open(file_path, 'r', encoding="utf-8") as f:
        words = []
        for line in f:
            l = line.strip()
            # print(f"Here is the current line : {l}")
            words.extend(line.strip().split())
    return words

def get_random_sentence(length):
    words = get_words_from_file(file_path)
    sentence = " ".join(random.choices(words, k = length))
    return sentence.lower()

def main():
    print("This program generates a random sentence containing between 2 and 20 words.")
    print("Choose the length and let the magic happen !")

    try:
        length = int(input("Choose the length you want for your sentence (2 - 20): "))
        if 2 <= length <= 20:
            print(f"sentence : {get_random_sentence(length)}")
        else:
            print("Error : The number must be between 2 and 20.")
    except ValueError as e: 
        print("Error : You have to choose a valid integer between 2 and 20.")


if __name__ == "__main__":
        main()

