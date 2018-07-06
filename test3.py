#very simple ip address checker (very simple ****)(you can improve it)
# this program will get the ip address from the user input and makes validation and the saves as txt file
print("please enter the ip address")
ip = input()
ip = ip.split(".")
if len(ip) < 5:
    with open("D:\ip.txt", 'w') as ip_address:
        for i in range(len(ip)):
            if len(ip[i]) < 4:
                print(ip[i],end=".",file=ip_address)

            else:
                print("invalid ip address")
                break
