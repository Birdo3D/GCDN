def minimum(l: list) -> (int, int):
    ind = 0
    elt = l[0]
    for i in range(len(l)):
        if l[i] < ind:
            ind = i
            elt = l[i]
    return ind, elt


def maximum(l: list) -> (int, int):
    ind = 0
    elt = l[0]
    for i in range(len(l)):
        if l[i] > ind:
            ind = i
            elt = l[i]
    return ind, elt
