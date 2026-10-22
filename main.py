password = "1234"
current_guess = 0
while True:
    if str(current_guess).zfill(4) == password:
        print(f"пароль: {str(current_guess).zfill(4)}")
        break
    current_guess += 1
print("Атака завершена!")
