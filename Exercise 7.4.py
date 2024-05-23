topping = ""
while topping != "quit":
    topping = input("Enter a pizza topping (enter 'quit' to finish): ")
    if topping != "quit":
        print(f"I'll add {topping} to your pizza.")
