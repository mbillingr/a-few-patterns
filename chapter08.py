from abc import ABC, abstractmethod
from dataclasses import dataclass

print("CHAPTER 8")


class ExprD(ABC):
    @abstractmethod
    def accept(self, ask: "ExprVisitorI") -> object:
        pass


class ExprVisitorI(ABC):
    @abstractmethod
    def for_plus(self, l: ExprD, r: ExprD) -> object:
        pass

    @abstractmethod
    def for_diff(self, l: ExprD, r: ExprD) -> object:
        pass

    @abstractmethod
    def for_prod(self, l: ExprD, r: ExprD) -> object:
        pass

    @abstractmethod
    def for_const(self, c: object) -> object:
        pass


@dataclass
class Plus(ExprD):
    l: ExprD
    r: ExprD

    def accept(self, ask: ExprVisitorI) -> object:
        return ask.for_plus(self.l, self.r)


@dataclass
class Diff(ExprD):
    l: ExprD
    r: ExprD

    def accept(self, ask: ExprVisitorI) -> object:
        return ask.for_diff(self.l, self.r)


@dataclass
class Prod(ExprD):
    l: ExprD
    r: ExprD

    def accept(self, ask: ExprVisitorI) -> object:
        return ask.for_prod(self.l, self.r)


@dataclass
class Const(ExprD):
    c: object

    def accept(self, ask: ExprVisitorI) -> object:
        return ask.for_const(self.c)


class EvalD(ExprVisitorI):
    def for_plus(self, l: ExprD, r: ExprD) -> object:
        return self.plus(l.accept(self), r.accept(self))

    def for_diff(self, l: ExprD, r: ExprD) -> object:
        return self.diff(l.accept(self), r.accept(self))

    def for_prod(self, l: ExprD, r: ExprD) -> object:
        return self.prod(l.accept(self), r.accept(self))

    def for_const(self, c: object) -> object:
        return c

    @abstractmethod
    def plus(self, l, r):
        pass

    @abstractmethod
    def diff(self, l, r):
        pass

    @abstractmethod
    def prod(self, l, r):
        pass


class IntEvalV(EvalD):
    def plus(self, l, r):
        return l + r

    def diff(self, l, r):
        return l - r

    def prod(self, l, r):
        return l * r


class SetEvalV(EvalD):
    def plus(self, l: "SetD", r: "SetD"):
        return l.plus(r)

    def diff(self, l: "SetD", r: "SetD"):
        return l.diff(r)

    def prod(self, l: "SetD", r: "SetD"):
        return l.prod(r)


print(Prod(Const(3), Const(2)).accept(IntEvalV()))


class SetD(ABC):
    def add(self, i):
        if self.mem(i):
            return self
        else:
            return Add(i, self)

    @abstractmethod
    def mem(self, i) -> bool:
        pass

    @abstractmethod
    def plus(self, s: "SetD") -> "SetD":
        pass

    @abstractmethod
    def diff(self, s: "SetD") -> "SetD":
        pass

    @abstractmethod
    def prod(self, s: "SetD") -> "SetD":
        pass


@dataclass
class Empty(SetD):
    def mem(self, i) -> bool:
        return False

    def plus(self, s: SetD) -> SetD:
        return s

    def diff(self, s: SetD) -> SetD:
        return Empty()

    def prod(self, s: SetD) -> SetD:
        return Empty()


@dataclass
class Add(SetD):
    i: object
    s: SetD

    def mem(self, i) -> bool:
        if i == self.i:
            return True
        else:
            return self.s.mem(i)

    def plus(self, t: SetD) -> SetD:
        return self.s.plus(t.add(self.i))

    def diff(self, t: SetD) -> SetD:
        if t.mem(self.i):
            return self.s.diff(t)
        else:
            return self.s.diff(t).add(self.i)

    def prod(self, t: SetD) -> SetD:
        if t.mem(self.i):
            return self.s.prod(t).add(self.i)
        else:
            return self.s.prod(t)


print(Prod(Const(Empty().add(7)), Const(Empty().add(3))).accept(SetEvalV()))
