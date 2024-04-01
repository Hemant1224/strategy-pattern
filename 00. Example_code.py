class Employee:
    def __init__(self, name, salary, job_title):
        self.name = name
        self.salary = salary
        self.job_title = job_title

employee = [Employee("Anand", 2000, "Manager"),
            Employee("Vikash", 1800, "Station Attendant"),
            Employee("Bali", 1900, "Station Attendant")]

for e in employee:
    print(f"{e.name}, ${e.salary}, {e.job_title}")


# But look at the code , there is a duplicate code . It would be nice if the job_title would be defined
# by the employee object type. For this we need to subclass the employee 