iter_num = 0

def fib(num):
    global iter_num
    iter_num += 1
    print("Iteration number {0}. num = {1}".format(iter_num, num))

    # Base class for fibonnaci series
    if num==0 or num==1:
        return 1
    # Recursive call
    else:
        return fib(num-1)+fib(num-2)


if __name__ == '__main__':
    num = int(input("Enter a number: "))
    ans = fib(num)
    print("Fibonnaci sum of the number is ", ans)

