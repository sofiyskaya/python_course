# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался. 
# Количество повторов добавляется к символам с помощью постфикса формата _n.
# Для решения данной задачи используйте функцию .split()

my_string = 'a a v b c a b d d c a b'
my_list = my_string.split()

res = {}
for i in my_list:
    print(i if i not in res else f'{i}_{res[i]}', end = ' ')
    res[i] = res.get(i, 0) + 1
          