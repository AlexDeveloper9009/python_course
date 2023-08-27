#22
# n = int(input("Введите количество элементов первого множества: "))
# m = int(input("Введите количество элементов второго множества: "))
#
# set1 = set()
# set2 = set()
#
# print("Введите элементы первого множества:")
# for i in range(n):
#     element = int(input())
#     set1.add(element)
#
# print("Введите элементы второго множества:")
# for i in range(m):
#     element = int(input())
#     set2.add(element)
#
# intersection = set1 & set2
# sorted_intersection = sorted(intersection)
#
# print("Числа, которые встречаются в обоих множествах:")
# for num in sorted_intersection:
#     print(num)
#22 - другое решение
# n = int(input("Введите количество элементов первого множества: "))
# m = int(input("Введите количество элементов второго множества: "))
#
# set1 = set()
# set2 = set()
#
# print("Введите элементы первого множества:")
# for i in range(n):
#     element = int(input())
#     set1.add(element)
#
# print("Введите элементы второго множества:")
# for i in range(m):
#     element = int(input())
#     set2.add(element)
#
# intersection = sorted(set1.intersection(set2))
#
# print("Числа, которые встречаются в обоих множествах:")
# for num in intersection:
#     print(num)
# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты высажены
# только по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом
# кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего
# модуля и нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым
# кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль,
# находясь перед некоторым кустом заданной во входном файле грядки.
# def max_berries(garden):
#     n = len(garden)
#     max_berries = 0
#
#     for i in range(n):
#         berries = garden[i] + garden[(i - 1) % n] + garden[
#             (i + 1) % n]  # суммируем ягоды с текущего куста и двух соседних
#         max_berries = max(max_berries, berries)  # обновляем максимальное число ягод
#
#     return max_berries
#
#
# # Пример использования
# garden = []
# n = int(input("Введите количество кустов черники: "))
# print("Введите количество ягод на каждом кусте:")
# for i in range(n):
#     berries = int(input())
#     garden.append(berries)
#
# max_berries = max_berries(garden)
# print(f"Максимальное число ягод: {max_berries}")