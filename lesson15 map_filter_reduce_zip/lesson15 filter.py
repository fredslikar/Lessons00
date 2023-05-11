#фильтр - эта функция используется для фильтрации элементов последовательности, т. е. она получает в качестве аргумента какую-то функцию, которая возвращает
#либо тру либо фолз и последовательность элементы которой она будет фильтровать
#создадим функцию ф которая из чисел будет возвращать только четные числа т.е.:

def f(a):
    if a % 2 == 0:                                  #если число а четное (в записи если остаток при деления а на 2 равер 0) то:
        return a
a = filter(f, (2, 4, 5))
print(list(a))                                      #она должна вернуть из нашей последовательности только четные числа, т.е. отфильтровать согласно нашей функции, если будет тру, то выводится, смотрим


a = filter(lambda x: (x % 2 == 0), (2, 4, 5))
print(list(a))                                      #то же самое только с использованием функции лямбда














    
        







