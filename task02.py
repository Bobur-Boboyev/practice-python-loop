n = int(input("Son: "))

total = 0

while n != 0:
    i = n % 10
    n = n // 10
    total += i

print(total)