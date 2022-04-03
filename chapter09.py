from abc import ABC, abstractmethod
from dataclasses import dataclass
from math import sqrt

print("CHAPTER 9")


class PointD(ABC):
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def closer_to0(self, p: "PointD") -> bool:
        return self.distance_to0() <= p.distance_to0()

    def minus(self, p: "PointD") -> "PointD":
        return CartesianPt(self.x - p.x, self.y - p.y)

    @abstractmethod
    def distance_to0(self) -> int:
        pass


class CartesianPt(PointD):
    def distance_to0(self) -> int:
        return int(sqrt(self.x**2 + self.y**2))


class ManhattanPt(PointD):
    def distance_to0(self) -> int:
        return self.x + self.y


class ShadowedManhattanPt(ManhattanPt):
    def __init__(self, x: int, y: int, dx: int, dy: int):
        super().__init__(x, y)
        self.dx = dx
        self.dy = dy

    def distance_to0(self) -> int:
        return super().distance_to0() + self.dx + self.dy


class ShadowedCartesianPt(CartesianPt):
    def __init__(self, x: int, y: int, dx: int, dy: int):
        super().__init__(x, y)
        self.dx = dx
        self.dy = dy

    def distance_to0(self) -> int:
        return CartesianPt(self.x + self.dx, self.y + self.dy).distance_to0()


class ShapeD(ABC):
    @abstractmethod
    def accept(self, ask: "ShapeVisitorI") -> bool:
        pass


@dataclass
class Circle(ShapeD):
    r: int

    def accept(self, ask: "ShapeVisitorI") -> bool:
        return ask.for_circle(self.r)


@dataclass
class Square(ShapeD):
    s: int

    def accept(self, ask: "ShapeVisitorI") -> bool:
        return ask.for_square(self.s)


@dataclass
class Trans(ShapeD):
    q: PointD
    s: ShapeD

    def accept(self, ask: "ShapeVisitorI") -> bool:
        return ask.for_trans(self.q, self.s)


class ShapeVisitorI(ABC):
    @abstractmethod
    def for_circle(self, r: int) -> bool:
        pass

    @abstractmethod
    def for_square(self, s: int) -> bool:
        pass

    @abstractmethod
    def for_trans(self, q: PointD, s: ShapeD) -> bool:
        pass


@dataclass
class HasPtV(ShapeVisitorI):
    p: PointD

    @staticmethod
    def new(p: PointD) -> ShapeVisitorI:
        return HasPtV(p)

    def for_circle(self, r: int) -> bool:
        return self.p.distance_to0() <= r

    def for_square(self, s: int) -> bool:
        return self.p.x <= s and self.p.y <= s

    def for_trans(self, q: PointD, s: ShapeD) -> bool:
        return s.accept(self.new(self.p.minus(q)))


assert not Circle(10).accept(HasPtV(CartesianPt(10, 10)))
assert Square(10).accept(HasPtV(CartesianPt(10, 10)))
assert Trans(CartesianPt(5, 6), Circle(10)).accept(HasPtV(CartesianPt(10, 10)))


class UnionVisitorI(ShapeVisitorI):
    @abstractmethod
    def for_union(self, s: ShapeD, t: ShapeD):
        pass


@dataclass
class Union(ShapeD):
    s: ShapeD
    t: ShapeD

    def accept(self, ask: UnionVisitorI) -> bool:
        return ask.for_union(self.s, self.t)


class UnionHasPtV(HasPtV, UnionVisitorI):
    @staticmethod
    def new(p: PointD) -> ShapeVisitorI:
        return UnionHasPtV(p)

    def for_union(self, s: ShapeD, t: ShapeD):
        return s.accept(self) or t.accept(self)


assert Trans(CartesianPt(3, 7), Union(Square(10), Circle(10))).accept(
    UnionHasPtV(CartesianPt(13, 17))
)
