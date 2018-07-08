simple program to use shelve (very simple way to store data into your computer)
import shelve
print("This program Using shelve module")
ch = int(input("Enter the option 1 for Entry or 0 for retrive \n "))
inc = 0
if ch == 1:
    p = int(input("How many persons you went to register \n "))
    with shelve.open("camon") as fruit:
        while p > inc:
            name = input("enter The name of the student")
            desc = input("Enter the discription of the member")
            fruit[name] = desc
            inc += 1
else:
    with shelve.open("camon") as read:
        for reads in read.items():
            print(reads)
