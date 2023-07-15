count = int(input())
dragons = {}
av_per_type = {}
av_damage, av_health, av_armor = 0, 0, 0

for _ in range(count):
    color, name, damage, health, armor = input().split()
    damage = int(damage) if damage != "null" else 45
    health = int(health) if health != "null" else 250
    armor  = int(armor) if armor != "null" else 10
    dragons.setdefault(color, {})
    dragons[color][name] = (damage, health, armor)

for k, v in dragons.items():
    for name, values in v.items():
        av_damage += values[0] / len(v)
        av_health += values[1] / len(v)
        av_armor += values[2] / len(v)
    av_per_type[k] = (av_damage, av_health, av_armor)
    av_damage, av_health, av_armor = 0, 0, 0

for key, value in av_per_type.items():
    print(f"{key}::({value[0]:.2f}/{value[1]:.2f}/{value[2]:.2f})")
    sorted_names = sorted(dragons[key].items(), key=lambda x: x[0])
    for name, pairs in sorted_names:
        print(f"-{name} -> damage: {pairs[0]}, health: {pairs[1]}, armor: {pairs[2]}")
