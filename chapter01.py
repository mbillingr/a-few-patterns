from abc import ABC
from dataclasses import dataclass

# ---------------------------------------


class SeasoningD(ABC):
    pass


class Salt(SeasoningD):
    pass


class Pepper(SeasoningD):
    pass


print(Salt())
print(Pepper())


class Thyme(SeasoningD):
    pass


class Sage(SeasoningD):
    pass


# ---------------------------------------


class PointD(ABC):
    pass


class CartesianPt(PointD):
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class ManhattanPt(PointD):
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


# ---------------------------------------


class NumD(ABC):
    pass


@dataclass
class Zero(NumD):
    pass


@dataclass
class OneMoreThan(NumD):
    predecessor: NumD


print(Zero())
print(OneMoreThan(Zero()))
print(OneMoreThan(OneMoreThan(Zero())))

# ---------------------------------------


class LayerD(ABC):
    pass


@dataclass
class Base(LayerD):
    o: object


@dataclass
class Slice(LayerD):
    l: LayerD


print(Base(Zero()))
print(Base(Salt()))
