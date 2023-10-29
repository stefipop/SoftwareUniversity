from typing import Dict


class Player:
    def __init__(self, name: str, hp: int, mp: int):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills: Dict[str: int] = {}
        self.guild = "Unaffiliated"

    def add_skill(self, skill_name: str, mana_cost: int) -> str:
        if skill_name in self.skills:
            return "Skill already added"

        self.skills[skill_name] = mana_cost
        return f"Skill {skill_name} added to the collection of the player {self.name}"

    def player_info(self) -> str:
        result = ([f"Name: {self.name}", f"Guild: {self.guild}", f"HP: {self.hp}", f"MP: {self.mp}"] +
                  [f"==={s} - {m}" for s, m in self.skills.items()])

        return "\n".join(result)
