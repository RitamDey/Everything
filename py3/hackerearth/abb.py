hate=list()
final=str()
for a in range(int(input())):
 hate+=input().split()
line=input()
line=input().split()
for a in line:
 if a not in hate:
  final+=a[0].upper()+"."
print("%s" %final,end="\b")
