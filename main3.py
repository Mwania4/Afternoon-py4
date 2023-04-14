from database import Employees
try:
    employee_name = input("Enter employee name\n")
    employee_age = input("Enter employee age\n")
    employee_sector = input("Enter employee sector\n")
    Employees.create(name=employee_name, age=employee_age, sector=employee_sector)
    print("Registration was successful")
except:
    print("An error occured")
