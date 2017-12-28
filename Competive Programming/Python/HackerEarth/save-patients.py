from sys import exit


def bubble_sort(arr, length):
    sort = False
    while not sort:
        for i in range(length-1):
            sort = True
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                sort = False
    return arr


length = int(input())
vaccines = bubble_sort(list(map(int, input().split())), length)
patients = bubble_sort(list(map(int, input().split())), length)


for i in range(length):
    if vaccines[i] != patients[i]:
        print("No")
        exit()
print("Yes")
