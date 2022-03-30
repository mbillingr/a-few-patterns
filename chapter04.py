from abc import ABC, abstractmethod
from dataclasses import dataclass


class ShishD(ABC):
    def __init__(self):
        self.oo_fn = OnlyOnionsV()
        self.iv_fn = IsVegetarianV()

    @abstractmethod
    def only_onions(self) -> bool:
        pass

    @abstractmethod
    def is_vegetarian(self) -> bool:
        pass


class Skewer(ShishD):
    def __init__(self):
        super().__init__()

    def only_onions(self) -> bool:
        return self.oo_fn.for_skewer()

    def is_vegetarian(self) -> bool:
        return self.iv_fn.for_skewer()


class Onion(ShishD):
    def __init__(self, s: ShishD):
        super().__init__()
        self.s = s

    def only_onions(self) -> bool:
        return self.oo_fn.for_onions(self.s)

    def is_vegetarian(self) -> bool:
        return self.iv_fn.for_onion()


class Lamb(ShishD):
    def __init__(self, s: ShishD):
        super().__init__()
        self.s = s

    def only_onions(self) -> bool:
        return self.oo_fn.for_lamb(self.s)

    def is_vegetarian(self) -> bool:
        return self.iv_fn.for_lamb()


class Tomato(ShishD):
    def __init__(self, s: ShishD):
        super().__init__()
        self.s = s

    def only_onions(self) -> bool:
        return self.oo_fn.for_tomato(self.s)

    def is_vegetarian(self) -> bool:
        return self.iv_fn.for_tomato()


class OnlyOnionsV:
    def for_skewer(self) -> bool:
        return True

    def for_onions(self, s: ShishD) -> bool:
        return s.only_onions()

    def for_lamb(self, s: ShishD) -> bool:
        return False

    def for_tomato(self, s: ShishD) -> bool:
        return False


class IsVegetarianV:
    def for_skewer(self) -> bool:
        return True

    def for_onions(self, s: ShishD) -> bool:
        return s.is_vegetarian()

    def for_lamb(self, s: ShishD) -> bool:
        return False

    def for_tomato(self, s: ShishD) -> bool:
        return s.is_vegetarian()


assert Onion(Lamb(Tomato(Onion(Skewer())))).only_onions() is False
assert Onion(Onion(Skewer())).only_onions() is True
