class User:
    def __init__(self, first_name, last_name, age, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email

    def describe_user(self):
        print(f"User Information:\nName: {self.first_name} {self.last_name}\nAge: {self.age}\nEmail: {self.email}")

    def greet_user(self):
        print(f"Hello, {self.first_name}! Welcome back.")

user1 = User("Jethro", "Valdez", 19, "Jethro@gmail.com")
user2 = User("Bob", "Johnson", 21, "bob@gmail.com")
user3 = User("Eve", "Williams", 25, "eve@gmail.com")

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()
