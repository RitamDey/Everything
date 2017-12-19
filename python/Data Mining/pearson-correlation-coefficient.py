from math import sqrt


def calc_coeff(rating1, rating2):
    sum_num = 0
    sum_x = 0
    sum_y = 0
    sum_x2 = 0
    sum_y2 = 0
    n = 0

    for rating in rating1:
        if rating in rating2:
            n += 1
            x = rating1[rating]
            y = rating2[rating]
            sum_num += x * y
            sum_x += x
            sum_y += y
            sum_x2 += x**2
            sum_y2 += y**2

    if n == 0:
        return 0

    deno = sqrt(sum_x2 - (sum_x**2) / n) *\
           sqrt(sum_y2 - (sum_y**2) / n)

    if deno == 0:
        return 0
    else:
        return (sum_num - (sum_x * sum_y) / n) / deno


if __name__ == "__main__":
    users = {"Angelica":
             {
                 "Blues Traveler": 3.5,
                 "Broken Bells": 2.0,
                 "Norah Jones": 4.5,
                 "Phoenix": 5.0,
                 "Slightly Stoopid": 1.5,
                 "The Strokes": 2.5,
                 "Vampire Weekend": 2.0
             },
             "Bill":
             {
                 "Blues Traveler": 2.0,
                 "Broken Bells": 3.5,
                 "Deadmau5": 4.0,
                 "Phoenix": 2.0,
                 "Slightly Stoopid": 3.5,
                 "Vampire Weekend": 3.0
             },
             "Chan":
             {
                 "Blues Traveler": 5.0,
                 "Broken Bells": 1.0,
                 "Deadmau5": 1.0,
                 "Norah Jones": 3.0,
                 "Phoenix": 5,
                 "Slightly Stoopid": 1.0
             },
             "Dan":
             {
                 "Blues Traveler": 3.0,
                 "Broken Bells": 4.0,
                 "Deadmau5": 4.5,
                 "Phoenix": 3.0,
                 "Slightly Stoopid": 4.5,
                 "The Strokes": 4.0,
                 "Vampire Weekend": 2.0
             },
             "Hailey":
             {
                 "Broken Bells": 4.0,
                 "Deadmau5": 1.0,
                 "Norah Jones": 4.0,
                 "The Strokes": 4.0,
                 "Vampire Weekend": 1.0
             },
             "Jordyn":
             {
                 "Broken Bells": 4.5,
                 "Deadmau5": 4.0, "Norah Jones": 5.0,
                 "Phoenix": 5.0,
                 "Slightly Stoopid": 4.5,
                 "The Strokes": 4.0,
                 "Vampire Weekend": 4.0},
             "Sam":
             {"Blues Traveler": 5.0,
              "Broken Bells": 2.0,
              "Norah Jones": 3.0,
                 "Phoenix": 5.0,
              "Slightly Stoopid": 4.0,
              "The Strokes": 5.0
              },
             "Veronica":
             {
                 "Blues Traveler": 3.0,
                 "Norah Jones": 5.0,
                 "Phoenix": 4.0,
                 "Slightly Stoopid": 2.5,
                 "The Strokes": 3.0
             }
             }

    print(calc_coeff(users['Angelica'], users['Bill']))
    print(calc_coeff(users['Angelica'], users['Hailey']))
    print(calc_coeff(users['Angelica'], users['Jordyn']))
