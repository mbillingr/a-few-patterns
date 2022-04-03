from abc import ABC, abstractmethod
from dataclasses import dataclass


print("CHAPTER 10c")


class PointD(ABC):
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def closer_to0(self, p: "PointD") -> bool:
        return self.distance_to0() <= p.distance_to0()

    def minus(self, p: "PointD") -> "PointD":
        return CartesianPt(self.x - p.x, self.y - p.y)

    def move_by(self, dx: int, dy: int):
        self.x += dx
        self.y += dy
        return self.distance_to0()

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


pt_child = ManhattanPt(1, 4)
assert pt_child.distance_to0() == 5
assert pt_child.move_by(2, 8) == 15

pt_child_balloon = ShadowedManhattanPt(1, 4, 1, 1)
assert pt_child_balloon.distance_to0() == 7
assert pt_child_balloon.move_by(2, 8) == 17