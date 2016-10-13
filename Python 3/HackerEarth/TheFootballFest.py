for _ in range(int(input())):
    tests, pid = input().split()
    pid = [pid]
    for _ in range(int(tests)):
    	this_pass = input().split()
    	if this_pass[0] == 'P':
    		pid.append(this_pass[1])
    	else:
    		pid.append(pid[-2])
    print("Player", pid[-1])
