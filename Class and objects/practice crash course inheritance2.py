# 9-7. Admin: , 9.8. Privileges
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


class Privileges():
    def __init__(self, privileges = []):
        self.privileges = privileges

    def show_privileges(self, get_privileges):
        str_privileges = ''
        for privilege in get_privileges:
            str_privileges += '\n-' + privilege
        print('This user has these privilages' + str_privileges)


class Admin(User):
    def __init__(self, first_name, last_name, phone, email, login_attempts):
        super().__init__(first_name, last_name, phone, email, login_attempts)

        self.admin_privilages = Privileges()


        """
        self.privileges = ["can add post", "can delete post", "can ban user"]

   def show_privileges(self):
        str_privileges = ''
        for privilege in self.privileges:
            str_privileges += '\n-'+privilege
        print('This user has these privilages'+str_privileges)"""


admin1 = Admin("arnab","chertterjee", '+47 1234567', 'arnab@gmail.com',3)
admin1.admin_privilages.show_privileges(["can add post2", "can delete post2", "can ban user2"])

