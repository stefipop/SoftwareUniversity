class Equipment:
    id = 1

    def __init__(self, name: str) -> None:
        self.id = Equipment.get_next_id()
        self.name = name

    @staticmethod
    def get_next_id() -> int:
        current_id = Equipment.id
        Equipment.id += 1
        return current_id

    def __repr__(self) -> str:
        return f"Equipment <{self.id}> {self.name}"
