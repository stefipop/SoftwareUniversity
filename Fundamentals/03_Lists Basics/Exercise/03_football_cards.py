team_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
team_b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
cards_input = input().split()
is_break = False

for card in cards_input:
    card_info = card.split("-")
    team_name = card_info[0]
    player = int(card_info[1])

    if team_name == 'A' and player in team_a:
        team_a.remove(player)
    elif team_name == 'B' and player in team_b:
        team_b.remove(player)
    if len(team_a) < 7 or len(team_b) < 7:
        is_break = True
        break
print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
if is_break:
    print(f"Game was terminated")

# cards_list = input().split(" ")
# team_a_players = 11
# team_b_players = 11
# cards_list = set(cards_list)
# is_terminated = False
# for card in cards_list:
#     if "A" in card:
#         team_a_players -= 1
#     elif "B" in card:
#         team_b_players -= 1
#     if team_a_players < 7 or team_b_players < 7:
#         is_terminated = True
#         break
#
# print(f"Team A - {team_a_players}; Team B - {team_b_players}")
# if is_terminated:
#     print("Game was terminated")

# team_a = ['A-1', 'A-2', 'A-3', 'A-4', 'A-5', 'A-6', 'A-7', 'A-8', 'A-9', 'A-10', 'A-11']
# team_b = ['B-1', 'B-2', 'B-3', 'B-4', 'B-5', 'B-6', 'B-7', 'B-8', 'B-9', 'B-10', 'B-11']
# players_sent_off = input().split()
# game_was_terminated = False
# for player in players_sent_off:
#     if player in team_a:
#         team_a.remove(player)
#     elif player in team_b:
#         team_b.remove(player)
#     if len(team_a) < 7 or len(team_b) <7:
#         game_was_terminated = True
#         break
# print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
# if game_was_terminated:  # if game_was_terminated == True:
#     print("Game was terminated")
