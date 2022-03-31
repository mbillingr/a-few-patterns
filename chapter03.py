from abc import ABC, abstractmethod
from dataclasses import dataclass

print("CHAPTER 3")


class Pizza(ABC):
    @abstractmethod
    def remove_anchovy(self) -> "Pizza":
        pass

    @abstractmethod
    def top_anchovy_with_cheese(self) -> "Pizza":
        pass

    @abstractmethod
    def substitute_anchovy_by_cheese(self) -> "Pizza":
        pass


@dataclass
class Crust(Pizza):
    def remove_anchovy(self) -> Pizza:
        return Crust()

    def top_anchovy_with_cheese(self) -> Pizza:
        return Crust()

    def substitute_anchovy_by_cheese(self) -> Pizza:
        return Crust()


@dataclass
class Cheese(Pizza):
    p: Pizza

    def remove_anchovy(self) -> Pizza:
        return Cheese(self.p.remove_anchovy())

    def top_anchovy_with_cheese(self) -> Pizza:
        return Cheese(self.p.top_anchovy_with_cheese())

    def substitute_anchovy_by_cheese(self) -> Pizza:
        return Cheese(self.p.substitute_anchovy_by_cheese())


@dataclass
class Olive(Pizza):
    p: Pizza

    def remove_anchovy(self) -> Pizza:
        return Olive(self.p.remove_anchovy())

    def top_anchovy_with_cheese(self) -> Pizza:
        return Olive(self.p.top_anchovy_with_cheese())

    def substitute_anchovy_by_cheese(self) -> Pizza:
        return Olive(self.p.substitute_anchovy_by_cheese())


@dataclass
class Anchovy(Pizza):
    p: Pizza

    def remove_anchovy(self) -> Pizza:
        return self.p.remove_anchovy()

    def top_anchovy_with_cheese(self) -> Pizza:
        return Cheese(Anchovy(self.p.top_anchovy_with_cheese()))

    def substitute_anchovy_by_cheese(self) -> Pizza:
        return Cheese(self.p.substitute_anchovy_by_cheese())


@dataclass
class Sausage(Pizza):
    p: Pizza

    def remove_anchovy(self) -> Pizza:
        return Sausage(self.p.remove_anchovy())

    def top_anchovy_with_cheese(self) -> Pizza:
        return Sausage(self.p.top_anchovy_with_cheese())

    def substitute_anchovy_by_cheese(self) -> Pizza:
        return Sausage(self.p.substitute_anchovy_by_cheese())


@dataclass
class Spinach(Pizza):
    p: Pizza

    def remove_anchovy(self) -> Pizza:
        return Spinach(self.p.remove_anchovy())

    def top_anchovy_with_cheese(self) -> Pizza:
        return Spinach(self.p.top_anchovy_with_cheese())

    def substitute_anchovy_by_cheese(self) -> Pizza:
        return Spinach(self.p.substitute_anchovy_by_cheese())
