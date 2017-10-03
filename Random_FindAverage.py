"""Создать массив из 1000 элементов и рандомно заполнить его числами от -1000 до 1000.
Найти среднее арифметическое всех элементов. Создать другой массив и записать в него все элементы,
которые на +- 20 % отличаются от среднего."""
from random import randint
random_list = []
while len(random_list) < 1000:
    random_list.append(randint(-1000, 1000))
    len(random_list)
print(random_list)
average = sum(random_list)/len(random_list)
print(average)
new_list = []
print(average * 0.8, average * 1.2)
if average > 0:
    for element in range(int(average * 0.8), int(average * 1.2 + 1)):
        new_list.append(element)
elif average < 0:
    for element in range(int(average * 1.2), int(average * 0.8+1)):
        new_list.append(element)
print(new_list)
