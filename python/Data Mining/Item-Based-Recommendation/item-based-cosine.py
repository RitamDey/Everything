from math import sqrt


user = {
    "David": {
        "Imagine Dragons": 3,
        "Daft Punk": 5,
        "Lorde": 4,
        "Fall Out Boy": 1
    },
    "Matt": {
        "Imagine Dragons": 3,
        "Daft Punk": 4,
        "Lorde": 4,
        "Fall Out Boy": 1
    },
    "Ben": {
        "Kacey Musgraves": 4,
        "Imagine Dragons": 3,
        "Lorde": 3,
        "Fall Out Boy": 1
    },
    "Chris": {
        "Kacey Musgraves": 4,
        "Imagine Dragons": 4,
        "Daft Punk": 4,
        "Lorde": 3,
        "Fall Out Boy": 1
    },
    "Tori": {
        "Kacey Musgraves": 5,
        "Imagine Dragons": 4,
        "Daft Punk": 5,
        "Fall Out Boy": 3
    }
}


def cosine(users: dict, item1: str, item2: str) -> float:
    """
    Cosine Similarity between two items
    """
    avg_ratings = {}
    for user in users:
        values = users[user].values()
        avg_ratings[user] = round(sum(values)/len(values), 2)

    num = 0.0
    dem1 = 0.0
    dem2 = 0.0
    for user in users:
        if item1 in users[user] and item2 in users[user]:
            x = users[user][item1] - avg_ratings[user]
            y = users[user][item2] - avg_ratings[user]
            num += (x*y)
            dem1 += (x**2)
            dem2 += (y**2)
    return round((num/(sqrt(dem1)*sqrt(dem2))),4)


if __name__ == '__main__':
    print("Similarity of Imagine Dragons and Kacey Musgraves", cosine(user, "Kacey Musgraves", "Imagine Dragons"))
    print("Similarity of Kacey Musgraves and Fall Out Boy", cosine(user, "Kacey Musgraves", "Fall Out Boy"))
