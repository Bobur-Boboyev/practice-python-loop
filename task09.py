from random import randint

pin_code = randint(1000, 9999)

tries = 0
is_found = False

while not is_found:
    if tries == 7:
        print("Bloklandingiz!")
        break

    else:
        your_pin = int(input(f"{tries+1}-urinish. pin code: "))
        tries += 1

        if pin_code == your_pin:
            print("Tabriklaymiz, topdingiz!")
            is_found = True
        elif pin_code > your_pin:
            print("Juda katta son!")
        else:
            print("Juda kichik son!")