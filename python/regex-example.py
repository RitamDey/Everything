from re import findall


string = "I am sTux, Born April 7th 2005"


for regex in [r"[0-9]", r"[0-9]+", r"[a-z]", r"[A-Z]", r"[a-z]+", r"[A-Z]+", r"[a-zA-z]", r"[a-zA-Z]+",r"[a-zA-Z0-9]", r"[a-zA-Z0-9]+"]:
    print(f"Launching regex {regex}")
    print(f"Found {findall(string=string, pattern=regex)} from {string}")

