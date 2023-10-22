from collections import defaultdict


def team_lineup(*args):
    # Create a dictionary
    football_players = defaultdict(list)
    # Organize players by country.
    for player, country in args:
        football_players[country].append(player)

    # Sort the dictionary by the number of players per country (descending).
    sorted_dict = dict(sorted(football_players.items(), key=lambda x: (-len(x[1]), x[0])))

    result = []
    # Generate the output in the desired format.
    for country, players in sorted_dict.items():
        result.append(f"{country}:")
        for player_ in players:
            result.append(f"  -{player_}")

    return "\n".join(result)


# print(team_lineup(
#    ("Harry Kane", "England"),
#    ("Manuel Neuer", "Germany"),
#    ("Raheem Sterling", "England"),
#    ("Toni Kroos", "Germany"),
#    ("Cristiano Ronaldo", "Portugal"),
#    ("Thomas Muller", "Germany")))

print(team_lineup(
   ("Lionel Messi", "Argentina"),
   ("Neymar", "Brazil"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Harry Kane", "England"),
   ("Kylian Mbappe", "France"),
   ("Raheem Sterling", "England")))
#
# print(team_lineup(
#    ("Harry Kane", "England"),
#    ("Manuel Neuer", "Germany"),
#    ("Raheem Sterling", "England"),
#    ("Toni Kroos", "Germany"),
#    ("Cristiano Ronaldo", "Portugal"),
#    ("Thomas Muller", "Germany"),
#    ("Bruno Fernandes", "Portugal"),
#    ("Bernardo Silva", "Portugal"),
#    ("Harry Maguire", "England")))

