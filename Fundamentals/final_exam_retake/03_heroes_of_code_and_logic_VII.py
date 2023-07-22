def cast_spell(hero_dict, split_command):
    hero_name, mana, spell_name = split_command.split(" - ")
    mana = int(mana)
    if hero_dict[hero_name]["mana"] >= mana:
        hero_dict[hero_name]["mana"] -= mana
        print(f"{hero_name} has successfully cast {spell_name} and now has {hero_dict[hero_name]['mana']} MP!")
    else:
        print(f"{hero_name} does not have enough MP to cast {spell_name}!")
    return hero_dict


def take_damage(hero_dict, split_command):
    hero_name, damage, attacker = split_command.split(" - ")
    hero_dict[hero_name]["HP"] -= int(damage)
    if hero_dict[hero_name]["HP"] > 0:
        print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {hero_dict[hero_name]['HP']} HP left!")
    else:
        print(f"{hero_name} has been killed by {attacker}!")
        del hero_dict[hero_name]
    return hero_dict


def recharge(hero_dict, split_command):
    hero_name, amount = split_command.split(" - ")
    recovered = min(int(amount), MAX_MP - hero_dict[hero_name]["mana"])
    hero_dict[hero_name]["mana"] += recovered
    print(f"{hero_name} recharged for {recovered} MP!")
    return hero_dict


def heal(hero_dict, split_command):
    hero_name, amount = split_command.split(" - ")
    recovered = min(int(amount), MAX_HP - hero_dict[hero_name]["HP"])
    hero_dict[hero_name]["HP"] += recovered
    print(f"{hero_name} healed for {recovered} HP!")
    return hero_dict


MAX_HP = 100
MAX_MP = 200
nums = int(input())
heroes = {}

for _ in range(nums):
    name, hit_points, mana_points = input().split()
    heroes[name] = {"HP": int(hit_points), "mana": int(mana_points)}

command = input()

while command != "End":
    action, info = command.split(" - ", 1)
    if action == "CastSpell":
        heroes = cast_spell(heroes, info)
    elif action == "TakeDamage":
        heroes = take_damage(heroes, info)
    elif action == "Recharge":
        heroes = recharge(heroes, info)
    else:
        heroes = heal(heroes, info)
    command = input()

for name, values in heroes.items():
    print(name)
    print(f"  HP: {values['HP']}")
    print(f"  MP: {values['mana']}")
