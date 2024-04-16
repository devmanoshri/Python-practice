class Employee:
    def __init__(self, id_val, name):
        self.id_obj = id_val
        self.name_obj = name

    def display(self):
        print(f"Id is: {self.id_obj} & Name: {self.name_obj} ")


emp1 = Employee(7,"Ahana")
emp1.display()

del emp1.id_obj

emp2 = Employee(3,"Mamon")

try:
    print(emp1.id_obj)
except AttributeError:
    print('id does not exist')

emp2.display()

del emp2

try:
    emp2.display()
except NameError:
    print("emp2 desn't exist")

