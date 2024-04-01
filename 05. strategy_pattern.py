# Strategy Pattern
# The strategy pattern really gives us the flexibility to combine algorithms at runtime.
# without adding any employee subclass , we can now create employee types at run-time

class Employee:
    def __init__(self, name, salary, job_title, work):
        self.name = name
        self.salary = salary
        self.job_title = job_title
        self.work = work

class ManagerJobTitle:
    def get_job_title(self):
        return "Manager"
 
class AttendantJobTitle:
    def get_job_title(self):
        return "Station Attendant"
    
class MechanicJobTitle:
    def get_job_title(self):
        return "Mechanic"

class ManagerWork:
    def get_work(self):
        return "I manage a department"

class FillGasolineWork:
    def get_work(self):
        return "I fill up cars with gasoline"

class OilChangeWork:
    def get_work(self):
        return "I change oil" 
    

employee = [Employee("Anand", 2000, ManagerJobTitle(), ManagerWork()),
            Employee("Vikash", 1800, AttendantJobTitle(), FillGasolineWork()),
            Employee("Bali", 1900, AttendantJobTitle(), FillGasolineWork()),
            Employee("Nehal", 1950, AttendantJobTitle(), OilChangeWork()),
            Employee("Lokesh", 1950, MechanicJobTitle(), OilChangeWork())]

for e in employee:
    print(f"{e.name}, ${e.salary}, {e.job_title.get_job_title()}")
    print(e.work.get_work())
    print()
    


