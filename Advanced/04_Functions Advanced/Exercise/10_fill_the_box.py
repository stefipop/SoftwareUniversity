def fill_the_box(*args):
    height, length, width, *volumes = args
    volume = height * length * width
    sum_volumes = 0

    # for idx in range(len(volumes)):
    #     if volumes[idx] == "Finish":
    #         break
    #     sum_volumes += volumes[idx]
    # for item in volumes:
    #     if item == "Finish":
    #         break
    #     sum_volumes += item
    idx = 0

    while idx < len(volumes) and volumes[idx] != "Finish":
        sum_volumes += volumes[idx]
        idx += 1

    if volume > sum_volumes:
        return f"There is free space in the box. You could put {volume - sum_volumes} more cubes."
    return f"No more free space! You have {sum_volumes - volume} more cubes."


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))