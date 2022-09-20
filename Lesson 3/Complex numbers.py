import numpy as np

class Complex(object):
    #------------
    #
    #------------

    def __init__(self, real, imag = 0.0):
        self.real = real
        self.imag = imag

    def module(self, real, imag):
        return np.sqrt(self.real**2+self.imag**2)

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(selfs, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __mul__(self, other):
        # Как происходит перемножение комплексных чисел:
        # (a+bj) * (c+dj) = (ac-bd) + (ad+bc)j
        return Complex(self.real * other.real - self.imag * other.image, self.real * other.imag + self.imag*other.real)

    def __truediv__(self, other):
        # Как происходит деление комплексных чисел:
        # (a+bj) / (c+dj) = (a+bj)*(c-dj) / (c+dj)*(c-dj) = (a+bj) * (c-dj) / divisor = (ac+bd)/divisor + (bc - ad)j/divisor
        # divisor = c**2 + d**2

        divisor = other.module(other.real, other.imag)**2
        return Complex(((self.real * other.real)+(self.imag * other.imag))/divisor,
                       ((self.imag * other.real - self.real * other.imag))/divisor)

    def to_exp(self):
        # Показательной формой комплексного числа z называется выражение |z|exp(iφ).
        m = (self.real**2 + self.imag**2)**0.5

        if self.real > 0:
            phi = np.arctan(self.imag / self.real)

        elif self.real < 0 and self.image > 0:
            phi = np.arctan(self.imag / self.real) + np.pi

        elif self.real < 0 and self.image < 0:
            phi = np.arctan(self.imag / self.real) - np.pi

        # Хотим ответ в градусах
        phi = 180*phi/np.pi

        return '{}*exp({}*i)'.format(m, phi)



    def __repr__(self):
        # Добавим свое repr-описание класса вместо стандартного.
        return '({}, {})'.format(self.real, self.imag)









