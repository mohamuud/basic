# this program will log your input
# you can use sync method to reduce memory Usage but this is simple one
import time
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
    date = " sanadka " + str(times.tm_year) + " - bisha " +str(times.tm_mon) + " - malinaa " +str(times.tm_mday) + " - daqiiqada " + str(times.tm_min) + " - mirirada " + str(times.tm_sec)
    file[date] = note
    file.close()
else:
    read = shelve.open("files")
    for item in read.items():
        print(item)
