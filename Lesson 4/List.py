class Node:
    def __init__(self, value,
                 prev_pointer=None, next_pointer=None):
        self.set_value(value)
        self.set_prev(prev_pointer)
        self.set_next(next_pointer)

    def get_value(self):
        return self._value

    def get_next(self):
        return self._next_pointer

    def get_prev(self):
        return self._prev_pointer

    def set_value(self, value):
        self._value = value

    def set_prev(self, prev_pointer):
        self._prev_pointer = prev_pointer

    def set_next(self, next_pointer):
        self._next_pointer = next_pointer

    def __str__(self):
        return str(self.get_value())

class List:
    def __init__(self, collection = None):
        # По умолчанию все на None, если просто создают List().
        self._start_pointer = None
        self._finish_pointer = None
        self._length = 0

        # Чекаем если нам вводят числа через []:
        if isinstance(collection, list):
            for i in collection:
                self.append(i)

        # Чекаем если набор - просто одно число (int или float):
        elif isinstance(collection, int) or isinstance(collection, float):
            self.append(collection)

    def __len__(self):
        return self._length

    def __getitem__(self, i):
        # Обращение к элементу по индексу должно занимать не более чем N/2 операций
        if i < 0 or i >= self._length:
            return False

        if i <= self._length // 2:
            curr_pointer = self._start_pointer
            for j in range(i):
                curr_pointer = curr_pointer.get_next()

        if i > self._length // 2:
            curr_pointer = self._finish_pointer
            for j in range(self._length - i - 1):
                curr_pointer = curr_pointer.get_prev()

        return curr_pointer.get_value()

    def __add__(self, other):
        for i in range(len(other)):
            self.append(other[i])
        return self

    def __radd__(self, other):
        for i in range(len(self)):
            other.append(self[i])
        return other

    def __str__(self):
        arr = []
        for i in range(self._length):
            arr.append(str(self[i]))
        return "[" + ", ".join(arr) + "]"

    def append(self, value):
        if self._length == 0:
            self._start_pointer = Node(value)
            self._finish_pointer = self._start_pointer
            self._length = 1
        else:
            self._finish_pointer.set_next(Node(value,
                                               self._finish_pointer))
            self._finish_pointer = self._finish_pointer.get_next()
            self._length += 1

    def pop(self, index = None):
        # Если захотят pop-нуть не тот индекс
        if index is not None and abs(index) > self._length:
            raise IndexError('Index out of range :((')

        #По умолчанию выбираем последний элемент
        elif index is None:
            index = self._length - 1

        self.arr = []
        for i in range(self._length):
            if i != index:
                self.arr += [self[i]]

        self = List(self.arr)
        return self