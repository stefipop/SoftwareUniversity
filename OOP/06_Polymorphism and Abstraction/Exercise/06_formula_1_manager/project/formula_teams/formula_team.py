from abc import ABC, abstractmethod
from typing import Dict


class FormulaTeam(ABC):
    def __init__(self, budget: int) -> None:
        self.budget = budget

    @property
    @abstractmethod
    def sponsors(self) -> Dict[str, Dict[int, int]]:
        ...

    @property
    @abstractmethod
    def expenses(self) -> int:
        ...

    @property
    def budget(self):
        return self.__budget

    @budget.setter
    def budget(self, value):
        if value < 1000000:
            raise ValueError("F1 is an expensive sport, find more sponsors!")

        self.__budget = value

    def calculate_revenue_after_race(self, race_pos: int) -> str:
        revenue = 0
        revenue -= self.expenses

        for positions in self.sponsors.values():
            for pos in positions:
                if race_pos <= pos:
                    revenue += positions[pos]
                    break

        self.budget += revenue
        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"
