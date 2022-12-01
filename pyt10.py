# task 1. Реализуйте классы MinStat, MaxStat, AverageStat, которые будут находить минимум,
#  максимум и среднее арифметическое последовательности целых чисел.


# class MinStat:

#     def __init__(self):
#         self.list_int = []

#     def add_number(self, number):
#         self.list_int.append(number)

#     def result(self):
#         if self.list_int == []:
#             return None
#         else:
#             return min(self.list_int)


# class MaxStat:

#     def __init__(self):
#         self.list_int = []

#     def add_number(self, number):
#         self.list_int.append(number)

#     def result(self):
#         if self.list_int == []:
#             return None
#         else:
#             return max(self.list_int)


# class AverageStat:

#     def __init__(self):
#         self.list_int = []

#     def add_number(self, number):
#         self.list_int.append(number)

#     def result(self):
#         if self.list_int == []:
#             return None
#         else:
#             return sum(self.list_int) / len(self.list_int)

# # example 1


# values = [1, 2, 4, 5]

# mins = MinStat()
# maxs = MaxStat()
# average = AverageStat()
# for v in values:
#     mins.add_number(v)
#     maxs.add_number(v)
#     average.add_number(v)

# print(mins.result(), maxs.result(), '{:<05.7}'.format(average.result()))

# # example 2

# mins = MinStat()
# maxs = MaxStat()
# average = AverageStat()

# print(mins.result(), maxs.result(), average.result())

# # example 3

# values = [1, 0, 0]

# mins = MinStat()
# maxs = MaxStat()
# average = AverageStat()
# for v in values:
#     mins.add_number(v)
#     maxs.add_number(v)
#     average.add_number(v)

# print(mins.result(), maxs.result(), '{:<05.7}'.format(average.result()))


# task 2. Реализуйте класс Table, который хранит целые числа в двумерной таблице.
#  При инициализации Table(rows, cols) экземпляру передаются число строк и столбцов
#  в таблице.Строки и столбцы нумеруются с нуля.


# class Table(object):

#     def __init__(self, rows, cols):
#         self._rows = rows
#         self._cols = cols
#         self._table = [[0] * cols for _ in range(rows)]

#     def get_value(self, row, col):
#         return (self._table[row][col] if 0 <= row < self._rows and 0 <= col < self._cols
#                 else None)

#     def set_value(self, row, col, value):
#         self._table[row][col] = value

#     def n_rows(self):
#         return self._rows

#     def n_cols(self):
#         return self._cols

#     def delete_row(self, row):
#         self._table.pop(row)
#         self._rows -= 1

#     def delete_col(self, col):
#         for row in range(self._rows):
#             self._table[row].pop(col)
#         self._cols -= 1

#     def add_row(self, row):
#         self._table.insert(row, [0] * self._cols)
#         self._rows += 1

#     def add_col(self, col):
#         for row in range(self._rows):
#             self._table[row].insert(col, 0)
#         self._cols += 1


# tab = Table(3, 5)
# tab.set_value(0, 1, 10)
# tab.set_value(1, 2, 20)
# tab.set_value(2, 3, 30)
# for i in range(tab.n_rows()):
#     for j in range(tab.n_cols()):
#         print(tab.get_value(i, j), end=' ')
#     print()
# print()

# tab.add_row(1)

# for i in range(tab.n_rows()):
#     for j in range(tab.n_cols()):
#         print(tab.get_value(i, j), end=' ')
#     print()
# print()

# tab = Table(2, 2)

# for i in range(tab.n_rows()):
#     for j in range(tab.n_cols()):
#         print(tab.get_value(i, j), end=' ')
#     print()
# print()

# tab.set_value(0, 0, 10)
# tab.set_value(0, 1, 20)
# tab.set_value(1, 0, 30)
# tab.set_value(1, 1, 40)

# for i in range(tab.n_rows()):
#     for j in range(tab.n_cols()):
#         print(tab.get_value(i, j), end=' ')
#     print()
# print()

# for i in range(-1, tab.n_rows() + 1):
#     for j in range(-1, tab.n_cols() + 1):
#         print(tab.get_value(i, j), end=' ')
#     print()
# print()

# tab.add_row(0)
# tab.add_col(1)

# for i in range(-1, tab.n_rows() + 1):
#     for j in range(-1, tab.n_cols() + 1):
#         print(tab.get_value(i, j), end=' ')
#     print()
# print()


# tab = Table(1, 1)

# for i in range(tab.n_rows()):
#     for j in range(tab.n_cols()):
#         print(tab.get_value(i, j), end=' ')
#     print()
# print()

# tab.set_value(0, 0, 1000)

# for i in range(tab.n_rows()):
#     for j in range(tab.n_cols()):
#         print(tab.get_value(i, j), end=' ')
#     print()
# print()

# for i in range(-1, tab.n_rows() + 1):
#     for j in range(-1, tab.n_cols() + 1):
#         print(tab.get_value(i, j), end=' ')
#     print()
# print()

# tab.add_row(0)
# tab.add_row(2)
# tab.add_col(0)
# tab.add_col(2)

# tab.set_value(0, 0, 2000)
# tab.set_value(0, 2, 3000)
# tab.set_value(2, 0, 4000)
# tab.set_value(2, 2, 5000)

# for i in range(-1, tab.n_rows() + 1):
#     for j in range(-1, tab.n_cols() + 1):
#         print(tab.get_value(i, j), end=' ')
#     print()
# print()
