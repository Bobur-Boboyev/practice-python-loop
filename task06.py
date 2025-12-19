text = input("Text: ")

sentence = 0

for i in text:
    if i in ".!?":
        sentence += 1

print(sentence)