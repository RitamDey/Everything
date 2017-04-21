"""
Left rotating an array.
Rotating an array by 4 means:
    [1, 2, 3, 4, 5] => [5, 1, 2, 3, 4]
This means that numbers to the left of the rotate_no will come to the right
And the numbers to the right of the right of rotate_no will go to the left
"""

def array_left_rotate(a, n, k):
    new_array = a[k:]

    for elem in a[:k]:
        new_array.append(elem)

    return new_array


if __name__ == '__main__':
    n, k = map(int, input("Enter array length and rotate count: ").strip().split())
    array = list(map(int, input("Enter the array: ").strip().split()))

    print(array_left_rotate(array, n, k), sep=" ")
