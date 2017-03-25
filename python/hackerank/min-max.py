numlist = list(map(int, input().strip().split()))  # Gets froms stdin, splits all the number by whitespces and converts to a list

if [numlist[0],]*5 == numlist:
    """
    Edge case: When all the elements are equal
    Then min and max is same and is equal to the sum of all the elements in the list - the value of one element
    """
    f = sum(numlist[0:-1])
    print(f, f)

else:
    sum_store = []
    for n in numlist:
        x = 0
        for k in numlist:
            if k != n:
                x += k
        sum_store.append(x)

    print(min(sum_store), max(sum_store))
