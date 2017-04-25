def sort(arr, arr_len):
    for i in range(arr_len):
        for j in range(arr_len-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
        print(arr)
    return arr


if __name__ == '__main__':
    arr = []
    arr_len = int(input().strip())
    for _ in range(arr_len):
        arr.append(int(input().strip()))
    print(*sort(arr, arr_len), sep='\n')
