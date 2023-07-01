counter = 0
event = input()

while event != "END":
    if event == "coding" or event == "dog" or event == "cat" or event == "movie":
        counter += 1
    elif event == "CODING" or event == "DOG" or event == "CAT" or event == "MOVIE":
        counter += 2
    event = input()

if counter > 5:
    print("You need extra sleep")
else:
    print(counter)