from dataclasses import dataclass
from typing import List
from app.instances.car import Car


@dataclass
class Customer:

    name: str
    product_cart: dict
    location: List[int]
    money: float
    car: Car

    def ride_to_shop(
        self,
        trip_cost: float,
        shop_name: str,
        shop_location: List[int]
    ) -> None:
        print(f"{self.name} rides to {shop_name}\n")
        self.money = self.money - trip_cost
        self.home_location = self.location
        self.location = shop_location

    def ride_home(self, trip_cost: float) -> None:
        print(f"{self.name} rides home")
        self.money = round(self.money - trip_cost, 2)
        print(f"{self.name} now has {self.money} dollars\n")
        self.location = self.home_location