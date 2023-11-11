class Category:
    def __init__(self, category_id: int, name: str) -> None:
        self.id = category_id
        self.name = name

    def edit(self, new_name: str) -> None:
        """Edit the name of the Category."""
        self.name = new_name

    def __repr__(self) -> str:
        return f"Category {self.id}: {self.name}"
