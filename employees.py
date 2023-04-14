from database import Employees

employees = Employees.select()
for employee in employees:
    print(employee.name, employee.age, employee.sector)