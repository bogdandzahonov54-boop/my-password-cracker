password = str(input("Enter password to check:"))
was_found = False
try:
    with open("data.txt","r") as file:
        for i in file:
            if i.strip() == password:
                was_found = True
                break
    if was_found:
        print(f"Password found: {password}")
    else:
        print("Password NOT found!")
except FileNotFoundError:
    print("File NOT found!")
print("Attack finished!")
