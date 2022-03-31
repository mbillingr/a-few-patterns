from abc import ABC, abstractmethod
from dataclasses import dataclass

from chapter05 import FishD, Anchovy, Tuna, Salmon

print("CHAPTER 6")


class PizzaPieD(ABC):
    @abstractmethod
    def accept(self, ask: "PieVisitorI") -> "PizzaPieD":
        pass


class Bottom(PizzaPieD):
    def accept(self, ask: "PieVisitorI") -> "PizzaPieD":
        return ask.for_bot()

    def __repr__(self):
        return "Bottom()"


class Topping(PizzaPieD):
    def __init__(self, t: object, r: PizzaPieD):
        super().__init__()
        self.t = t
        self.r = r

    def accept(self, ask: "PieVisitorI") -> "PizzaPieD":
        return ask.for_top(self.t, self.r)

    def __repr__(self):
        return f"Topping({self.t}, {self.r})"


class PieVisitorI(ABC):
    @abstractmethod
    def for_bot(self) -> PizzaPieD:
        pass

    @abstractmethod
    def for_top(self, t: object, r: object) -> PizzaPieD:
        pass


class RemoveV(PieVisitorI):
    def __init__(self, o: object):
        self.o = o

    def for_bot(self) -> PizzaPieD:
        return Bottom()

    def for_top(self, t: object, r: PizzaPieD):
        if t == self.o:
            return r.accept(self)
        else:
            return Topping(t, r.accept(self))


class SubstV(PieVisitorI):
    def __init__(self, n: object, o: object):
        self.n = n
        self.o = o

    def for_bot(self) -> PizzaPieD:
        return Bottom()

    def for_top(self, t: object, r: PizzaPieD):
        if t == self.o:
            return Topping(self.n, r.accept(self))
        else:
            return Topping(t, r.accept(self))


class LimitedSubstitutionV(PieVisitorI):
    def __init__(self, c: int, n: object, o: object):
        self.c = c
        self.n = n
        self.o = o

    def for_bot(self) -> PizzaPieD:
        return Bottom()

    def for_top(self, t: object, r: PizzaPieD):
        if self.c == 0:
            return Topping(t, r)
        if t == self.o:
            return Topping(
                self.n, r.accept(LimitedSubstitutionV(self.c - 1, self.n, self.o))
            )
        else:
            return Topping(t, r.accept(self))


print(
    Topping(Anchovy(), Topping(Tuna(), Topping(Anchovy(), Bottom()))).accept(
        RemoveV(Anchovy())
    )
)
print(
    Topping(Anchovy(), Topping(Tuna(), Topping(Anchovy(), Bottom()))).accept(
        SubstV(Salmon(), Anchovy())
    )
)
print(
    Topping(
        Anchovy(), Topping(Anchovy(), Topping(Tuna(), Topping(Anchovy(), Bottom())))
    ).accept(LimitedSubstitutionV(2, Salmon(), Anchovy()))
)
