from math import sqrt


def cosine(ratings1, ratings2):
    x_sum = 0
    y_sum = 0
    x_y_prod = 0

    for rating in ratings1:
        if rating in ratings2:
            x_sum += (ratings1[rating]**2)
            y_sum += (ratings2[rating]**2)
            x_y_prod += ratings1[rating]*ratings2[rating]
    return x_y_prod/(sqrt(x_sum)*sqrt(y_sum))


if __name__ == '__main__':
    ratings = {
            'Angelica': {
                'Blues Traveler': 3.5,
                'Broken Bells': 2,
                'Deadmau 5':  0,
                'Norah Jones': 4.5,
                'Phoenix': 5,
                'Slightly Stoopid': 1.5,
                'The Stokes': 2.5,
                'Vampire Weekend': 2
            },
            'Veronica': {
                'Blues Traveler': 3,
                'Broken Bells': 0,
                'Deadmau 5': 0,
                'Norah Jones': 5,
                'Phoenix': 4,
                'Slightly Stoopid': 2.5,
                'The Stokes': 3,
                'Vampire Weekend': 0
            }
    }

    print("%.4f" %cosine(ratings['Angelica'], ratings['Veronica']))
