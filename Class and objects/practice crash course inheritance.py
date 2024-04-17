# 9-6. Ice Cream Stand:
class Resturant():
    def __init__(self, resturant_name, cuisine_type, number_served):
        self.resturant_name = resturant_name
        self.cuisine_type = cuisine_type
        self.opening_time = ""
        self.number_served = number_served


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


class IceCreamStand(Resturant):
    def __init__(self, resturant_name, cuisine_type, number_served):
        super().__init__(resturant_name, cuisine_type, number_served)
        self.flavurs = "vanilla"

    def describe_flavurs(self,list_of_flavurs):
        flavur_list = ''
        for flavur in list_of_flavurs:
            flavur_list += '\n-' + flavur.title()
        print("This icecream stand sells these flavurs", flavur_list)

    def open_restaurant(self):
        print("This Icecreamstand open only on afternoon!")  # example of method overriding from parent class

my_iceCreamStand = IceCreamStand("Diplom", "Icecream", 35)

my_iceCreamStand.describe_restaurant()

my_iceCreamStand.describe_flavurs({"vanilla", "chocolate", "butter scotch" })

my_iceCreamStand.open_restaurant()