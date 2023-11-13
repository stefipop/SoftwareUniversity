from project.cat import Cat


class Kitten(Cat):
    def __init__(self, name, age) -> None:
        super().__init__(name, age, gender="Female")

    def make_sound(self) -> str:
        return "Meow"
