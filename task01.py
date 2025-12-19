text = input("Text: ")

count = 0

for i in text:
    if i.lower() in "aeuio":
        count += 1
    
print(count)