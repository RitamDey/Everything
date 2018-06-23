def sort(arr, length):
    for i in range(1, length):
        key = arr[i]
        j = i

        while j > 0 and arr[j-1] > key:
            arr[j] = arr[j-1]
            j -= 1

        arr[j] = key

    return arr


def main():
    input()
    zombies = []
    zombies_length = 0
    zombies_sum = 0

    vampires = []
    vampires_length = 0
    vampires_sum = 0

    for i in map(int, input().split()):
        if i%2:
            vampires_length += 1
            vampires_sum += i
            vampires.append(i)
        else:
            zombies_length += 1
            zombies_sum += i
            zombies.append(i)

    print(*sort(zombies, zombies_length), zombies_sum, end=" ")
    print(*sort(vampires, vampires_length), vampires_sum)

if __name__ == '__main__':
    main()