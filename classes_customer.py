from classes_person import Person


class Customer(Person):
    def __init__(self, first_name, last_name, customer_type, tenure):
        super().__init__(first_name, last_name)
        self.customer_type = customer_type
        self.tenure = tenure

    def get_customer_info(self):
        return self.first_name + " " + self.last_name + " has been a " + self.customer_type + " customer " + "for " + self.tenure