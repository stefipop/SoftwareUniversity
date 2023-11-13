from typing import Dict

from project.formula_teams.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):
    @property
    def sponsors(self) -> Dict[str, Dict[int, int]]:
        return {
            "Petronas": {1: 1000000, 3: 500000},
            "TeamViewer": {5: 100000, 7: 50000},
        }

    @property
    def expenses(self) -> int:
        return 200000
