# Найти сумму цифр числа с помощью рекурсии. 112 = 4

n=int(input("Введите число : "))
def sum_hujy (n):
    if n==0:
        return 0
    return (n % 10 + sum_hujy(int(n / 10)))
    dis=n%10

print(sum_hujy(n))