import shelve
print("=" * 10 + " welcome to Evc plus program " + "=" * 10)
print("""
1. Itus haraagaaga
2. Kaarka hadalka
3. Bixi biil
4. U wareeji Evc plus
5. Warbixin kooban
6. Salaam Bnak
7. Maareynta
8. Kabax""")
numbers = [615379757,615337844,615339865,615444634,615326753,615912339,616433286]
ch = int(input())
with shelve.open("Evc") as EvcData:
    EvcData["usd"] = 123.5
    EvcData["Airtime"] = 0
    EvcData["number"] = numbers
    if ch == 1:
        print("haraagaau waa {}$".format(EvcData["usd"]))
    elif(ch == 2):
        print("""
        1. Kushubo airtime
        2. Ugushub Airtime
        3. kabax""")
        ch = int(input())
        if ch == 1:
            print("Gali lacagta aad ku shubaneyso")
            mon = int(input())
            if mon <= EvcData["usd"]:
                EvcData["Airtime"] = mon
                EvcData["usd"] = EvcData["usd"] - EvcData["Airtime"]
                print("waxaad ku shubatay {} haraagaa hada waa {} ".format(mon, EvcData["usd"]))
            else:
                print("Haraaga kuguma filna")
        elif(ch == 2):
            print("Fadlan geli mobile number ka")
            num = int(input())
            if num in EvcData["number"]:
                print("Fadlan geli lacagta loo xawilayo")
                mon = int(input())
                if mon <= EvcData["usd"]:
                    EvcData["usd"] = EvcData["usd"] - mon
                    print("waxaad {} U wareejisay {} Haraaga waa {}".format(mon,num,EvcData["usd"]))
                else:
                    print("Haraagaaga Kuguma filna")
            else:
                print("Numberkan ma diiwaan gashana")
