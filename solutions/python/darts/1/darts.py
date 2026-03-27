def score(x, y):
    outer_circle_sqr = 10 ** 2
    middle_circle_sqr = 5 ** 2
    inner_circle_sqr = 1 ** 2
    distance = (abs(0 - x) ** 2) + (abs(0 - y) ** 2)
    print(distance)
    print(f"Outer: {outer_circle_sqr ** 2}, Middle: {middle_circle_sqr ** 2}, Inner: {inner_circle_sqr ** 2}")

    if middle_circle_sqr < distance <= outer_circle_sqr:
        return 1
    elif inner_circle_sqr < distance <= middle_circle_sqr:
        return 5
    elif distance <= inner_circle_sqr:
        return 10
    else:
        return 0