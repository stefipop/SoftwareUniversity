from collections import deque
# Input
initial_fuel = deque(int(el) for el in input().split())
consumption = deque(int(el) for el in input().split())
necessary_fuel = deque(int(el) for el in input().split())
reached_altitudes = []

# Iterate over the queues
idx = 0
while initial_fuel and consumption and necessary_fuel:
    current_fuel = initial_fuel[-1]
    current_consumption = consumption[0]
    idx += 1
    result = current_fuel - current_consumption
    if result >= necessary_fuel[0]:
        necessary_fuel.popleft()
        initial_fuel.pop()
        consumption.popleft()
        reached_altitudes.append(f"Altitude {idx}")
        print(f"John has reached: Altitude {idx}")
    else:
        print(f"John did not reach: Altitude {idx}")
        break

# Check and print the result
if reached_altitudes and necessary_fuel:
    print(f"John failed to reach the top.\nReached altitudes: {', '.join(reached_altitudes)}")
if not reached_altitudes:
    print("John failed to reach the top.\nJohn didn't reach any altitude.")
if not necessary_fuel:
    print("John has reached all the altitudes and managed to reach the top!")
