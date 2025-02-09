import random #for q4

#q1
sentence = input("Please enter a string : ")
if len(sentence) < 10:
    print("string not long enough")
elif len(sentence) > 10:
    print("string too long")
else:
    print("perfect string")
print("\n===========================")

#q2
print(sentence[0])
print(sentence[-1])
print("\n===========================")

#q3
res = sentence[0]
print(res)
for car in range(1,len(sentence)):
    res+=sentence[car]
    print(res)
print("\n===========================")

#q4
characters = list(sentence)
random.shuffle(characters)
shuffled_sentence = ''.join(characters)
print(shuffled_sentence)