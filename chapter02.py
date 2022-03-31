from abc import ABC, abstractmethod
from dataclasses import dataclass
from math import sqrt

print("CHAPTER 2")


@dataclass
class PointD(ABC):
    x: int
    y: int

    @abstractmethod
    def distance_to0(self):
        pass

    def closer_to0(self, p: "PointD") -> bool:
        return self.distance_to0() <= p.distance_to0()


@dataclass
class CartesianPt(PointD):
    def distance_to0(self):
        return int(sqrt(self.x**2 + self.y**2))


@dataclass
class ManhattanPt(PointD):
    def distance_to0(self):
        return self.x + self.y


print(ManhattanPt(3, 4).distance_to0())
print(CartesianPt(3, 4).distance_to0())

# ---------------------------------------


class ShishD(ABC):
    @abstractmethod
    def only_onions(self) -> bool:
        pass

    @abstractmethod
    def is_vegetarian(self) -> bool:
        pass


@dataclass
class Skewer(ShishD):
    def only_onions(self) -> bool:
        return True

    def is_vegetarian(self) -> bool:
        return True


@dataclass
class Onion(ShishD):
    s: ShishD

    def only_onions(self) -> bool:
        return self.s.only_onions()

    def is_vegetarian(self) -> bool:
        return self.s.is_vegetarian()


@dataclass
class Lamb(ShishD):
    s: ShishD

    def only_onions(self) -> bool:
        return False

    def is_vegetarian(self) -> bool:
        return False


@dataclass
class Tomato(ShishD):
    s: ShishD

    def only_onions(self) -> bool:
        return False

    def is_vegetarian(self) -> bool:
        return self.s.is_vegetarian()


print(Skewer())
print(Onion(Skewer()))
print(Onion(Lamb(Onion(Skewer()))))

assert Onion(Onion(Skewer())).only_onions() is True
assert Onion(Lamb(Skewer())).only_onions() is False

# ---------------------------------------


class KebabD(ABC):
    @abstractmethod
    def is_veggie(self) -> bool:
        pass

    @abstractmethod
    def what_holder(self) -> object:
        pass


@dataclass
class Holder(KebabD):
    o: object

    def is_veggie(self):
        return True

    def what_holder(self) -> object:
        return o


@dataclass
class Shallot(KebabD):
    k: KebabD

    def is_veggie(self):
        return self.k.is_veggie()

    def what_holder(self) -> object:
        return self.k.what_holder()


@dataclass
class Shrimp(KebabD):
    k: KebabD

    def is_veggie(self):
        return False

    def what_holder(self) -> object:
        return self.k.what_holder()


@dataclass
class Radish(KebabD):
    k: KebabD

    def is_veggie(self):
        return self.k.is_veggie()

    def what_holder(self) -> object:
        return self.k.what_holder()


class Rod(ABC):
    pass


@dataclass
class Dagger(Rod):
    pass


@dataclass
class Sabre(Rod):
    pass


@dataclass
class Sword(Rod):
    pass


class PlateD(ABC):
    pass


@dataclass
class Gold(PlateD):
    pass


@dataclass
class Silver(PlateD):
    pass


@dataclass
class Brass(PlateD):
    pass


@dataclass
class Copper(PlateD):
    pass


@dataclass
class Wood(PlateD):
    pass


print(Shallot(Radish(Holder(Dagger()))))
assert Shallot(Radish(Holder(Dagger()))).is_veggie() is True
assert Shallot(Radish(Holder(Gold()))).is_veggie() is True


@dataclass
class Pepper(KebabD):
    k: KebabD

    def is_veggie(self):
        return self.k.is_veggie()

    def what_holder(self) -> object:
        return self.k.what_holder()


@dataclass
class Zucchini(KebabD):
    k: KebabD

    def is_veggie(self):
        return self.k.is_veggie()

    def what_holder(self) -> object:
        return self.k.what_holder()
