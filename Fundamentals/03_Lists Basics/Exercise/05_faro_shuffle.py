# def faro_shuffle(deck):
#     half = len(deck) // 2
#     left_half = deck[:half]
#     right_half = deck[half:]
#     shuffle_deck = []
#     for i in range(half):
#         shuffle_deck.append(left_half[i])
#         shuffle_deck.append(right_half[i])
#     return shuffle_deck
#
#
# def perform_faro_shuffles(deck, num_shuffles):
#     for _ in range(num_shuffles):
#         deck = faro_shuffle(deck)
#     return deck
#
#
# elements = input().split()
# shuffles = int(input())
#
# shuffled_deck = perform_faro_shuffles(elements, shuffles)
#
# print(shuffled_deck)


cards = input().split()
n = int(input())
half_size = len(cards) // 2
for i in range(n):
    left_side = cards[:half_size]
    right_size = cards[half_size:]
    faro_cards = []
    for j in range(len(left_side)):
        faro_cards.append(left_side[j])
        faro_cards.append((right_size[j]))
    cards = faro_cards
print(cards)


# for _ in range(n):
#     first_half = []
#     second_half = []
#     for idx in range(1, len(cards) - 1):
#         card = cards[idx]
#         if idx < len(cards) / 2:
#             first_half.append(card)
#         else:
#             second_half.append(card)
#
#     shuffled = []
#     first_half_j = 0
#     second_half_j = 0
#     for j in range(len(first_half) * 2):
#         if j % 2 == 0:
#             shuffled.append(second_half[second_half_j])
#             second_half_j += 1
#         else:
#             shuffled.append(first_half[first_half_j])
#             first_half_j += 1
#     cards = [cards[0]] + shuffled + [cards[-1]]
# print(cards)
