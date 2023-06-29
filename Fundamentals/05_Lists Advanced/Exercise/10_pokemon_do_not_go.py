distances = [int(x) for x in input().split()]
sum_elements = 0
del_element = 0

while distances:
    index = int(input())
    if index in range(0, len(distances)):
        del_element = distances[index]
        distances.pop(index)
    elif index < 0:
        del_element = distances[0]
        distances[0] = distances[-1]
    else:
        del_element = distances[-1]
        distances[-1] = distances[0]

    sum_elements += del_element

    for dist in range(len(distances)):
        if distances[dist] <= del_element:
            distances[dist] += del_element
        else:
            distances[dist] -= del_element

print(sum_elements)
