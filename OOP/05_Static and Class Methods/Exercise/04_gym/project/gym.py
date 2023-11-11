from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer
from typing import List


class Gym:
    def __init__(self) -> None:
        self.subscriptions: List[Subscription] = []
        self.customers: List[Customer] = []
        self.trainers: List[Trainer] = []
        self.equipment: List[Equipment] = []
        self.plans: List[ExercisePlan] = []

    @staticmethod
    def add_to_list(obj, obj_list: List) -> None:
        if obj not in obj_list:
            obj_list.append(obj)

    def add_customer(self, customer: Customer) -> None:
        self.add_to_list(customer, self.customers)

    def add_trainer(self, trainer: Trainer) -> None:
        self.add_to_list(trainer, self.trainers)

    def add_equipment(self, equipment: Equipment) -> None:
        self.add_to_list(equipment, self.equipment)

    def add_plan(self, plan: ExercisePlan) -> None:
        self.add_to_list(plan, self.plans)

    def add_subscription(self, subscription: Subscription) -> None:
        self.add_to_list(subscription, self.subscriptions)

    def subscription_info(self, subscription_id: int) -> str:
        subscription = next((s for s in self.subscriptions if s.id == subscription_id), None)
        if subscription:
            customer = next((c for c in self.customers if c.id == subscription.customer_id), None)
            trainer = next((t for t in self.trainers if t.id == subscription.trainer_id), None)
            plan = next((p for p in self.plans if p.id == subscription.exercise_id), None)
            if plan:
                equipment = next((e for e in self.equipment if e.id == plan.equipment_id), None)

                return "\n".join([str(subscription), str(customer), str(trainer), str(equipment), str(plan)])
