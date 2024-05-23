sandwich_orders = ['tuna', 'pastrami', 'chicken', 'pastrami', 'veggie', 'pastrami']
finished_sandwiches = []

print("Sandwich Orders:")
for order in sandwich_orders:
    print(f"I made your {order} sandwich.")
    finished_sandwiches.append(order)

print("\nFinished Sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)

print("\nThe deli has run out of pastrami.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print("\nUpdated Sandwich Orders (without pastrami):")
print(sandwich_orders)