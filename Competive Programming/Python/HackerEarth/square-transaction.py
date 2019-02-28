def search(sales, length, target):
    low = 0
    high = length
    curr_target = -1
    
    while low < high:
        mid = (low + high) // 2
        if sales[mid] >= target:
            curr_target = mid+1
            high = mid
        else:
            low = mid+1
    return curr_target


if __name__ == '__main__':
    n_length = int(input())
    transactions = [int(i) for i in input().split()]
    accumulated = [transactions[0],]
    for i in range(1, n_length):
        accumulated.append(accumulated[i-1] + transactions[i])

    for case in range(int(input())):
        target = int(input())
        print(search(accumulated, n_length, target))

