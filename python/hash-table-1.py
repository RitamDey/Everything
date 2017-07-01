from collections import deque


class HashFunction:
    def __init__(self, length: int):
        self.arr = deque(["-1" for _ in range(length)], maxlen=length)
        self.len = length
        self.items = 0

    def hash1(self, strings_array: list, thearr: list) -> None:
        for n in range(len(strings_array)):
            newelem = strings_array[n]

            thearr[int(newelem)] = newelem

    def hash2(self, strings_array: list, thearr: list) -> None:
        for n in range(len(strings_array)):
            newelem = strings_array[n]

            index = int(newelem) % 29
            print(f"Modulus Index={index}")

            while thearr[index] != "-1":
                index += 1
                print(f"Collision. Trying Index={index}")
                index %= self.len

            thearr[index] = newelem

    def findkey(self, key: str) -> str:
        index = int(key) % 29

        while self.arr[index] != "-1":
            if self.arr[index] == key:
                print("{0} was found in index {1}".format(key, index))
                return self.arr[index]

            index += 1
            index %= self.len

        return None


def main():
    func = HashFunction(30)

    # elementsToAdd = ["1", "5", "17", "21", "26"]
    # func.hash1(elementsToAdd, func.arr)

    elementsToAdd2 = [
        "100", "510", "170", "214", "268", "398",
        "235", "802", "900", "723", "699", "1", "16", "999", "890",
        "725", "998", "978", "988", "990", "989", "984", "320", "321",
        "400", "415", "450", "50", "660", "624"
    ]

    func.hash2(elementsToAdd2, func.arr)
    print(func.arr)

    func.findkey("660")


if __name__ == '__main__':
    main()
