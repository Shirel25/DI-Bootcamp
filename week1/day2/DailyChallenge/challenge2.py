users_word = input("Please enter a string : ")

# ======== version 1 ========
string_single = users_word[0]

for i in range(1, len(users_word)):
    if users_word[i-1] != users_word[i]:
        string_single += users_word[i]
    
# ======== version 2 ========
# string_single = ""

# for i in range(0, len(users_word) - 1):
#     if users_word[i] != users_word[i+1]: # with range starting at 0
#         string_single += users_word[i]
    
# string_single += users_word[-1]

print(string_single)