active = True
while active:
    age = input("Enter your age (enter 'quit' to exit): ")
    if age.lower() == 'quit':
        active = False
    else:
        age = int(age)
        if age < 3:
            print("Your ticket is free.")
        elif 3 <= age <= 12:
            print("Your ticket costs $10.")
        else:
            print("Your ticket costs $15.")