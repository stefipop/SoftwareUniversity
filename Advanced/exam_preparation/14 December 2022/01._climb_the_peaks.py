from collections import deque

WEEK = 7
portions = [int(el) for el in input().split(", ")]
stamina = deque(int(el) for el in input().split(", "))
conquered_peaks = []

peaks = deque([
    ("Vihren", 80),
    ("Kutelo", 90),
    ("Banski Suhodol", 100),
    ("Polezhan", 60),
    ("Kamenitza", 70)
])

for _ in range(WEEK):
    portion  = portions.pop()
    daily_stamina = stamina.popleft()
    result = portion + daily_stamina
    if peaks:
        current_peak = peaks.popleft()

        if result >= current_peak[1]:
            conquered_peaks.append(current_peak[0])
        else:
            peaks.appendleft(current_peak)

if not peaks:
    print(f"Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")

if conquered_peaks:
    print(f"Conquered peaks:")
    print('\n'.join(conquered_peaks))
