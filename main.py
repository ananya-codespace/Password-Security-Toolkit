import string
import random

# Password Strength Checker
def password_checker(password, offer_generator):
    pass_len = len(password)
    has_length = has_upper = has_lower = has_num = has_char = False
    
    if pass_len >= 8:
        has_length = True
    for ch in password:
        if ch.isupper():
            has_upper = True
        if ch.islower():
            has_lower = True
        if ch.isnumeric():
            has_num = True
        if not ch.isalnum():
            has_char = True

    case = sum([has_length, has_upper, has_lower, has_num, has_char])  

    if case == 5:
        print("Password Strength : Strong")
    elif case >= 3:
        print("Password Strength : Medium\n")
    else:
        print("Password Strength : Weak\n")

    if not has_length:
        print("Password should contain atleast 8 characters")
    if not has_upper:
        print("Password should contain atleast 1 upper-case letter")
    if not has_lower:
        print("Password should contain atleast 1 lower-case letter")
    if not has_num:
        print("Password should contain atleast 1 number")
    if not has_char:
        print("Password should contain atleast 1 special character")
    print()

    if case < 3 and offer_generator:
        pass_gen = input("Would you like to use the Random Password Generator tool to help generate a password? (yes/no): ")
        print()
        if pass_gen.lower() == "yes":
            new_password = password_generator()
            print("The password is", new_password)
            print()

# Random Password Generator
def password_generator():
    while True:
        pass_len = int(input("Enter the length of the password (positive non-negative number): ")) 
        if pass_len <= 0:
            print("\nInvalid length, enter again...")
            print()
        else:
            break

    print("\nThe password will contain lower-case letters by default")
    upper = input("Should the password include upper-case letters? (yes/no): ")
    num = input("Should the password include numbers? (yes/no): ")
    char = input("Should the password include special characters? (yes/no): ")
    print()

    # include all lower-case letters 
    pool = string.ascii_lowercase   # from string module 
    if upper.lower() == "yes":
        # include all upper-case letters
        pool += string.ascii_uppercase
    if num.lower() == "yes":
        # include all digits (0-9)
        pool += string.digits
    if char.lower() == "yes":
        # include all special characters
        pool += string.punctuation

    password = ""
    for i in range(pass_len):
        # to choose one character from the pool
        password += random.choice(pool)  # from random module 
    return password

print("\n -------------------- PASSWORD SECURITY TOOLKIT -------------------- \n")
print("WELCOME!\nThis tool helps you create and evaluate strong, secure passwords.")
print("The Password Strength Checker tool analyzes your password for length, character variety, and common weak patterns.")
print("The Random Password Generator tool creates a strong, random password based on the criteria you choose.\n")

while 1:
    print("Choose the tool you wish to use: \n1. Password Strength Checker\n2. Random Password Generator\n3. Exit")
    choice = int(input())
    print()

    if choice == 1:
        password_check = input("Enter your password: ")
        print()  # to add a single extra line 

        pass_list = ["password", "password123", "12345678", "qwerty", "abc123", "admin", "87654321", "login"]

        if password_check in pass_list:
            print("The password is too common, choose something unique\n")
            # exit()    # the program stops (exits) here; you need not check further conditions as the password is weak; can be used if u r not using else
        else:
            # offer_generator = True, will ask if you want to use the generator tool
            password_checker(password_check, True)

    elif choice == 2:
        password_generate = password_generator()
        print("The password is", password_generate)
        print()
        pass_check = input("Would you like to use the Password Strength Checker tool to check the strength of the password? (yes/no): ")
        print()
        if pass_check.lower() == "yes":
            # offer_generator = False, will not ask if you want to use the generator tool
            password_checker(password_generate, False)

    elif choice == 3:
        print("Exiting...")
        print("THANK YOU!\n")
        break   # as we don't have anything after the loop break can be used here; exit() can also be used
    
    else:
        print("Invalid choice, choose again...\n")

    







"""
Things learnt:
print automatically goes to new line
print() - prints 1 extra line and print("\n") - prints 2 extra lines
print() automatically adds a single space between multiple comma-separated arguments (eg: print("The value is", x)) - The value is x (space after is added automatically due to parameter 'sep')
sum() - func to add the elements
string and random module - research more 
Can use default parameters for password_checker
    def password_checker(password, offer_generator=True)
and while calling the funtion if nthg is passed by default True, or False when passed
    password_checker(password)
    password_checker(password, False)

Things to do:
menu driven - done
at the start of each tool, 1 intro statement - done 
in checker, if weak password ask if they want help of generator - done
also in generator, after generating password ask if they want to check strength - done
if length in password wrong take input again - done 
same for if choice wrong - checker, generator, exit - done 
change folder name 
"""