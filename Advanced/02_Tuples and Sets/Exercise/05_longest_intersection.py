n = int(input())
longest_data = set()

for i in range(n):
    start, end = input().split("-")
    first_st, first_end = (int(x) for x in start.split(","))
    second_st, second_end = (int(x) for x in end.split(","))

    first_set = set(range(first_st, first_end + 1))
    second_set = set(range(second_st, second_end + 1))

    intersection = first_set & second_set

    if len(intersection) > len(longest_data):
        longest_data = intersection

print(f"Longest intersection is {list(longest_data)} with length {len(longest_data)}")
