def f1():
    return [i for i in range(17,100) if i % 17 == 0]


def f2():
    return [i for i in range(1000) if '2' in str(i)]


def f3():
    return [i for i in range(10000) if str(i) == str(i)[::-1]]


def f4(string):
    return string.count(' ')


def f5(string):
    return ''.join([i for i in string.lower() if i not in 'aeiou'])


def f6(string):
    return list(filter(lambda w: len(w) < 6, string.split()))


def f7(string):
    return {i: len(i) for i in string.split()}


def f8(string):
    return list(set([i for i in string.lower() if i.isalpha()]))


def f9(arr):
    return list(map(lambda x: x**2, arr))


def f10(arr):
    return {dot: (dot[0]**2 + dot[1]**2)**0.5 for dot in arr if dot[1] == 5 * dot[0] - 2}


def f11():
    return list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, range(2, 27))))


def f12(arr):
    return max([(dot[0]**2 + dot[1]**2)**0.5 for dot in arr if dot[0] > 0 and dot[1] > 0])


def f13(arr1, arr2):
    return [tuple(pair) for pair in zip(map(lambda x, y: x+y, arr1, arr2), map(lambda x, y: x-y, arr1, arr2))]


def f14(arr):
    return list(map(lambda  x: str(x) ,filter(lambda x: int(x)**2 % 2 == 0, arr)))


def f15(text):
    cols = [dict(zip(list(zip(*[row.split(',') for row in text.split('\n')]))[0], resume)) for resume in list(zip(*[row.split(',') for row in text.split('\n')]))[1:]]
    return cols


def f16(arr):
    return [sum(col) for col in zip(*arr)]


def main():
    string = 'A simple sentence has the most basic elements that make it a sentence: a subject a verb and a completed thought'
    print('Найти все числа от 1 до 1000, которые делятся на 17')
    print(f1())
    print('Найти все числа от 1 до 1000, которые содержат в себе цифру 2')
    print(f2())
    print('Найти все числа от 1 до 10000, которые являются палиндромом	')
    print(f3())
    print('Посчитать количество пробелов в строке')
    print(f4(string))
    print('Есть любая последовательность непробельных символов латинского алфавита, удалить все гласные из этого слова')
    print(f5(string.replace(' ', '')))
    print('На входе строка со словами, разделенными через 1 пробел. Найти все слова, длина которых не больше 5')
    print(f6(string))
    print('На входе строка со словами, разделенными через 1 пробел. Получить словарь, где в качестве ключа используется само слово, а в значении длина этого слова.')
    print(f7(string))
    print('На входе предложение со всеми пробельными и непробельными символами латинского алфавита. Получить словарь используемых букв в строке, то есть на выходе список уникальных букв')
    print(f8(string))
    print('На входе список чисел, получить список квадратов этих чисел / use map')
    print(f9([1, 8, 11, -1, 0]))
    print('На входе список координат, например, [(1, 1), (2, 3), (5, 3)]. Найти все точки, которые принадлежат прямой y = 5 * x - 2. '
          'На выходе получить словарь из самой точки и расстоянии до этой точки из начала координат (0, 0)')
    print(f10([(0, 0), (3, 4), (2, 8), (-1, -7)]))
    print('Возвести в квадрат все четные числа от 2 до 27. На выходе список.')
    print(f11())
    print('На входе список из координат точек на плоскости. Найти расстояние до самой удаленной точку от начала координат (0, 0) в первой четверти')
    print(f12([(-2, -3), (1, 1), (10, 2), (10, -3)]))
    print('На входе два списка чисел nums_first = [1, 2, 3, 5, 8] и nums_second = [2, 4, 8, 16, 32]. Получить пары сумм и разниц, [(3, -1), (6, -2), (11, -5), ...]')
    print(f13([1, 2, 3, 5, 8], [2, 4, 8, 16, 32]))
    print("На входе список строк из чисел, например, ['43141', '32441', '431', '4154', '43121']. Найти четные квадраты этих чисел. Ответ записать снова в список из строк, то есть сформировать обратно список строк, но уже отфильтровать все четные квадраты.")
    print(f14(['43141', '32441', '431', '4154', '43121']))
    print('''Менеджер как обычно придумал свое представление данных, а нам оно не подходит

input_str = """name,Petya,Vasya,Masha,Vova
grade,5,5,8,3
subject,math,language,physics,math
year,1999,2000,1995,1998"""''')
    print("""Мы хотим получить нормальную таблицу, чтобы импортировать в csv


[
  {
    'name': 'Petya',
    'grade': '5'
    'subject': 'math'
    'year': '1999'
  },
  {
    'name': 'Vasya',
    'grade': '5'
    'subject': 'language'
    'year': '2000'
  },
  ...
]""")
    print(f15("""name,Petya,Vasya,Masha,Vova
grade,5,5,8,3
subject,math,language,physics,math
year,1999,2000,1995,1998"""))
    print('Получить сумму по столбцам у двумерного списка')
    print(f16([[11.9, 12.2, 12.9], [15.3, 15.1, 15.1], [16.3, 16.5, 16.5], [17.7, 17.5, 18.1]]))


if __name__ == "__main__":
    main()
