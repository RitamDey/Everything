l=list()
for a in range(int(input())):
	s=input()
	s=map(int,input().split())
	for a in s:
		l.append(a)
	l.sort(reverse=True)
	print(l[0],end="")
	for a in l[1:]:
		print(" %d" %(a),end="")
	l=[]
	print()
