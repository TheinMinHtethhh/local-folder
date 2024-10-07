from colorama import Fore, Style, init

num1 = int(input("enter number 1  "))
num2 = int(input("enter number 2  "))

result = num1 + num2
print(Fore.GREEN+f"the result is {result}")
user_name = "theinmin"
password = "1234"
print(Fore.RED + "welcome to our coding system ")
print(Fore.GREEN + "you need to log in")
user_name_input = input("enter username ")
password_input = input("enter your password ")
if user_name == user_name_input and password == password_input:
    print(Fore.BLUE + f"welcome back {user_name}  how was it mann?")
else:
    print(Fore.BLACK + "try again")