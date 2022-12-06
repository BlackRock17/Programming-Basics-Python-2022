username = input()
password = input()

password_entered = input()

while password_entered != password:
    password_entered = input()

if password_entered == password:
    print(f"Welcome {username}!")

