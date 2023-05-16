# Задача No45. Решение в группах
# Два различных натуральных числа n и m называются дружественными, если сумма делителей числа n (включая 1, но исключая само n) равна числу m и наоборот. 
# Например, 220 и 284 – дружественные числа. По данному числу k выведите все пары дружественных чисел, каждое из которых не превосходит k. 
# Программа получает на вход одно натуральное число k, не превосходящее 105. 
# Программа должна вывести все пары дружественных чисел, каждое из которых не превосходит k. Пары необходимо выводить по одной в строке, разделяя пробелами. 
# Каждая пара должна быть выведена только один раз (перестановка чисел новую пару не дает).

def sum_dividers(number: int) -> int:
    sum_div = 0
    for div in range(1, number // 2 + 1):
        if not number % div:
            sum_div += div
    return sum_div

for num in range(10000):
    if num == sum_dividers(sum_dividers(num)) and num < sum_dividers(num):
        print(num, sum_dividers(num), sep=' \U0001F91D ')        