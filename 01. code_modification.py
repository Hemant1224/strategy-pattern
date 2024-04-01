# The job titles are now defined in the subclass 
# we have removed the job_title from Employee class 
# And we replaced Employee class instance with Manager and Attendant class
# Using inheritance we have solved the duplicate code

# But inheritance can lead to some other problmes
# Lets see by adding some more methods to the subclasses in the next example 02. code_modification.py

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def get_job_title(self):
        return "Manager"
    
class Attendant(Employee):
    def get_job_title(self):
        return "Station Attendant"

employee = [Manager("Anand", 2000),
            Attendant("Vikash", 1800),
            Attendant("Bali", 1900)]

for e in employee:
    print(f"{e.name}, ${e.salary}, {e.get_job_title()}")


