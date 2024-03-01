def print_sequence(n):
    """Выводит n первых элементов последовательности 122333444455555… (число повторяется столько раз, чему оно равно)"""
    line = ''

    for i in range(1, n + 1):
        line += (str(i) * i)

    return line


element = int(input('Введите число: '))
print(print_sequence(element))
