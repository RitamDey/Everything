from math import floor  # just to play safe


def get_total(days):
    curr_reach = 5
    total_like = 0
    today_like = None

    for _ in range(days):
        today_like = floor(curr_reach/2)
        total_like += today_like
        curr_reach = today_like*3

    return total_like


print(get_total(int(input())))

