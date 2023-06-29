# def merging(element, initial, last):
#     merge_result = ''
#     for i in range(initial, last + 1):
#         merge_result += element[i]
#     return merge_result


data_list = input().split()
user_input = input()

while user_input != "3:1":
    command, start, end = user_input.split()
    if command == "merge":
        start_index = max(0, int(start))
        end_index = min(len(data_list) - 1, int(end))
        # united_el = merging(data_list, start_index, end_index)
        remove_count = end_index - start_index + 1
        removed_els = []
        for _ in range(remove_count):
            el = data_list.pop(start_index)
            removed_els.append(el)
        data_list.insert(start_index, ''.join(removed_els))
    elif command == "divide":
        index = int(start)
        partitions = int(end)
        element = data_list[index]
        partition_size = len(element) // partitions
        element_parts = []
        current_partition = ''
        for idx in range((partitions - 1) * partition_size):
            current_partition += element[idx]
            if len(current_partition) == partition_size:
                element_parts.append(current_partition)
                current_partition = ''
        current_partition = ''
        for idx in range((partitions - 1) * partition_size, len(element)):
            current_partition += element[idx]
        element_parts.append(current_partition)
        data_list.pop(index)
        for idx in range(len(element_parts)):
            data_list.insert(index + idx, element_parts[idx])
    user_input = input()

print(' '.join(data_list))