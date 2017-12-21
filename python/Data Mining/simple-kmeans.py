def kMeans(data, k):
    names = sorted(data, key=lambda key: data[key]['distance'], reverse=True)[:k]
    k_sum = 0
    for n in names:
        k_sum += data[n]['distance']
    k_influence = [round(data[i]['distance']/k_sum, 4) for i in names]
    projection = 0

    for i in range(k):
        projection += data[names[i]]['rating']*k_influence[i]

    return projection


if __name__ == '__main__':
    data = {
            'Sally': {
                        'distance': 0.8,
                        'rating': 3.5
                     },
            'Eric': {
                        'distance': 0.7,
                        'rating': 5
                    },
            'Amanda': {
                        'distance': 0.5,
                        'rating': 4.5
                      }
            }
    print("%.1f" %kMeans(data, 2))

