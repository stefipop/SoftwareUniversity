import re

lines = int(input())
attacked_planet, destroyed_planet = [], []
pattern = re.compile(r"@(?P<planet>[A-Z][a-z]+)([^@\-!:>]*)"
                     r":(?P<population>\d+)([^@\-!:>]*)"
                     r"!(?P<attack>[AD])!([^@\-!:>]*)"
                     r"->(?P<soldiers>\d+)")

for _ in range(lines):
    text = input()
    counter = sum(text.lower().count(char) for char in "star")
    new_message = "".join(chr(ord(char) - counter) for char in text)
    matches = re.finditer(pattern, new_message)
    for match in matches:
        planet = match.group('planet')
        attack = match.group('attack')
        if attack == 'A':
            attacked_planet.append(planet)
        elif attack == 'D':
            destroyed_planet.append(planet)

print(f"Attacked planets: {len(attacked_planet)}")
for planet in sorted(attacked_planet):
    print(f"-> {planet}")
print(f"Destroyed planets: {len(destroyed_planet)}")
for planet in sorted(destroyed_planet):
    print(f"-> {planet}")
