sequence = input("Please enter a coma-separated sequence of words :")

res = [','.join(sorted(sequence.split(',')))]

print(res)