#Evc plus program
import random
print("- EVC Plus- Fadlan gali PIN-kaaga(Enter PIN) ")
numbers = [{ "mohamuud" : 615379757} ,{ "sahra" : 615337844} ,{"shukri" : 615339865},{"shamso" :615444634},{"daahir" :615326753},{"naima" :615912339},{"faarax" :616433286}]
print("Si Aad Isu Diiwaan Galid Gali Magacaaga")
l_name = input()
l_num = 0
for num in range(6):
    l_num += random.randint(1,100000)
last = {l_name : "615 "+str(l_num)}
numbers.append(last)
print("your info is {}".format(numbers[-1]))
print("Sameyso Pin Cusub")
info = {
    "lacag" : [100],
    2 : [0,89,7]
}
# testing commit
#thrid commit
balance = 100
card_bala = 0
PIN = int(input())
if (PIN == 12345):
    while True:
        print("""
        1.itus haraagaaga
        2.kaarka hadalka
        3.bixi Biil
        4.U Wareeji EVCPlus
        5.Warbixi Kooban
        6.Salaam Bank
        7.Maarynta
        0. Ka Bax""")
        ch = int(input())
        if(ch == 0):
            print("Macsalaama")
            break
        elif(ch == 1):
            print("Haraagaa waa ${}".format(balance))
            break
        elif(ch == 2):
            print("""
            1.Ku Shubo Artime
            2.Ugu Shub artime
            3.MIFI Packages
            0.Kabax""")
            ch = int(input())
            if ch == 1:
                print("Gali lacagta aad ku shubaneyso")
                bala = int(input())
                print("Mahubtaa Inaad ku Shubaneydo {} \n 1.haa \n 2.maya".format(bala))
                ch = int(input())
                if bala < balance*balance and ch == 1:
                    balance = balance - bala
                    print("waxaad ku shubay {} haraagaa waa {}".format(bala,balance))
                    break
                else:
                    print("macsalaama")
            elif( ch == 2):
                print("gali MObile Numberka")
                info[2][0]= int(input())
                if(info[2][0] in numbers):
                    print("gali lacgta")
                    info[2][1] = int(input())
                    if(ch < balance):
                        balance = balance-info[2][1]
                        print("waxaad {}$ U Wareejisay numberks {} haraaga waa {}$".format(info[2][1], info[2][0], balance))
                        break
                    else:
                        print("haraagaaga wuu yaryaha")
                        break
                else:
                    print("Numberkaa ma diiwaan gashana")
                    break
            else:
                print("wax qaldan ayaad dooratay")
                break




