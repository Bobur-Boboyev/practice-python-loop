correct = "12345"

is_found = False
tries = 0

while not is_found:
    if tries == 3:
        print("Bloklandiz")
        break
    
    else:
        password = input("Password: ")
        tries += 1

        if correct == password:
             print("Topdingiz.")
             is_found = True
        elif correct != password and tries != 3:
             print("yana urinib ko'ring.")
