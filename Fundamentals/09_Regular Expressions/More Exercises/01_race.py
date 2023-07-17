import re

participants = input().split(", ")
name_list = dict.fromkeys(participants, 0)
text = input()
distance = 0

while text != "end of race":
    pattern = r"\d"
    distance = sum(int(x) for x in ((re.findall(pattern, text))))
    pattern1 = r"\W+|\d*"
    text = re.sub(pattern1, '', text)
    if text in participants:
        name_list[text] += distance
    text = input()
    distance = 0

sorted_dict = sorted(name_list.items(), key=lambda x: -x[1])
rank = ['1st', '2nd', '3rd']
for i in range(len(rank)):
    print(f"{rank[i]} place: {sorted_dict[i][0]}")
