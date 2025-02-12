from specific_text import Text
import string
import re

class TextModification(Text):

    def without_punctuation(self):
        return self.text.translate(str.maketrans('', '', string.punctuation))
        # 'maketrans' creates a table for removing punctuation characters 
        # str.maketrans(ancien, new, to delete)
        # 'traslate' applies the deletion and returns the tex without punctuation

    def without_stop_words(self):
        stop_words = {"the", "a", "an", "in", "on", "is", "and", "but", "or", "because"}
        text = self.without_punctuation()
        words = text.split() # list of words
        filtered_words = []
        for word in words:
            if word.lower() not in stop_words:
                filtered_words.append(word) 
        
        return " ".join(filtered_words)

    def without_special_characteres(self):
         cleaned_text = re.sub(r'[^a-zA-Z0-9\s]', '', self.text)
         return cleaned_text

def main():
    stranger_text = TextModification.from_file('the_stranger.txt')
    print(stranger_text.without_punctuation())
    print("\n================================================")
    print(stranger_text.without_stop_words())
    print("\n================================================")
    print(stranger_text.without_special_characteres()) 

if __name__ == '__main__':
        main()


