"""
Реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>).
Количество генерируемых кортежей не должно быть больше длины списка tutors. Если в списке klasses меньше элементов,
чем в списке tutors, необходимо вывести последние кортежи в виде: (<tutor>, None)
"""

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Cемён', 'Максим', 'Егор']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']


def check_gen(tutors: list, klasses: list):
    n = 0

    for _ in range(1, len(tutors) + 1):
        if n > len(klasses) - 1:                             # Если количество элементов в списке tutore больше чем в
            result_tuple = (tutors[n], None)                 # klasses - вместо недостающих элементов подставляется None
        else:
            result_tuple = (tutors[n], klasses[n])
        n += 1
        yield result_tuple


generator = check_gen(tutors, klasses)
print(f'Доказательство: {type(generator)}')
for _ in range(len(tutors)):
    print(next(generator))
#next(generator)  # если раскомментировать, то должно падать в traceback по StopIteration