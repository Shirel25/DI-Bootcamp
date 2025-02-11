import random 

s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVW"
i = 0
res = ""

while i < 5:
    res += random.choice(s)
    i+=1
print(res)