from re import findall
for a in range(int(input())):
 name=input()
 suvo=findall("SUVO",name)
 suvojit=findall("SUVOJIT",name)
 print("SUVO = %i SUVOJIT = %i" %(len(suvo)-len(suvojit),len(suvojit)))
