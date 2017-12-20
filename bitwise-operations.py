"""
Tutorial is at https://www.hackerearth.com/practice/basic-programming/bit-manipulation/basics-of-bit-manipulation/tutorial/
"""


"""
Using Left Shift `<<` operation is like multiplying a number with 2^k
"""

print("5 * 4:", 5<<2)
print("5 * 8:", 5<<3)
print("10 * 32:", 10<<5)


"""
We can easily check if a number is in power of 2 ,i.e, 2^k by checking if `x & (x-1) == 0`
"""
x = 4
print("Is 4 in power of 2s:", x & (x-1) == 0)
x = 8
print("Is 8 in power of 2s:", x & (x-1) == 0)
x = 6
print("Is 6 in power of 2s:", x & (x-1) == 0)


"""
To check if ith bit is set, we can `&` it with 2**i since powers of 2 have only one bit set.
If the result is non-zero then the ith bit is set
"""
n = 20 # (10100) in binary
print("Is the 2nd bit in 20 set?", (n & (1 << 2)) != 0)


def possibleSubsets(arr, length):
    for i in range(1<<length):
        for j in range(length):
            if i&(1<<j):
                print(arr[j], end=" ")
        print("")


print("Possible subsets of ['a', 'b', 'c']:", end='')
possibleSubsets(["a", "b", "c"], 3)
print("Possible subsets of [1, 2, 3, 4, 5]:", end='')
possibleSubsets([1, 2, 3,  4, 5], 5)



def CountSetBits(n):
    count = 0
    while n:
        n = n&(n-1)  # x-1 flips the rightmost 1 and the bits right to it
        count += 1
    return count


print("Set bits in 4", CountSetBits(4))
print("Set bits in 10:", CountSetBits(10))
