'''from re import match'''
s=input().split(":")
if match(".*PM",s[2]):
    if match("12",s[0]):
      print("%s:%s:%s" % (s[0],s[1], s[2][0:2:]))
    else:
      print("%i:%s:%s" % (int(s[0]) + 12, s[1], s[2][0:2:]))
elif match("12",s[0]) and match(".*AM",s[2]):
    print("00:%s:%s" % (s[1], s[2][0:2:]))
else:
    print("%s:%s:%s" % (s[0],s[1], s[2][0:2:]))
