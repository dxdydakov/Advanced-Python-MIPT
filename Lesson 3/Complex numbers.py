import numpy as np

class Complex(object):
    #------------
    # Создан класс для хранения комплексных чисел с инициализатором.
    # Добавлены и перегружены основные методы для работы с комплексными числами.
    # Добавлены описания методов с математическими вкладками.
    # Добавлена библиотека numpy для тригонометрических вычислений.
    #------------

    def __init__(self, real, imag = 0):
        # Сообственно сам инициализатор, который принимает 2 параметра: real, imag - действительная и мнимые части числа соответсвенно.
        # Исключение составляет, когда запрашивается метод object.to_alg(). Подробнее ниже.
        # Возможен ввод чисто действительного числа, т.к. по умолчанию imag = 0.
        self.real = real
        self.imag = imag

    def __add__(self, other):
        # Сложение комплексных чисел эквивалетно сложению их действительных и мнимых частей соответственно.
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        # Вычитание комплексных чисел эквивалетно вычитанию их действительных и мнимых частей соответственно.
        return Complex(self.real + other.real, self.imag + other.imag)

    def __mul__(self, other):
        # Перемножение комплексных чисел: (a+bj) * (c+dj) = (ac-bd) + (ad+bc)j.
        return Complex(self.real * other.real - self.imag * other.image, self.real * other.imag + self.imag*other.real)

    def __truediv__(self, other):
        # Деление комплексных чисел:
        # (a+bj) / (c+dj) = (a+bj)*(c-dj) / (c+dj)*(c-dj) = (a+bj) * (c-dj) / divisor = (ac+bd)/divisor + (bc - ad)j/divisor.
        # divisor = c**2 + d**2.

        divisor = other.get_module(other.real, other.imag)**2
        return Complex(((self.real * other.real)+(self.imag * other.imag))/divisor,
                       ((self.imag * other.real - self.real * other.imag))/divisor)

    def __repr__(self):
        # Меняем repr-описание объекта. Позволяет выводить комплексное число в явном виде.
        return '({}, {})'.format(self.real, self.imag)

    def set_real(self, number):
        # Меняет действительную часть числа.
        self.real = number
        return self.real

    def set_imag(self, number):
        # Меняет мнимую часть числа.
        self.imag = number
        return self. imag

    def get_conjugate(self):
        # Получить сопряжённое комплексное число.
        return Complex(self.real, -1 * self.imag)

    def get_module(self):
        # Получить модуль комплексного числа.
        self.m = np.sqrt(self.real ** 2 + self.imag ** 2)
        return self.m

    def get_phi(self):
        # Получить угол соответствующий комплексному числу.
        if self.real > 0:
            self.phi = np.arctan(self.imag / self.real) * 180 / np.pi

        elif self.real < 0 and self.image > 0:
            self.phi = (np.arctan(self.imag / self.real) + np.pi) * 180 / np.pi

        elif self.real < 0 and self.image < 0:
            self.phi = (np.arctan(self.imag / self.real) - np.pi) * 180 / np.pi

        elif self.imag == 0:
            self.phi = 0

        elif self.real == 0:
            self.phi = 90

        return self.phi

    def to_exp(self):
        # Получить показательную форму комплексного числа с точностью до десятых: z = |z|exp(iφ).
        return '{:.1f}*exp({:.1f}*i)'.format(self.get_module(), self.get_phi())

    def to_coord(self):
        # Принимает на вход 2 параметра, которым сооответствует модуль комплексного числа и его угол в градусах на комплексной плоскости.
        # Ставит в соответствие комплексное число (пару точек) из нашего класса, вычислив его действительную и мнимую части c точностью до десятых.
        self.m, self.phi = self.real, self.imag

        self.real = self.m * np.cos(self.phi)
        self.imag = self.m * np.sin(self.phi)

        return '({:.1f},{:.1f})'.format(self.real, self.imag)


