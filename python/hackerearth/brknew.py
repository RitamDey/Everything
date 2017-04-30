dg=0
db=0
for a in range(int(input())):
    s=input().split()
    if "19" in s and "21" in s:
        dg+=4
        db+=3
    elif "19" in s:
        dg+=4
    elif "21" in s:
        db+=3
if dg > db:
    print("Date")
else:
    print("No Date")
