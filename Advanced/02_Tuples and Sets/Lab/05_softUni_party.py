n = int(input())

reservation = set()

for _ in range(n):
    rev_number = input()
    reservation.add(rev_number)

guest = input()

while guest != "END":
    reservation.remove(guest)
    guest = input()

print(len(reservation))

for num in sorted(reservation):
    print(num)
