class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open!")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, increment):
        self.number_served += increment


restaurant = Restaurant("Foodie Haven", "Italian")
print("Initial Number of Customers Served:", restaurant.number_served)

restaurant.number_served = 10
print("Updated Number of Customers Served:", restaurant.number_served)

restaurant.set_number_served(20)
print("Number of Customers Served after setting:", restaurant.number_served)

restaurant.increment_number_served(15)
print("Number of Customers Served after incrementing:", restaurant.number_served)
