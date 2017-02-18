list=list()

for a in range(int(input())):
 s=input().split()
 if "append" in s:
  list.append(int(s[1]))
 elif "insert" in s:
  list.insert(int(s[1]),int(s[2]))
 elif "remove" in s:
  list.remove(int(s[1]))
 elif "pop" in s[0]:
  list.pop();
 elif "index" in s:
  list.index(int(s[1]))
 elif "count" in s:
  list.count(int(s[1]));
 elif "sort" in s:
  list.sort()
 elif "reverse" in s:
  list.reverse()
 else:
  print(list)


