text = input("text: ")

count = 0

for i in text:
    if i.isupper():
        count += 1

print(count)