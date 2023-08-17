gift_list = input().split()
while True:
    command = input().split()
    to_do = command[0]
    gift = command[1]

    if to_do == "OutOfStock":
        for i in range(len(gift_list)):
            if gift_list[i] == gift:
                gift_list[i] = "None"
    elif to_do == "Required":
        idx = int(command[2])
        if 0 <= idx < len(gift_list):
            gift_list[idx] = gift
    elif to_do == "JustInCase":
        gift_list[-1] = gift
    else:
        break

for gift in gift_list:
    if gift == "None":
        continue
    print(gift, end=' ')
