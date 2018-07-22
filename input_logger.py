# this program will log your input
# you can use sync method to reduce memory Usage but this is simple one

import time
import datetime
import random
import shelve
times = time.localtime()
print("*"*20 + " welcome " + "*"*20)
print("""Enter you option
1.Save
2.read""")
ch = int(input())
if ch == 1:
    file =  shelve.open("files")
    print("Enter your notes")
    note = input()
    date = str(datetime.datetime.now())
    file[date] = note
    file.close()
else:
    read = shelve.open("files")
    for item in read.items():
        print(item)
