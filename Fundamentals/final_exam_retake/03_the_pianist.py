count = int(input())
music_list = {}

for i in range(count):
    piece, composer, key = input().split("|")
    music_list[piece] = {composer: key}

command = input()

while command != "Stop":
    action, info = command.split("|", 1)

    if action == "Add":
        piece, composer, key = info.split("|")
        if piece not in music_list:
            music_list[piece] = {composer: key}
            print(f"{piece} by {composer} in {key} added to the collection!")
        else:
            print(f"{piece} is already in the collection!")

    elif action == "Remove":
        piece = info
        if piece in music_list:
            music_list.pop(piece)
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    else:
        piece, new_key = info.split("|")
        if piece in music_list:
            music_list[piece] = {composer: new_key for composer in music_list[piece]}
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    command = input()

for piece, composers in music_list.items():
    for composer, key in composers.items():
        print(f"{piece} -> Composer: {composer}, Key: {key}")
