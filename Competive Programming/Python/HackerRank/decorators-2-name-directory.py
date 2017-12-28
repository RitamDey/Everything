def person_lister(f):
    def inner(people):
        x = []
        people.sort(key=lambda elem: elem[2])

        for p in people:
            x.append(f(p))
        return x
    return inner


@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]


if __name__ == '__main__':
    people = [input() for i in range(int(input()))]
    print(*name_format(people), sep='\n')

