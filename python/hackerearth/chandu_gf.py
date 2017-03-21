l=list()
for a in range(int(input())):
	s=input()
	l=sorted(map(int,input().split()),reverse=True)
        print(" ".join(map(str,l)))
