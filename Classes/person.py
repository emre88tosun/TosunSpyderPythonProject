"""
@author: emretosun

"""
class Person:
    def __init__(self, firstName, lastName, age):
        self.firstName = firstName;
        self.lastName = lastName;
        self.age = age;
    def getFullname(self):
        return self.firstName + " " + self.lastName;
    def isEmployee(self):
        return False;
firstPerson = Person("Emre", "Tosun", 25);
print(firstPerson.firstName)
class Employee(Person):
    def __init__(self, firstName, lastName, age, salary):
        self.firstName = firstName;
        self.lastName = lastName;
        self.age = age;
        self.salary = salary;
    def isEmployee(self):
        return True;
    def getSalary(self):
        return self.salary;
john = Employee("John", "Doe", 25, "$2300");
print(john.getFullname(), john.isEmployee());
print(john.getFullname(), john.getSalary());
jane = Person("Jane", "Doe", 23);
print(jane.getFullname(), jane.isEmployee());