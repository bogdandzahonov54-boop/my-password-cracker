password = str(input())
with open("data.txt","r") as file:
    for i in file:
        if i.strip() == password:
            print(f"Password found: {i.strip()}")
            break
print("Attack finished!")
