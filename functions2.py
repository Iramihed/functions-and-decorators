# Написать функцию, которая определяет количество разрядов введённого целого числа.
def func(x):
    return len(str(x))
a = int(input('num: '))
print(func(a))
