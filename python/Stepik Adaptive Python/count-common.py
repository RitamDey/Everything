from collections import Counter


in_file = open('/home/stux/Downloads/dataset_28252_1.txt')


for line in in_file:
    line = line.lower().split()
    count = Counter(line)

    print(*count.most_common(1))

