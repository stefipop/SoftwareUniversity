class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)
        Zoo.__animals += 1

    def get_info(self, species):
        info = ""
        if species == "mammal":
            info = f"Mammals in {self.name}: {', '.join(self.mammals)}"
        elif species == "fish":
            info = f"Fishes in {self.name}: {', '.join(self.fishes)}"
        elif species == "bird":
            info = f"Birds in {self.name}: {', '.join(self.birds)}"
        return f"{info}\nTotal animals: {Zoo.__animals}"


zoo_name = input()
zoo = Zoo(zoo_name)
n = int(input())

for _ in range(n):
    species, name = input().split()
    zoo.add_animal(species, name)

specie = input()
print(zoo.get_info(specie))
