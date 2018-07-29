from functions import passs, gets , check_words
import shelve
import random

users = 10
print("Dear user Enter your user name and password to continue")
name = input("name: ")
password = input("password: ")
desc = input("Descreption: ")
country = input("your Time zone : its Like This Africa/Mogadishu")

a = passs(password)
b = check_words(desc)
c = gets(country)


for i in range(users):
    ran =+ random.randint(1,100)
if a and desc and c:
    files = shelve.open("hola")
    files[str(users)] = "name " + name + " password " + a + " description " + b + " Exact Time " + str(c)
    files.close()
else:
    print("check Your Entry Please")
