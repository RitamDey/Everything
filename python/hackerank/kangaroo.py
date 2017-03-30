k1_x, k1_rate, k2_x, k2_rate = map(int, input().split())

if (k2_x - k1_x) >= 0 and (k2_rate - k1_rate) >= 0:
    print('NO')

elif (k1_x - k2_x) >= 0 and (k1_rate - k2_rate) >= 0:
    print('NO')

else:
    print('YES')
