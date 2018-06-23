length = int(input())
k = int(input())

arr = sorted([int(input()) for _ in range(length)])


# In this problem, I used the Double-Pointer technique where I use
# two variables, here `low` and `high`, to track the current subarray start and
# end. and difference between them is the minimum length of the subarray. Using
# this technique, I trivally found the min(subarray), i.e `arr[low]`, and the
# max(subarray), i.e `arr[high]`.
low = 0
high = low + k - 1
min_diff = None


while high < length:
    diff = arr[high] - arr[low]

    if min_diff is None or min_diff > diff:
        min_diff = diff

    low += 1
    high += 1


print(min_diff)
