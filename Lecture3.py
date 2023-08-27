# def sum_Numbers(n): # ставим : в функции
#     summa = 0
#     for i in range(1, n+1):
#         summa+=i
#     print(summa)
#
# sum_Numbers(6)

# def sum_str(*args): #Указали пайтону что хотим передавать неограниченное кол-во аргументов *
#     res = '' #создали переменную res - тип данных строка
#     for i in args: #пройдемся по всем элементам переменной args
#         res += i # при каждой итерации добавляем к переменной res наш i
#     return res #вернем нашу переменную res
# print(sum_str('q', 'w', 'r')) #вызываем нашу функцию и передаем в нее аргументы q w r и просим распечатать
# print(sum_str('q', 'w', 'r','rr', '123')) #вызываем нашу функцию и передаем в нее аргументы q w r и просим распечатать

# import module #первый вариант импорта функции из другого файла
# print(module.max1(5,7))

# from module import max1 #импортировали напрямую
# #from  module import * такой вариант импорта импортирует все функции из
# print(max1(7, 9))

# import module as m1 #импортировали функцию module и переименовали ее для дальнейшего использования
# print(m1.max1(10 , 24)) #m1.max1 вызвали функцию из импортированного модуля

# Рекурсия
# 💡 Рекурсия — это функция, вызывающая сама себя.
# С рекурсией Вы знакомы с C#, в Python она ничем не отличается, давай рассмотрим
# следующую задачу: Пользователь вводит число n. Необходимо вывести n - первых
# членов последовательности Фибоначчи.
# Напоминание: Последовательно Фибоначчи, это такая последовательность, в
# которой каждое последующее число равно сумму 2-ух предыдущих
# 💡 При описании рекурсии важно указать, когда функции надо
# остановиться и перестать вызывать саму себя. По-другому говоря, необходимо
# указать базис рекурсии
# def fib(n):
#     if n in [1,2]:
#         return 1
#     return fib(n-1)+fib(n-2)
# list_1=[]
# for i in range(1,20):
#     list_1.append(fib(i))
# print(list_1)

#Сортировка пузырьком
# def quick_sort(array):
#     if len(array) <= 1:
#         return array
#     else:
#         pivot = array[0]
#     les =[i for i in array[1:]if i <= pivot]
#     greater = [i for i in array[1:]if i > pivot]
#     return quick_sort(les) + [pivot] +quick_sort(greater)
# print(quick_sort([13,5,6,9,0,234,1]))

#Сортировка слиянием
def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums)//2
        left = nums[:mid]
        right = nums[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i+=1
            else:
                nums[k]= right[j]
                j+=1
            k+=1
        while i < len(left):
            nums[k]=left[i]
            i+=1
            k+=1
        while j < len(left):
            nums[k]=right[j]
            j+=1
            k+=1
list_1 = [1,5,7,4,5,9,23,29,2134,236,312,119]
merge_sort(list_1)
print(list_1)