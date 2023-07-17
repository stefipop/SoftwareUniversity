import re

text = input()
result = re.split(r'[,\s]+', text)
name_regex = re.compile(r"[^0-9+\-*/\.]")
num_regex = re.compile(r"[-+]?[0-9]+\.?\d*")
pattern_operator = r"[*\/]"

for demon in sorted(result):
    match_name = re.findall(name_regex, demon)
    health = sum(ord(match) for match in match_name)

    match_num = re.findall(num_regex, demon)
    damage = sum(float(match) for match in match_num)
    operator = re.findall(pattern_operator, demon)
    for op in operator:
        if '*' in op:
            damage *= 2
        elif '/' in op:
            damage /= 2
    print(f"{demon} - {health} health, {damage:.2f} damage")
