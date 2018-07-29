import pytz
import datetime


ac = 0
def gets(country ):
    current = pytz.timezone(country)
    localtime = datetime.datetime.now(tz=current)
    print("the time in {} is {} ".format(country,localtime))
    return localtime

def passs(pas):
    if pas.isupper():
        print("make sure your password is consists lower case")
    elif(pas.islower()):
        print("make sure your password consists UPPER CASE leter")
    elif(pas.isdigit()):
        print("make sure your password is consists Lettrs")
    else:
        tru = pas
        ac = 1
        print("Created New Account")
        return tru

def check_words(words):
    if len(words) > 20:
        print("you are using over 20 charcters please use less")
    else:
        return words
