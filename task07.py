mx = 0

for i in range(5):
    num = int(input(f"{i+1}-Num: "))

    if i == 0:
        mx = num
    
    if num >= mx:
        mx = num

print(mx)