#{} - такие скобки означают множество или словарь
#генератор списка = [финальное выражение, Коллекция, условие]
#Задача - взять список и создать из него множество используя генератор множеств(напоминаю, множество не хранит в себе дубликаты и словари тоже - все значения в них будут уникальными)

s = [7, 8, 8, -10, -10]
set1 = {i for i in s}

print(set1)

s2 = [7, 8, 8, -10, -10]
dict1 = {i : i**10 for i in s}

print(dict1)































