from abc import ABC, abstractmethod
from dataclasses import dataclass

from chapter01 import Zero

print("CHAPTER 5")


class PizzaPieD(ABC):
    def __init__(self):
        self.rem_fn = RemoveV()
        self.subst_fn = SubstV()

    def remove_anchovies(self) -> "PizzaPieD":
        return self.remove_fish(Anchovy())

    def remove_fish(self, f: "FishD") -> "PizzaPieD":
        return self.remove(f)

    @abstractmethod
    def remove(self, o: object) -> "PizzaPieD":
        pass

    @abstractmethod
    def substitute(self, n: object, o: object) -> "PizzaPieD":
        pass


class Bottom(PizzaPieD):
    def remove(self, o: object) -> PizzaPieD:
        return self.rem_fn.for_bot(o)

    def substitute(self, n: object, o: object) -> PizzaPieD:
        return self.subst_fn.for_bot(n, o)

    def __repr__(self):
        return "Bottom()"


class Topping(PizzaPieD):
    def __init__(self, t: object, r: PizzaPieD):
        super().__init__()
        self.t = t
        self.r = r

    def remove(self, o: object) -> PizzaPieD:
        return self.rem_fn.for_top(self.t, self.r, o)

    def substitute(self, n: object, o: object) -> PizzaPieD:
        return self.subst_fn.for_top(self.t, self.r.substitute(n, o), n, o)

    def __repr__(self):
        return f"Topping({self.t}, {self.r})"


class FishD(ABC):
    pass


@dataclass
class Anchovy(FishD):
    pass


@dataclass
class Salmon(FishD):
    pass


@dataclass
class Tuna(FishD):
    pass


class RemoveV:
    def for_bot(self, o: object) -> PizzaPieD:
        return Bottom()

    def for_top(self, t: object, r: PizzaPieD, o: object):
        if t == o:
            return r.remove(o)
        else:
            return Topping(t, r.remove(o))


class SubstV:
    def for_bot(self, n: object, o: object) -> PizzaPieD:
        return Bottom()

    def for_top(self, t: object, r: PizzaPieD, n: object, o: object):
        if t == o:
            return Topping(n, r.substitute(n, o))
        else:
            return Topping(t, r.substitute(n, o))


print(
    Topping(Anchovy(), Topping(Tuna(), Topping(Anchovy(), Bottom()))).remove_anchovies()
)
print(
    Topping(Anchovy(), Topping(Tuna(), Topping(Anchovy(), Bottom()))).remove(Anchovy())
)

# assert Topping(
#    Salmon(), Topping(Anchovy(), Topping(Tuna(), Topping(Anchovy(), Bottom())))
# ).remove_anchovies() == Topping(Salmon, Topping(Tuna(), Bottom()))

print(Topping(Zero(), Bottom()).remove(Zero()))
print(Topping(Zero(), Bottom()).substitute(42, Zero()))
