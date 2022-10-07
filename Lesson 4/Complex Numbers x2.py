import numpy as np

class Complex(object):
    #------------PART 1------------
    # Создан класс для хранения комплексных чисел с инициализатором.
    # Добавлены и перегружены основные методы для работы с комплексными числами.
    # Добавлены описания методов с математическими вкладками.
    # Добавлена библиотека numpy для тригонометрических вычислений.
    #------------------------------

    #------------PART2-------------
    # Исправлена ошибка с вычитанием комплексных чисел.
    # Добавлено присваивание и обращение к мнимой и действительной частям комплексного числа по индексам:
    # x[0] = Re(x), x[1] = Im(x).
    # Перегружен метод метод __abs__(self). Теперь он возвращает модуль комплексного числа.
    # Появилась возможность сравнивать комплексные числа методами __eq__(self, other) и __ne(self, other)__.
    # Не добавлял излишне методы аналогичные __radd__(self, other).
    #------------------------------

    def __init__(self, real, imag = 0):
        # Принимает 2 параметра: real, imag - действительная и мнимая части комплексного числа.
        # Исключение составляет, когда запрашивается метод object.to_alg(). Подробнее ниже.
        # Возможен ввод чисто действительного числа, т.к. по умолчанию imag = 0.
        self.storage = {0: real, 1: imag}
        self.real = self.storage[0]
        self.imag = self.storage[1]

    def __add__(self, other):
        # Сложение комплексных чисел эквивалентно сложению их действительных и мнимых частей соответственно.
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        # Вычитание комплексных чисел эквивалентно вычитанию их действительных и мнимых частей соответственно.
        return Complex(self.real - other.real, self.imag - other.imag)

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

    def __eq__(self, other):
        if self.real == other.real and self.imag == other.imag:
            return True
        return False

    def __ne__(self, other):
        if self.real != other.real or self.imag != other.imag:
            return True
        return False

    def __abs__(self):
        return np.sqrt(self.real ** 2 + self.imag ** 2)

    def __setitem__(self, key, value):
        if key not in [0, 1]:
            raise IndexError('There are only 2 indexes. x[0] = Re(x), x[1] = Im(x).')

        self.storage[key] = value
        self.real = self.storage[0]
        self.imag = self.storage[1]

    def __getitem__(self, key):
        if key not in [0, 1]:
            raise IndexError('There are only 2 indexes: x[0] = Re(x), x[1] = Im(x).')
        return self.storage[key]

    def __repr__(self):
        # Меняем repr-описание объекта. Позволяет выводить комплексное число в явном виде.
        return '({}, {})'.format(self.real, self.imag)

    def get_conjugate(self):
        # Получить сопряжённое комплексное число.
        return Complex(self.real, -1 * self.imag)

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
        return '{:.1f}*exp({:.1f}*i)'.format(self.__abs__(), self.get_phi())

    def to_coord(self):
        # Принимает 2 параметра, которым сооответствует модуль комплексного числа и его угол в градусах на комплексной плоскости.
        # Ставит в соответствие комплексное число (пару точек) из нашего класса, вычислив его действительную и мнимую части c точностью до десятых.
        self.m, self.phi = self.real, self.imag

        self.real = self.m * np.cos(self.phi)
        self.imag = self.m * np.sin(self.phi)

        return '({:.1f},{:.1f})'.format(self.real, self.imag)

