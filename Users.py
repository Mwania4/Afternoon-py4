from database import User

users = User.select()
for user in users:
    print(user.name, user.email, user.password)

# Deleting a record from a SqLite db
User.delete().where(User.id == 1).execute()