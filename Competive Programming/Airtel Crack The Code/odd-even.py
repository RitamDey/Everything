def is_odd_even(arr):
    if not arr:
        return False
    odd_sum = sum([n%2==1 for n in arr])
    even_sum = sum([n%2==0 for n in arr])
    return odd_sum == even_sum


if __name__ == "__main__":
    n_length = int(input())
    arr = list(map(int, input().split()))
    n_subs = 0


    for i in range(n_length):
        for j in range(n_length):
            if is_odd_even(arr[i:j+1]):
                # print(arr[i:j+1])
                n_subs += 1

    print(n_subs)

