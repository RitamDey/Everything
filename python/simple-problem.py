"""
Given an array arr[], find the maximum j - i such that arr[j] > arr[i]

Example:
    Input: [34, 8, 10, 3, 2, 80, 30, 33, 1]
    Output: 6 (j = 7, i = 1)

    Input: [9, 2, 3, 4, 5, 6, 7, 8, 18, 0]
    Output: 8 (j = 8, i = 0)

    Input: [1, 2, 3, 4, 5, 6]
    Output: 5 (j = 5, i = 0)

    Input: [6, 5, 4, 3, 2, 1]
    Output: -1
"""


arr = list(map(int, input().split()))
l = len(arr)
sol = None


for j in range(0, l):
    for i in range(0, l):
        if arr[j] > arr[i]:
            x = j-i
            try:
                if x > sol:
                    sol = j-i
            except:
                sol = j-i


print(sol)
