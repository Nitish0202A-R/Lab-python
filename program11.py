from collections import Counter
with open("word.txt", "r") as file:
    data = file.read()
print(data)
print(Counter(data))
