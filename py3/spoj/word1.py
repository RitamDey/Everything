cases=int(input())
for a in range(cases):
    l=list()
    s=int(input())
    for b in range(s):
        doors=input()
        d=len(doors)-1
        l[b]=doors[d]
    state=True
    for b in range(s):
        if l[b]==l[b+1]:
            state=True
        else:
            state=False
    if state:
        print("Ordering is possible")
    else:
        print("The door cannot be opened.")
