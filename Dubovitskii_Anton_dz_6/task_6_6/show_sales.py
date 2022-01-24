def main(start: int = 1, end: int = 0):
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        line = f.readlines()
        if end > 0:                                    # Исполняется если задан второй аргумент
            for i in range(start - 1, end):
                print(line[i].strip())
        else:
            for i in range(start - 1, len(line)):        # Исполняется если задан один аргумент или ни одного
                print(line[i].strip())


if __name__ == '__main__':
    import sys
    if len(sys.argv) == 1:
        exit(main())
    elif len(sys.argv) == 2:
        p, first_arg = sys.argv
        exit(main(int(first_arg)))
    elif len(sys.argv) == 3:
        p, first_arg, second_arg = sys.argv
        exit(main(int(first_arg), int(second_arg)))
    else:
        print('Ошибка, введите от 0 до 2 значений')

