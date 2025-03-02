def longest_word(sequence):
    words = sequence.split(' ')
    # longest_word = words[0]
    # for word in words:
    #     if len(word) > len(longest_word):
    #         longest_word = word
  
    longest_word = max(words, key=len)   
    return longest_word

print(longest_word("Margaret's toy is a pretty doll."))
print(longest_word("A thing of beauty is a joy forever."))
print(longest_word("Forgetfulness is by all means powerless!"))