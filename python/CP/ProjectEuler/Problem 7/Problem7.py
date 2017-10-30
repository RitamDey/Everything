def is_prime(n):
    if n == 1:
        return False
    if n == 2 or n == 3:
        return True

    for i in range(2, n//2+1):
        if n%i == 0:
            return False
    return True



count = 0
i = 1
while True:
    if is_prime(i):
        count += 1
        if count == 10001:
            print(i)
            break
    i += 1

