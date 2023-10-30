""" -------------- ГЛАВА 1. BIG-O NOTATION И БИНАРНЫЙ ПОИСК -------------- 

Big O notation - это мера эффективности «в худшем случае», то есть верхняя граница того, сколько времени потребуется для выполнения задачи, или сколько памяти для этого необходимо.
O(1) - одна операция для всех возможных входных данных
O(log n) - "разделяй и властвуй"; Кол-во операций равно логарифму кол-ва входных данных n (с основанием 2). Пример: n = 16 => log n = 4
O(n) - количество операций равно кол-ву входных данных (линейная скорость выполнения)
O(n log n) - O(n) + O(log n)
O(n^2) - сложность порядка n квадрат, к примеру два вложенных цикла for
O(2^n) и O(n!) - еще медленнее

Бинарный поиск - тип поискового алгоритма, который последовательно делит пополам заранее ОТСОРТИРОВАННЫЙ массив данных. Если элемент, который нужно найти, присутствует в списке, то бинарный поиск возвращает его позицию, его элемента нет - возвращает null
Время выполнения бинарного поиска - O(log n)
"""


# def binarySearch(list, item):
#     low = 0
#     high = len(list) - 1

#     while low <= high:
#         mid = (low + high) // 2
#         guess = list[mid]
#         if guess == item:
#             return mid
#         elif guess > item:
#             high = mid - 1
#         else:
#             low = mid + 1
#     return None
# list = [1, 3, 7, 8, 12, 20, 23, 28, 36]
# print(binarySearch(list, 23))


""" -------------- ГЛАВА 2. МАССИВЫ И СВЯЗАННЫЕ СПИСКИ, СОРТИРОВКА ВЫБОРОМ -------------- 

Массив - тип данных, все элементы которого хранятся в памяти непрерывно(рядом друг с другом, без пропусков).
Для того, чтобы добавить дополнительный элемент в массив, нужно либо положить его в ячейку памяти обязательно рядом с другими элементами массива без пробелов в ячейках памяти, либо найти новое место в памяти, в котором поместятся все элементы текущего массива + новые элементы, при этом без пропусков между всеми ними

Связанный список - тип данных, каждый элемент которого содержит ссылку на адрес в памяти следующего и/или предыдущего элемента списка, и располагается в произвольных местах памяти
Таким образом, каждый элемент связанного списка может храниться в любых ячейках памяти, не обязательно друг рядом с другом. В связанный список можно без проблем добавлять дополнительные элементы без перезаписи всего списка, тк его элементы, опять же, могут храниться в любых ячейках памяти
Минус связного списка в том, что не получится получить определенный элемент списка так же легко, как в массиве. Элементы списка хранятся в разных ячейках памяти, поэтому, чтобы определить индекс n-го элемента, нужно обратиться к первому элементу, чтобы получить адрес второго элемента, затем обратиться ко второму элементу  для получения адреса третьего - и так далее, пока не доберемся до n-го

Время выполнения задач массивом: Чтение - O(1), Вставка - O(n), Удаление - O(n)
Время выполнения задач списком:  Чтение - O(n), Вставка - O(1), Удаление - O(1)
Массивы обеспечивают быстрое чтение, списки обеспечивают быструю вставку и удаление

Сортировка выбором — алгоритм сортировки, легко обьясняется, но медленно работает. Быстрая сортировка - более эффективный алгоритм
Время выполнения сортировки выбором - O(n^2)
"""


# def findSmallest(arr):
#     smallest = arr[0]
#     smallestIndex = 0
#     for i in range(1, len(arr)):
#         if (arr[i] < smallest):
#             smallest = arr[i]
#             smallestIndex = i

#     return smallestIndex

# def selectionSort(arr):
#     newArr = []
#     for i in range(len(arr)):
#         smallest = findSmallest(arr)
#         newArr.append(arr.pop(smallest))
#     return newArr

# array = [4, 1, 5, 2, 8, 3, 6, 7]
# print(selectionSort(array))


