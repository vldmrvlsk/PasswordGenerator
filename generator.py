import string
import random

characters = list(string.ascii_letters + string.digits + " !@#$%^&*()")

def generate_password():
    password_length = int(input("How long would you like your password to be? "))
    
    random.shuffle(characters)
    
    password = []
    
    for x in range(password_length):
        password.append(random.choice(characters))
    
    random.shuffle(password)
    
    password = "" .join(password)
    print(password)

option = input("Do you want to generate a password? (Y/N): ")

if option == "Y":
    generate_password()
elif option == "N":
    print("WE DONE")
    quit()
else:
    print("Invalid input, please input Y or N")
    quit()