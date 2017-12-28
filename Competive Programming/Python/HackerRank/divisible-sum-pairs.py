def count_pairs(nums, length, div):
    pair_count = 0

    for i in range(length):
        for j in range(i, length):
            if (nums[i]+nums[j])%div == 0 and i < j:
                #print(i,j)
                pair_count += 1

    return pair_count


if __name__ == '__main__':
    length, sums = map(int, input().split())
    arr = list(map(int, input().split()))

    print(count_pairs(arr, length, sums))

