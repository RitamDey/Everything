"""
  * If the starting number is x and the delta between elements is d,
  * Then series is
  * (x+0*d) (x+1*d) (x+2*d) ... (x+n*d)
  * Now if target t the number is present then it can be is present 
  * can be found:
  * 
  * (t-x)%d should equate to 0
  * Though we must check that if target is greater than start 
  * while delta is negetive, then the target shall never be achieved.
"""
start, target, delta = map(int, input().split())


if target > start and delta < 0:
    print("NO")
elif (target-start)%delta == 0:
    print("YES")
else:
    print("NO")

