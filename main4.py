from database import Admin
try:
    admin_name = input("Enter name\n")
    admin_email = input("Enter email\n")
    admin_password = input("Enter password\n")
    admin_age = input("Enter age\n")
    admin_duty = input("Enter duty\n")
    Admin.create(name=admin_name,email=admin_email,password=admin_password, age=admin_age,duty=admin_duty)
    print("Details successfully saved")
except:
    print("Try again later")