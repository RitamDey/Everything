import math


def distance(ratings1, ratings2, p):
    total_distance = 0.0
    diff = 0.0
    for rating in ratings1:
        if rating in ratings2:
            diff = abs(ratings1[rating] - ratings2[rating]) ** p
            total_distance += diff
    return math.pow(total_distance, 1/p)


def nearest(users_ratings, base_user, p):
    user_ratings = users_ratings[base_user]
    distances = []

    for user in users_ratings:
        if user != base_user:
            distances.append((
                user, distance(user_ratings, users_ratings[user], p
                )))
    
    return sorted(distances, key=lambda r: r[-1])[0]


if __name__ == '__main__':
    users = {
        "Angelica": {
            "Blues Traveler": 3.5, "Broken Bells": 2.0,
            "Norah Jones": 4.5, "Phoenix": 5.0,
            "Slightly Stoopid": 1.5, "The Strokes": 2.5,
            "Vampire Weekend": 2.0
            },
        "Bill": {
            "Blues Traveler": 2.0, "Broken Bells": 3.5,
            "Deadmau5": 4.0, "Phoenix": 2.0,
            "Slightly Stoopid": 3.5, "Vampire Weekend": 3.0
            },
        "Chan": {
            "Blues Traveler": 5.0, "Broken Bells": 1.0,
            "Deadmau5": 1.0, "Norah Jones": 3.0,
            "Phoenix": 5, "Slightly Stoopid": 1.0
            },
        "Dan": {
            "Blues Traveler": 3.0, "Broken Bells": 4.0,
            "Deadmau5": 4.5, "Phoenix": 3.0,
            "Slightly Stoopid": 4.5, "The Strokes": 4.0,
            "Vampire Weekend": 2.0
            },
        "Hailey": {
            "Broken Bells": 4.0, "Deadmau5": 1.0,
            "Norah Jones": 4.0, "The Strokes": 4.0,
            "Vampire Weekend": 1.0
            },
        "Jordyn": {
            "Broken Bells": 4.5, "Deadmau5": 4.0,
            "Norah Jones": 5.0, "Phoenix": 5.0,
            "Slightly Stoopid": 4.5, "The Strokes": 4.0,
            "Vampire Weekend": 4.0
            },
        "Sam": {
            "Blues Traveler": 5.0, "Broken Bells": 2.0,
            "Norah Jones": 3.0, "Phoenix": 5.0,
            "Slightly Stoopid": 4.0, "The Strokes": 5.0
            },
        "Veronica": {
            "Blues Traveler": 3.0, "Norah Jones": 5.0,
            "Phoenix": 4.0, "Slightly Stoopid": 2.5,
            "The Strokes": 3.0
            }
        }
    
    for user in users:
        print(f"Nearest Neighbour for {user} is {nearest(users, user, 2)}")

