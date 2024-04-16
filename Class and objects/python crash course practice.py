
#9.1, 9.4
class Resturant():
    def __init__(self, resturant_name, cuisine_type, number_served):
        self.resturant_name = resturant_name
        self.cuisine_type = cuisine_type
        self.opening_time = ""
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Resturant name is: {self.resturant_name.title()}, cuisine type is: {self.cuisine_type.title()} "
              f"and number of customers the resturant has served: {self.number_served}")

    def open_restaurant(self, res_opening_time):
        self.opening_time = res_opening_time
        print("The resturant will open on:", self.opening_time)

    def set_number_served(self, new_serverd):
        self.number_served = new_serverd
        print(f"Now {self.resturant_name} resturant has been served {self.number_served} customers!")

    def increment_number_served(self, increment_served):
        self.number_served += increment_served
        print(f"After increment {self.resturant_name} resturant has been served {self.number_served} customers!")




my_resturant = Resturant("Bangaliana","indian",12)

my_resturant.describe_restaurant()
my_resturant.open_restaurant("10:30")

# 9.2

returant1 = Resturant("chiness","chiness mat", 100)
returant2 = Resturant("Italian","Italian mat", 200)
returant3 = Resturant("Maxican","Maxican mat", 300)

returant2.set_number_served(250)
returant2.increment_number_served(20)
returant1.increment_number_served(20)

returant1.describe_restaurant()
returant2.describe_restaurant()
returant3.describe_restaurant()

# 9.3, 9.5
class User():
    def __init__(self, first_name, last_name, phone, email, login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.login_attempts = login_attempts
    def describe_user(self):
        print(f"Name: {self.first_name.title()} {self.last_name.title()}\nPhone: {self.phone} \nEmail: {self.email}")

    def greet_user(self):
        print(f"Hello {self.first_name.title()} {self.last_name.title()}! \nWelcome to our resturant")

    def increment_login_attempts(self):
        self.login_attempts += 1
        print(f"Your current login attempt: {self.login_attempts}")

    def reset_login_attempts(self):
        self.login_attempts = 0
        print(f"Your  login attempt has been reset: {self.login_attempts}")

user1 = User("arnab","chertterjee", '+47 1234567', 'arnab@gmail.com',3)
user1.describe_user()
user1.greet_user()
user1.increment_login_attempts()
user1.reset_login_attempts()