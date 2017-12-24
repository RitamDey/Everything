def slope_one(item1, item2):
    card = 0
    num = 0

    for user in item1:
        if user in item2:
            card += 1
            num += (item1[user] - item2[user])

    return num/card


if __name__ == '__main__':
    data = {
        "Taylor Swift": {
            "Amy": 4,
            "Ben": 5,
            "Daisy": 5,
        },
        "PSY": {
            "Amy": 3,
            "Ben": 2,
            "Clara": 3.5,
        },
        "Whitney Houston": {
            "Amy": 4,
            "Clara": 4,
            "Daisy": 3,
        }
    }

    # print("Deviation Taylor Swift->PSY",
    #       slope_one(data["Taylor Swift"], data["PSY"]))
    items = ["Taylor Swift", "PSY", "Whitney Houston"]
    for item1 in items:
        for item2 in items:
            print(item1, item2, slope_one(data[item1], data[item2]))
