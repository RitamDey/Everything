def count_bags(balls, diff):
    count = 0
    target = diff

    while balls >= target:
        print(f"Target {target} Balls {balls}")
        count += 1
        balls -= target
        target += diff

    return count


if __name__ == '__main__':
    bags, balls, diff = map(int, input().split())

    print(bags - count_bags(balls, diff))

