for a in range(int(input())):
	l=input()
	l=list(map(int,input().split()))
	l+=map(int,input().split())
	l=sorted(l,reverse=True) 
	print(" ".join(map(str,l)))
