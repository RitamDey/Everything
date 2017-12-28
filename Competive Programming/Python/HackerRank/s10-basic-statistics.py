length = int(input())
arr = sorted(map(int, input().split()))


print("%.1f" %(sum(arr)/length))
if length%2:
    print("%.1f" %(arr[length//2]))
else:
    print("%.1f" %((arr[(length//2)-1]+arr[length//2])/2))


count_arr = [(i, arr.count(i)) for i in arr]
print(max(count_arr, key=lambda x: x[1])[0])
