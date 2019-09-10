username = input("username: ")
password = input("password: ")

verifyUsername = input("repeat username: ")
verifyPassword = input("repeat password: ")

if username == verifyUsername and password == verifyPassword:
    print("match")
else:
    print("incorrect")
