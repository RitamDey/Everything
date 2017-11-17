from itertools import accumulate


input()


data = list(map(int, input().split()))
data_sum = sum(data)

sum_max, sum_min = None, None


for i in data:
    try:
        if data_sum-i > sum_max:
            sum_max = data_sum-i
    except:
        sum_max = data_sum-i

    try:
        if data_sum-i < sum_min:
            sum_min = data_sum-i
    except:
        sum_min = data_sum-i



print(sum_min, sum_max)
