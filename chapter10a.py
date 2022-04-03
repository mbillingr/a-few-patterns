from abc import ABC, abstractmethod
from dataclasses import dataclass

from chapter05 import FishD, Anchovy, Tuna, Salmon


print("CHAPTER 10a")


class PieD(ABC):
    @abstractmethod
    def accept(self, ask: "PieVisitorI") -> object:
        pass


class PieVisitorI(ABC):
    @abstractmethod
    def for_bot(self) -> object:
        pass

    @abstractmethod
    def for_top(self, t: object, r: PieD) -> object:
        pass


@dataclass
class Bot(PieD):
    def accept(self, ask: PieVisitorI) -> object:
        return ask.for_bot()


@dataclass
class Top(PieD):
    t: object
    r: PieD

    def accept(self, ask: PieVisitorI) -> object:
        return ask.for_top(self.t, self.r)


@dataclass
class OccursV(PieVisitorI):
    a: object

    def for_bot(self) -> object:
        return 0

    def for_top(self, t: object, r: PieD) -> object:
        if t == self.a:
            return 1 + r.accept(self)
        else:
            return r.accept(self)


@dataclass
class SubstV(PieVisitorI):
    n: object
    o: object

    def for_bot(self) -> object:
        return Bot()

    def for_top(self, t: object, r: PieD) -> object:
        if t == self.o:
            return Top(self.n, r.accept(self))
        else:
            return Top(t, r.accept(self))


@dataclass
class RemV(PieVisitorI):
    o: object

    def for_bot(self) -> object:
        return Bot()

    def for_top(self, t: object, r: PieD) -> object:
        if t == self.o:
            return r.accept(self)
        else:
            return Top(t, r.accept(self))


class PiemanI(ABC):
    @abstractmethod
    def add_top(self, t: object) -> int:
        pass

    @abstractmethod
    def rem_top(self, t: object) -> int:
        pass

    @abstractmethod
    def subst_top(self, n: object, o: object) -> int:
        pass

    @abstractmethod
    def occ_top(self, o: object) -> int:
        pass


class PiemanM(PiemanI):
    def __init__(self):
        self.p = Bot()

    def add_top(self, t: object) -> int:
        self.p = Top(t, self.p)
        return self.occ_top(t)

    def rem_top(self, t: object) -> int:
        self.p = self.p.accept(RemV(t))
        return self.occ_top(t)

    def subst_top(self, n: object, o: object) -> int:
        self.p = self.p.accept(SubstV(n, o))
        return self.occ_top(n)

    def occ_top(self, o: object) -> int:
        return self.p.accept(OccursV(o))


assert PiemanM().occ_top(Anchovy()) == 0
assert PiemanM().add_top(Anchovy()) == 1

y = PiemanM()
assert y.add_top(Anchovy()) == 1
assert y.subst_top(Tuna(), Anchovy()) == 1
assert y.occ_top(Anchovy()) == 0

yy = PiemanM()
assert yy.add_top(Anchovy()) == 1
assert yy.add_top(Anchovy()) == 2
assert yy.add_top(Salmon()) == 1
assert yy.add_top(Tuna()) == 1
assert yy.add_top(Tuna()) == 2
assert yy.subst_top(Tuna(), Anchovy()) == 4
assert yy.rem_top(Tuna()) == 0

