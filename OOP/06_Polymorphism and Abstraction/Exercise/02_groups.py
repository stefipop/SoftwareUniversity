from typing import List


class Person:
    def __init__(self, name: str, surname: str) -> None:
        self.name = name
        self.surname = surname

    def __add__(self, other: 'Person') -> 'Person':
        # Create a new instance with the first name from the first person and the surname from the second person
        return Person(self.name, other.surname)

    def __repr__(self) -> str:
        return f"{self.name} {self.surname}"


class Group:
    def __init__(self, name: str, people: List[Person]) -> None:
        self.name = name
        self.people: List[Person] = people

    def __len__(self) -> int:
        return len(self.people)

    def __add__(self, other: 'Group') -> 'Group':
        new_name = f"{self.name} {other.name}"
        new_people = self.people + other.people
        return Group(new_name, new_people)

    # def __getitem__(self, idx) -> str:
    #     if idx == len(self.people):
    #         raise IndexError
    #     return f"Person {idx}: {str(self.people[idx])}"

    def __getitem__(self, index: int) -> Person:
        return self.people[index]

    def __iter__(self) -> str:
        for index, person in enumerate(self.people):
            yield f"Person {index}: {person.name}"

    def __repr__(self) -> str:
        # Represent the group with its name and members' names separated by a comma and space
        members_str = ", ".join(str(p) for p in self.people)
        return f"Group {self.name} with members {members_str}"


p0 = Person('Aliko', 'Dangote')
p1 = Person('Bill', 'Gates')
p2 = Person('Warren', 'Buffet')
p3 = Person('Elon', 'Musk')
p4 = p2 + p3

first_group = Group('__VIP__', [p0, p1, p2])
second_group = Group('Special', [p3, p4])
third_group = first_group + second_group

print(len(first_group))
print(second_group)
print(third_group[0])

for person in third_group:
    print(person)