"""-------------- ГЛАВА 3. РЕКУРСИЯ, СТЕК ВЫЗОВОВ -------------- 

Рекусия - вызов функцией самой себя
Стек вызовов - стек, хранящий информацию для возврата управления из подпрограмм (функций) в программу или подпрограмму (при вложенных или рекурсивных вызовах).
При вызове подпрограммы в стек заносится адрес возврата — адрес в памяти следующей инструкции приостанавливаемой программы, а управление передается подпрограмме. При последующем вложенном или рекурсивном вызове в стек заносится очередной адрес возврата и так далее.
При возврате из подпрограммы адрес возврата снимается со стека, и управление передается на следующую инструкцию приостановленной программы (или подпрограммы).
"""


# def countdown(i):
#     print(i-1)
#     if i <= 1: #базовый случай (используется для того, чтобы не было бесконечного рекурсивного цикла)
#         return
#     else:      #рекурсивный случай
#         countdown(i-1)
# countdown(10)

# def fact(x): # стек вызовов с рекурсией
#     if x == 1:
#         return 1
#     else:
#         return x * fact(x-1)
# print(fact(3))


""" -------------- ГЛАВА 4. СТРАТЕГИЯ "РАЗДЕЛЯЙ И ВЛАСТВУЙ", АЛГОРИТМ БЫСТРОЙ СОРТИРОВКИ -------------- 
Стратегия "Разделяй и властвуй" основана на разбиении задачи на уменьшающиеся фрагменты. Если вы используете эту стратегию со списком, то базовым случаем, скорее всего, будет пустой массив или массив из одного элемента.

Алгоритм быстрой сортировки работает так: из массива выбирается опорный элемент(обычно либо первый, либо рандомный), с ним сравниваются остальные элементы и помещаются в два списка справа и слева от опороного элемента(меньшие - в левый список, большие - в правый), дальше, в зависимости от значения, функция рекурсивно повторяется.
"""

# def sum(list):
#     if list == []: #базовый случай
#         return 0
#     return list[0] + sum(list[1:])
# print(sum([1,4,2]))

# def countElements(list):
#     if list == []: #базовый случай
#         return 0
#     return 1 + countElements(list[1:])
# print(countElements([1,3,2,7]))

# def findMax(list):
#     if len(list) == 2: #базовый случай
#         return list[0] if list[0] > list[1] else list[1]
#     return list[0] if list[0] > findMax(list[1:]) else findMax(list[1:])
# print(findMax([1,3,2,6,4]))

# def quickSort(list):
#     if len(list) < 2: #базовый случай
#         return list
#     else:
#         pivot = list[0] #опорный элемент
#         less = [i for i in list[1:] if i < pivot]    # Подмассив элементов, меньших опорного
#         greater = [i for i in list[1:] if i > pivot] # Подмассив элементов, больших опорного
#         return quickSort(less) + [pivot] + quickSort(greater)
# print(quickSort([10,8,3,1,12,5]))


""" -------------- ГЛАВА 5. ХЕШ-ТАБЛИЦЫ (СЛОВАРИ) --------------
Хеш-таблица — это структура данных, которая состоит из хеш-функции и массива. Она позволяет хранить пары ключ-значение и выполнять три операции: операцию добавления новой пары, операцию удаления и операцию поиска пары по ключу.
Время выполнения всех задач(поиск, вставка, удаление) хеш-таблицей в среднем случае - O(1), в худшем - O(n)
"""

# voted = {}
# def check_vote(name):
#     if voted.get(name):
#         print("Вы уже голосовали!")
#     else:
#         voted[name] = True
#         print("Проходите")
# check_vote('max')
# check_vote('tom')
# check_vote('max')

# cache = {}
# def get_page(url):
#     if cache.get(url):
#         return cache[url]
#     else:
#         data = get_data_from_server(url)
#         cache[url] = data
#         return data


""" -------------- ГЛАВА 6. ПОИСК В ШИРИНУ --------------
"""