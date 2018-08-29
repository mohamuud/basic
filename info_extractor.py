#! python3
# Mohamuud mohamed mohamed @2018

# simple python script to extract email and phones // uses pyperclip module to copy and paste.
# next update we will use urllip and requestes modules to get the data instead of pyperclip.
# note_  you can use sys and sys.argv[parameter index] module to use this Script  in the command line.
# download requirement pyperclip before you run the script , other modules came with python 3.
import os
import sys
import pyperclip
import re

# functions
def searchMail(text_to_search):
    result = ""
    pattern = re.compile(r"[a-zA-Z-0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+")
    info = pattern.finditer(text_to_search)
    for i in info:
        result += i.group()+" "
    return result.split()

def searchNumSo(phone_NUm):
    result = ""
    pattern = re.compile(r'''(
(\d{3}|\(\d{3}\))?
(\s|-|\.)?
(\d{3})
(\s|-|\.)
(\d{3})
(\s*(ext|x|ext.)\s*(\d{2,5}))?
)''', re.VERBOSE)
    info = pattern.finditer(phone_NUm)
    for i in info:
        result += i.group() + " "
    print(result)
    return result.split()


print(""" Enter your Option
 1. to search Emails
 2. to search Phone Numbers""")

ch = input("")

# if len(sys.argv) < 2:
#      print("Usage: python info_extractor.py [option]")
#      sys.exit()

if int(ch) == 1:
    var_Emails = str(pyperclip.paste())
    result = searchMail(var_Emails)
    if not"data.txt" in os.listdir(os.getcwd()) and len(result) > 0:
        file = open("data.txt", "w")
        file.write(str(result))
        file.close()
        print("Created New File Data.txt In this directory {}".format(os.getcwd()))
    elif "data.txt" in os.listdir(os.getcwd()) and len(result) > 0:
        file = open("data.txt", "a")
        file.write(str(result))
        file.close()
        print("Updated the Data.txt file in This directory {}".format(os.getcwd()))
    else:
        print("Nothing found!")
elif int(ch) == 2:
    var_phones = str((pyperclip.paste()))
    result_2 = searchNumSo(var_phones)
    if not"phone.txt" in os.listdir(os.getcwd()) and len(result_2) > 0:
        file = open("phone.txt", "w")
        file.write(str(result_2))
        file.close()
    elif "phone.txt" in os.listdir(os.getcwd()) and len(result_2) > 0:
        file_2 = open("phone.txt", "a")
        file_2.write(str(result_2))
        file_2.close()
        print("Updated The Data.txt file in This directory {}".format(os.getcwd()))
    else:
        print("We can't find matched result")

# ____________________ Try to use less code DRY(use function to save both files) _________________
