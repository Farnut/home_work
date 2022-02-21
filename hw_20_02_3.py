"""Задание 1
Два списка целых заполняются случайными числами.
Необходимо:
■ Сформировать третий список, содержащий элементы
обоих списков;
■ Сформировать третий список, содержащий элементы
обоих списков без повторений;
■ Сформировать третий список, содержащий элементы
общие для двух списков;
■ Сформировать третий список, содержащий только
уникальные элементы каждого из списков;
■ Сформировать третий список, содержащий только
минимальное и максимальное значение каждого из
списков."""

l1 = [2, 2, 4, 6, 8, 10, 3, 5]
l2 = [1, 1, 3, 5, 7, 9, 2, 4]
both = []
both_same = []
both_uniq = []
both_max_min = []
both.extend(l1)  # add list a
both.extend(l2)  # add list b
both_not_rep = list(set(both))  # not repeat
for i in l1:
    if i in both_same:
        continue
    for j in l2:
        if i == j:
            both_same.append(i)  # same elements
l1_max = max(l1)
l1_min = min(l1)
l2_max = max(l2)
l2_min = min(l2)
both_max_min.append(l1_max)
both_max_min.append(l1_min)
both_max_min.append(l2_max)
both_max_min.append(l2_min)
l11 = []
l22 = []
l1_a = l1
l2_b = l2
l1_a.insert(0, 'a')
l2_b.insert(0, 'a')
for elem in l1_a:
    a = l1_a.pop()
    if (a not in l1_a) and a != 'a':
        l11.append(a)
for elem in l2_b:
    b = l2_b.pop(0)
    if (b not in l2_b) and b != 'a':
        l22.append(b)
for elem in l11:
    both_uniq.append(elem)
for elem in l22:
    both_uniq.append(elem)  # unique elements
print(both)
print(both_not_rep)
print(both_same)
print(both_uniq)
print(both_max_min)
