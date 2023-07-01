side_by_player = {}
player_by_side = {}
command = input()

while command != "Lumpawaroo":
    if "|" in command:
        force_side, force_user = command.split(" | ")
        if force_side not in player_by_side:
            player_by_side[force_side] = []
        if force_user not in side_by_player:
            side_by_player[force_user]= force_side
            player_by_side[force_side].append(force_user)

    else:
        force_user, force_side = command.split(" -> ")
        if force_side not in player_by_side:
            player_by_side[force_side] = []
        player_by_side[force_side].append(force_user)
        if force_user in side_by_player:
            old_side = side_by_player[force_user]
            player_by_side[old_side].remove(force_user)
            side_by_player[force_user] = force_side
        else:
            side_by_player[force_user] = force_side
        print(f"{force_user} joins the {force_side} side!")
    command = input()

for side, users in player_by_side.items():
    if len(users) > 0:
        print(f"Side: {side}, Members: {len(users)}")
        for user in users:
            print(f"! {user}")
