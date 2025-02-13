import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "sowpods.txt")

class AnagramChecker:
    def __init__(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            self.words = f.read().splitlines() # words is a list

    def is_valid_word(self, word):
            if word.upper() in self.words:
                return True
            else:
                return False

    def get_anagrams(self, word):
        word = word.upper()        
        anagrams_list = []
        
        for w in self.words:
            if self.is_anagram(word, w):
                anagrams_list.append(w.lower())
        
        return anagrams_list
    
    def is_anagram(self, word1, word2):
        if word1 != word2:
            return sorted(word1) == sorted(word2)


