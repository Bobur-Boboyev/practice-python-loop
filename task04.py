import random as r

random_num = r.randint(1, 20)

is_found = False

while not is_found:
    num = int(input("Num: "))
    
    if num == random_num:
        is_found = True
        print("Topding!")
    