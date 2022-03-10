# define superclass

class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name= last_name

    # getter
    def get_basic_details(self):
        return self.first_name + self.last_name

    def __str__(self):
        return "Person's name is " + str(self.get_basic_details())





