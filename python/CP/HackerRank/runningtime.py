"""
Even this problem is about the Running Time of Insertion Sort
But the problem needs the number of swaps needed
Though it explains that Insertion Sort is O(n^2)
"""
def insertion_sort(arr, length):

    swaps = 0

    for y in range(1, length):
        e = arr[y]
        x = y

        while (x>0) and (arr[x-1] > e):
            arr[x] = arr[x-1]
            x -= 1
            swaps += 1

        arr[x] = e

    return swaps


length = int(input())
arr = list(map(int, input().split()))
print(insertion_sort(arr, length))

