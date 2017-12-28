for _ in range(int(input())):
    catA, catB, mouseC = map(int, input().split())
    distA = abs(catA - mouseC)
    distB = abs(catB - mouseC)

    if distA < distB:
        print("Cat A")
    elif distB < distA:
        print("Cat B")
    else:
        print("Mouse C")

