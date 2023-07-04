def get_sorted(item):
    return -item[1], item[0]


command = input()
players = {}

while command != "Season end":
    if "->" in command:
        player, position, skill = command.split(" -> ")
        skill = int(skill)
        players.setdefault(player, {}).setdefault(position, 0)
        if players[player][position] < skill:
            players[player][position] = skill
    elif " vs " in command:
        first_side, second_side = command.split(" vs ")
        if first_side in players and second_side in players:
            # matching_position = None
            # for position in players[first_side]:
            #     if position in players[second_side]:
            #         matching_position = position
            #         break
            matching_position = [position for position in players[first_side] if position in players[second_side]]
            if matching_position:
                if players[first_side][matching_position[0]] > players[second_side][matching_position[0]]:
                    del players[second_side]
                else:
                    del players[first_side]
    command = input()

sum_skills = {player: sum(positions.values()) for player, positions in players.items()}

if sum_skills:
    for player, total_sum in sorted(sum_skills.items(), key=get_sorted):
        print(f"{player}: {total_sum} skill")
        if player in players:
            player_positions = players[player]
            for position, skill in sorted(player_positions.items(), key=get_sorted):
                print(f"- {position} <::> {skill}")
