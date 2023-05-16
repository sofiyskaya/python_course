# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. 
# Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.

import random

print(my_list := [random.randint(1, 10) for _ in range(5)])

print(sum((my_list.count(i) // 2) for i in set (my_list))) 