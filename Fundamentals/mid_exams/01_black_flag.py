days = int(input())
daily_plunder  = int(input())
expected_plunder = float(input())
total = 0

for day in range(1, days + 1):
    total += daily_plunder
    if day % 3 == 0:
        total += daily_plunder * 0.5
    if day % 5 == 0:
        total -= total * 0.3
if total >= expected_plunder:
    print(f"Ahoy! {total:.2f} plunder gained.")
else:
    percentage = total * 100 / expected_plunder
    print(f"Collected only {percentage:.2f}% of the plunder.")
