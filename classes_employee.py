from classes_person import Person

# Employee is a kind of Person
# Employee is a derived class (subclass)
# Person is a base class (Superclass)


class Employee(Person):
    def __init__(self, first_name, last_name, job, tenure):
        super().__init__(first_name, last_name)
        self.job = job
        self.tenure = tenure

    def get_employee_info(self):
        return self.first_name + " " + self.last_name + " has been a " + self.job + " for " + self.tenure