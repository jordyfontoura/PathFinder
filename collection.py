import math
import typing
class Vector(list):
    def __init__(self, *args):
        list.__init__(self)
        for i in range(len(args)):
            self.append(args[i])
    def __hash__(self):
        return hash(tuple(self))
    @property
    def x(self):
        return self[0]

    @x.setter
    def x(self, value):
        self[0] = value

    @property
    def y(self):
        return self[1]

    @y.setter
    def y(self, value):
        self[1] = value

    @property
    def z(self):
        return self[2]

    @z.setter
    def z(self, value):
        self[2] = value

    @classmethod
    def zero(cls, quant=2) -> 'Vector':
        return cls(*[0 for _ in range(quant)])

    @classmethod
    def one(cls, quant=2) -> 'Vector':
        return cls(*[1 for _ in range(quant)])
    @classmethod
    def right(cls, quant=2) -> 'Vector':
        return cls(*[1, *(0 for _ in range(quant-1))])
    @classmethod
    def left(cls, quant=2) -> 'Vector':
        return cls(*[-1, *(0 for _ in range(quant-1))])
    @classmethod
    def up(cls, quant=2) -> 'Vector':
        return cls(*[*(0 for _ in range(quant-1)), 1])
    @classmethod
    def down(cls, quant=2) -> 'Vector':
        return cls(*[*(0 for _ in range(quant-1)), -1])

    def __imul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            for i in range(len(self)):
                self[i] *= other
        else:
            if len(self) != len(other):
                raise Exception('Tamanhos diferentes!')
            for i in range(len(self)):
                self[i] *= other[i]
        return self

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Vector(*[el * other for el in self])
        else:
            if len(self) != len(other):
                raise Exception('Tamanhos diferentes!')
            res = []
            for i in range(len(self)):
                res.append(self[i] * other[i])
            return Vector(*res)

    def __iadd__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            for i in range(len(self)):
                self[i] += other
        else:
            if len(self) != len(other):
                raise Exception('Tamanhos diferentes!')
            for i in range(len(self)):
                self[i] += other[i]
        return self

    def __add__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Vector(*[el + other for el in self])
        else:
            if len(self) != len(other):
                raise Exception('Tamanhos diferentes!')
            res = []
            for i in range(len(self)):
                res.append(self[i] + other[i])
            return Vector(*res)

    def __isub__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            for i in range(len(self)):
                self[i] -= other
        else:
            if len(self) != len(other):
                raise Exception('Tamanhos diferentes!')
            for i in range(len(self)):
                self[i] -= other[i]
        return self

    def __sub__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Vector(*[el - other for el in self])
        else:
            if len(self) != len(other):
                raise Exception(f'Tamanhos diferentes! {self} / {other}')
            res = []
            for i in range(len(self)):
                res.append(self[i] - other[i])
            return Vector(*res)

    def __idiv__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            for i in range(len(self)):
                self[i] /= other
        else:
            if len(self) != len(other):
                raise Exception('Tamanhos diferentes!')
            for i in range(len(self)):
                self[i] /= other[i]
        return self

    def __truediv__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Vector(*[el / other for el in self])
        else:
            if len(self) != len(other):
                raise Exception('Tamanhos diferentes!')
            res = []
            for i in range(len(self)):
                res.append(self[i] / other[i])
            return Vector(*res)

    def __ifloordiv__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            for i in range(len(self)):
                self[i] //= other
        else:
            if len(self) != len(other):
                raise Exception('Tamanhos diferentes!')
            for i in range(len(self)):
                self[i] //= other[i]
        return self

    def __floordiv__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Vector(*[el // other for el in self])
        else:
            if len(self) != len(other):
                raise Exception('Tamanhos diferentes!')
            res = []
            for i in range(len(self)):
                res.append(self[i] // other[i])
            return Vector(*res)

    def __neg__(self):
        return Vector(*[-x for x in self])
    def cast(self, ty: type):
        res = []
        for el in self:
            res.append(ty(el))
        return res

    def rotated(self, rotation):
        angle = math.radians(rotation)
        return Vector(self.x * math.cos(angle) + self.y * math.sin(angle),
                      self.y * math.cos(angle) - self.x * math.sin(angle))

    def __copy__(self):
        return Vector(*self)