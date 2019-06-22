def hypothesis(x, y, label_x) -> list:
    """
    Hypothesis function h(x) is defined as,
    h(x) = θ1 + θ2*x
    """
    return x + (y * label_x)



def cost_function(data, x, y) -> float:
    """
    Cost function J is defined as,
    J(θ1, θ2) = (1/2m) * (∑ sum of (h(x) - y)^2)

    m = the number of x, y pairs we have
    x = θ1
    y = θ2

    In ML, the target is to reduce the cost function by findinf paramters θ1, θ2
    A cost of  means perfect data
    """
    m = len(data)

    summation = 0
    for dx, dy in data:
        summation += (hypothesis(x, y, dx) - dy) ** 2

    return (1 / (2*m)) * summation


if __name__ == '__main__':
    data = [[2, 1], [2, 4], [5, 4], [5, 8], [9, 8], [9, 11]]
    print(round(cost_function(data, 1, 1), 3))

