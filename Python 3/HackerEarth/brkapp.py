d19=0
d21=0
for a in range(int(input())):
    s=input()
    d19+=s.count("19")*4
    d19+=s.count("20")*4
    d21+=s.count("21")*3
if d19 > d21:
    print("Date")
else:
    print("No Date")
