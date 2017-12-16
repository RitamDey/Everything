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

