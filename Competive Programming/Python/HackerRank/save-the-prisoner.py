def warn(n_prisoners, n_candies, start_id):
    last_prisoner = (n_candies + start_id) - 1
    if last_prisoner >= n_prisoners:
        last = last_prisoner % n_prisoners
        if last == 0:
            return n_prisoners
        else:
            return last
    else:
        return last_prisoner


if __name__ == '__main__':
    for _ in range(int(input())):
        n_prisoners, n_candies, start_id = map(int, input().split())
        print(warn(n_prisoners, n_candies, start_id))
