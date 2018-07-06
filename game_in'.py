locations = {
    0: "You are setting in front of your a computer learning python",
    1: "You are standing at the end of the road brfore a small brick bulding",
    2: "You are at the top of the hill",
    3: "You are inside a building , a well house for small stream",
    4: "You are in a velly beside a stream",
    5: "You are in the forest"
}

exits = [{"0" : 0},
         {"w" : 2, "E" : 3, "N" : 5, "S" : 4, "Q" : 0},
         {"N" : 5, "Q" : 0},
         {"W" : 1, "Q" : 0},
         {"N" : 1, "W" : 2, "Q" : 0},
         {"W" : 2, "S" : 2, "Q" : 0}
         ]
loc = 1
while True:
    availableExits = ""
    for direction in exits[loc].keys():
        availableExits += direction + ", "
    print(locations[loc])
    if loc == 0:
        break
    direction = input("available Exits are " + availableExits).upper()
    print()
    if direction in exits[loc]:
        loc = exits[loc][direction]
    else:
        print("suuro gal maaha")