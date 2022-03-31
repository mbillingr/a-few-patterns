from abc import ABC, abstractmethod
from dataclasses import dataclass

print("CHAPTER 7")


class FruitD(ABC):
    pass


@dataclass
class Peach(FruitD):
    pass


@dataclass
class Apple(FruitD):
    pass


@dataclass
class Pear(FruitD):
    pass


@dataclass
class Lemon(FruitD):
    pass


@dataclass
class Fig(FruitD):
    pass


class TreeD(ABC):
    @abstractmethod
    def accept(self, ask: "TreeVisitorI"):
        pass


@dataclass
class Bud(TreeD):
    def accept(self, ask: "TreeVisitorI"):
        return ask.for_bud()


@dataclass
class Flat(TreeD):
    f: FruitD
    t: TreeD

    def accept(self, ask: "TreeVisitorI"):
        return ask.for_flat(self.f, self.t)


@dataclass
class Split(TreeD):
    l: TreeD
    r: TreeD

    def accept(self, ask: "TreeVisitorI"):
        return ask.for_split(self.l, self.r)


class TreeVisitorI(ABC):
    @abstractmethod
    def for_bud(self):
        pass

    @abstractmethod
    def for_flat(self, f: FruitD, t: TreeD):
        pass

    @abstractmethod
    def for_split(self, l: TreeD, r: TreeD):
        pass


class bIsFlatV(TreeVisitorI):
    def for_bud(self) -> bool:
        return True

    def for_flat(self, f: FruitD, t: TreeD) -> bool:
        return t.accept(self)

    def for_split(self, l: TreeD, r: TreeD) -> bool:
        return False


class bIsSplitV(TreeVisitorI):
    def for_bud(self) -> bool:
        return True

    def for_flat(self, f: FruitD, t: TreeD) -> bool:
        return False

    def for_split(self, l: TreeD, r: TreeD) -> bool:
        return l.accept(self) and r.accept(self)


class bHasFruitV(TreeVisitorI):
    def for_bud(self) -> bool:
        return False

    def for_flat(self, f: FruitD, t: TreeD) -> bool:
        return True

    def for_split(self, l: TreeD, r: TreeD) -> bool:
        return l.accept(self) or r.accept(self)


assert Bud().accept(bIsSplitV())
assert Split(
    Split(Bud(), Split(Bud(), Bud())), Split(Bud(), Split(Bud(), Bud()))
).accept(bIsSplitV())

assert not Bud().accept(bHasFruitV())
assert Split(Bud(), Flat(Lemon(), Bud())).accept(bHasFruitV())


class iHeihtV(TreeVisitorI):
    def for_bud(self) -> int:
        return 0

    def for_flat(self, f: FruitD, t: TreeD):
        return 1 + t.accept(self)

    def for_split(self, l: TreeD, r: TreeD):
        return 1 + max(l.accept(self), r.accept(self))


assert Bud().accept(iHeihtV()) == 0
assert Split(Bud(), Flat(Fig(), Bud())).accept(iHeihtV()) == 2


@dataclass
class tSubstV(TreeVisitorI):
    n: FruitD
    o: FruitD

    def for_bud(self) -> TreeD:
        return Bud()

    def for_flat(self, f: FruitD, t: TreeD):
        if f == self.o:
            return Flat(self.n, t.accept(self))
        else:
            return Flat(f, t.accept(self))

    def for_split(self, l: TreeD, r: TreeD):
        return Split(l.accept(self), r.accept(self))


@dataclass
class iOccurs(TreeVisitorI):
    a: FruitD

    def for_bud(self) -> int:
        return 0

    def for_flat(self, f: FruitD, t: TreeD):
        if f == self.a:
            return 1 + t.accept(self)
        else:
            return t.accept(self)

    def for_split(self, l: TreeD, r: TreeD):
        return l.accept(self) + r.accept(self)
