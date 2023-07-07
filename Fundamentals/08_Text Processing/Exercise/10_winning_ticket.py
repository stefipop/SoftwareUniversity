def check_ticket(ticket):
    if len(ticket) != 20:
        return "invalid ticket"
    winning_symbols = ["@", "#", "$", "^"]
    left_part = ticket[:10]
    right_part = ticket[10:]
    for match in winning_symbols:
        for i in range(10, 5, -1):
            winning_symbols_repete = match * i
            if winning_symbols_repete in left_part and winning_symbols_repete in right_part:
                if i == 10:
                    return f'ticket "{ticket}" - {i}{match} Jackpot!'
                return f'ticket "{ticket}" - {i}{match}'
    return f'ticket "{ticket}" - no match'


tickets = [ticket.strip() for ticket in input().split(", ")]

for ticket in tickets:
    print(check_ticket(ticket))
