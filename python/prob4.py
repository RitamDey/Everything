"""
Solution for ProjectEular problem https://projecteuler.net/problem=4
Note: Multiply and selecting the first pallindrom product is not the right
      answer
      Run this code to get the the answer

      for x in range(999, 99, -1):
          for y in range(999, 99, -1):
              f =x*y
              if is_palin(f):
                  print("{0}*{1}={2}".format(x, y, f))
                  if f == 906609:
                      exit()
    The output will give you the answer
"""
def is_palin(n):
    return str(n) == str(n)[::-1]


max_palin = 0
for x in range(999, 99, -1):
    for y in range(999, 99, -1):
        f = x*y
        if f > max_palin and is_palin(f):
            max_palin = f
print(max_palin)
