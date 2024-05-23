sandwich_orders = ["Ham and Cheese", "Turkey Club", "BLT", "Tuna Salad"]
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\nList of sandwiches made:")
for sandwich in finished_sandwiches:
    print(sandwich)
