'''
My Question: http://codereview.stackexchange.com/questions/141516/where-is-it-slow

His Explanation:
Try tracking the current maximum, otherwise frequent occurrences of 3 will push your run time towards O(n²).

If you take a closer look at what your input actually means, you will notice that smaller values being pushed onto the stack have actually no significance if a greater value has being pushed previously. So for every fill level of the stack, you already know the corresponding maximum at the time you push onto the stack.
By storing the maximum instead of the raw value on the stack, you can always access the current maximum directly. Just don't forget to handle the special case when data is empty, so the new value will always be the maximum.

His Answer In Code:
'''
data = []
for _ in range(int(input())):
    ins = input().split()
    if ins[0] == '1':
        new_value = int(ins[1])
        if data and new_value < data[-1]:
            new_value = data[-1]
        data.append(new_value)
    elif ins[0] == '2':
        data.pop()
    elif ins[0] == '3':
        print(data[-1])
