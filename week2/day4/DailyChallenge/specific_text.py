import os
import random

script_dir = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(script_dir, "the_stranger.txt")

class Text:
    def __init__(self, text):
        self.text = text

    def frequency(self, word):
        count = 0
        list_sentence = self.text.split()

        for w in list_sentence:
            if w.lower() == word.lower():
                count += 1
    
        if count == 0:
            return "Word not found in the text"
        else:
            return count

    def dictionary(self):
        dict_text = {}
        keys = self.text.split() # list of words
        
        for key in keys:
            key = key.lower()
            if key in dict_text:
                dict_text[key] += 1
            else:
                dict_text[key] = 1
        return dict_text

    def most_common_word(self):
        dict_text = self.dictionary()
        return max(dict_text, key = dict_text.get)
        
    def unique_words(self):
        dict_text = self.dictionary()
        list_unique = []
        
        for key in dict_text:
            if dict_text[key] == 1:
                list_unique.append(key)
        return list_unique

    @classmethod
    def from_file(cls, file_name):
        with open(file_name, 'r', encoding="utf-8") as f:
            text_content = f.read()
        return cls(text_content)


def main():
    text = Text("A good book would sometimes cost as much as a good house.")
    # text = Text(" a a a a b b c d d e e e e e f f g h")
    print(text.frequency("good")) # 2
    print(text.frequency("shirel")) # Word not found in the text

    print("\n================================================")
    print(text.most_common_word()) # a
    print(text.unique_words()) # ['book', 'would', 'sometimes', 'cost', 'much', 'house.']
    
    print("\n================================================")
    stranger_text = Text.from_file('the_stranger.txt')
    print(stranger_text.text[:500])

if __name__ == "__main__":
        main()