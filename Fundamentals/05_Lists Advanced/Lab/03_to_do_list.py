# to_do_list = [0] * 10
# command = input()
#
# while command != "End":
#     importance, task = command.split('-')
#     importance = int(importance)
#     index = importance - 1
#     to_do_list[index] = task
#     command = input()
# print([task for task in to_do_list if task != 0])

# my decision
to_do_list = []

command = input()

while command != "End":
    importance, task = command.split('-')
    importance = int(importance)
    to_do_list.append((importance, task))
    command = input()

to_do_list.sort()

result_list = [task for _, task in to_do_list]
print(result_list)


# def process_todo_notes():
#     todo_notes = []
#     while True:
#         note = input()
#         if note == "End":
#             break
#         todo_notes.append(note)
#     sorted_notes = sorted(todo_notes, key=lambda x: int(x.split('-')[0]))
#     result_sorted_notes = [note.split('-')[1] for note in sorted_notes]
#     return result_sorted_notes
#
#
# result = process_todo_notes()
# print(result)