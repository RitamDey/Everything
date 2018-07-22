for _ in range(int(input())):
    n_buildings, r = map(int, input().split())
    buildings = list(map(int, input().split()))
    last_building_height = buildings[0]

    count = 1

    for i in range(1, n_buildings):
        if buildings[i] > last_building_height:
            count += 1
            last_building_height = buildings[i]

    print(r * count)

