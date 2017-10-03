"""Сгенерировать массив из задачи b. Найти 2 максимальных элемента данного массива. Элементы не должны быть равны."""
from random import randint
random_list = []
while len(random_list) < 1000:
    random_list.append(randint(-1000, 1000))
    len(random_list)
remove_doubles = set(random_list)
find_max = sorted(list(remove_doubles), reverse=True)
print(find_max[0:2])
