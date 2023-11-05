from typing import List
from project.animal import Animal
from project.worker import Worker
from project.lion import Lion
from project.tiger import Tiger
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.caretaker import Caretaker
from project.vet import Vet


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int) -> None:
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: List[Animal] = []
        self.workers: List[Worker] = []

    def add_animal(self, animal: Animal, price: int) -> str:
        if self.__budget >= price:
            if len(self.animals) < self.__animal_capacity:
                self.animals.append(animal)
                self.__budget -= price
                return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

            return "Not enough space for animal"

        return "Not enough budget"

    def hire_worker(self, worker: Worker) -> str:
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"

        return "Not enough space for worker"

    def fire_worker(self, worker_name: str) -> str:
        for worker in self.workers:
            if worker_name == worker.name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"

        return f"There is no {worker_name} in the zoo"

    def pay_workers(self) -> str:
        salary_sum = sum(w.salary for w in self.workers)
        if self.__budget >= salary_sum:
            self.__budget -= salary_sum
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self) -> str:
        expenses = sum(a.money_for_care for a in self.animals)
        if self.__budget >= expenses:
            self.__budget -= expenses
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount: int) -> None:
        self.__budget += amount

    def animals_status(self) -> str:
        # lions = [animal for animal in self.animals if animal.__class__.__name__== "Lion"]
        result = [f"You have {len(self.animals)} animals"]
        animal_types = {"Lions": Lion, "Tigers": Tiger, "Cheetahs": Cheetah}

        for type_name, animal_type in animal_types.items():
            animals_of_type = [a for a in self.animals if isinstance(a, animal_type)]
            result.append(f"----- {len(animals_of_type)} {type_name}:")
            result.extend(a.__repr__() for a in animals_of_type)

        return '\n'.join(result)

    def workers_status(self) -> str:
        result = [f"You have {len(self.workers)} workers"]
        worker_types = {"Keepers": Keeper, "Caretakers": Caretaker, "Vets": Vet}

        for type_name, worker_type in worker_types.items():
            workers_of_type = [w for w in self.workers if isinstance(w, worker_type)]
            result.append(f"----- {len(workers_of_type)} {type_name}:")
            result.extend(w.__repr__() for w in workers_of_type)

        return '\n'.join(result)
