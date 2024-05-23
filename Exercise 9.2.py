class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        print("The restaurant is open.")

restaurant1 = Restaurant("Italiano's", "Italian")
print(restaurant1.restaurant_name)
print(restaurant1.cuisine_type)
restaurant1.describe_restaurant()
restaurant1.open_restaurant()

restaurant2 = Restaurant("Burger Haven", "American")
restaurant2.describe_restaurant()

restaurant3 = Restaurant("Sushi Palace", "Japanese")
restaurant3.describe_restaurant()
