class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.login_attempts = 0

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

user1 = User("JohnDoe", "johndoe@example.com")

user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()

print("Login Attempts:", user1.login_attempts)

user1.reset_login_attempts()

print("Login Attempts after reset:", user1.login_attempts)
