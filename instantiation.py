from classes_person import Person
from classes_employee import Employee
from classes_customer import Customer

person1 = Person("Mel ", "Thomas")
print(person1.get_basic_details())
print(person1)

employee1 = Employee("Mel", "Thomas", "Software Developer", "7 Years")
employee2 = Employee("John", "Smith", "Software Developer", "8 Months")
print(employee1.get_employee_info())
print(employee2.get_employee_info())

customer1 = Customer("Jane", "Doe", "Business", "10 Years")
customer2 = Customer("Johnny", "Depp", "Private", "22 Years")
print(customer1.get_customer_info())
print(customer2.get_customer_info())
