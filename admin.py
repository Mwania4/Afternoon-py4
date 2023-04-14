from database import Admin

admins = Admin.select()
for admin in admins:
    print(admin.name, admin.email, admin.password, admin.age, admin.duty)
