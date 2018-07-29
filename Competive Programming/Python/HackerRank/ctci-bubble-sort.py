# Complete the countSwaps function below.
def countSwaps(arr):
    swaps = 0
    
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                swaps += 1
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    return swaps

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    print("Array is sorted in",countSwaps(arr),"swaps.")
    
    print("First Element: {0}\nLast Element: {1}".format(arr[0], arr[-1]))

