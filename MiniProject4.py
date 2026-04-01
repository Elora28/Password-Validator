def check_password(password):
    if len(password) < 8:
        return False

    has_number = False
    for char in password:
        if char.isdigit():
            has_number = True
            break
    if not has_number:
        return False

    has_upper = False
    for char in password:
        if char.isupper():
            has_upper = True
            break
    if not has_upper:
        return False

    special_characters = "!@#$%^&*()-_=+[]{};:'\",.<>?/\\|`~"
    has_special = False
    for char in password:
        if char in special_characters:
            has_special = True
            break
    if not has_special:
        return False

    return True


while True:
    user_password = input("Enter a password: ")

    if check_password(user_password):
        print("Password is valid!")
    else:
        print("Password is NOT strong enough.")

    again = input("Do you want to check another password? (yes/no): ")
    if again == "yes":
        print(input("Enter another password: "))
    else:
        break