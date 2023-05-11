from socket import gaierror


spisok = []

x = [3,4,5,9,10]
print(x)

y = [3,5,34.1,'name']
print(y)

z = [3,5,34.1,'name', [45,7]]
print(z)

name1 = 'Kesha'
name2 = 'Igor'
name3 = 'Gloves'

print(name1)
print(name2)
print(name3)

names = ['Kesha','Igor','Gloves']
print (names)

names = ['Kesha','Igor','Gloves']
print (names[-1])

for go in names:
    print(go)

names.append ('Kiborg')
print (names)

names.append ('Sleg')
names.append('Flag')

for go in names:
    print(go)

names.pop()
print(names)

n = names.index('Kiborg')
print(n+1)

v = len(names)
print(v)

numbers = [4,8,125,15,75,21,54,7,4]
numbers.sort()
print(numbers)

numbers2 = [4,8,125,15,75,21,54,7,4]
numbers2.sort(reverse=True)
print(numbers2)

numbers3 = [4,8,125,15,75,21,54,7,4]
numbers3[1] = 111
numbers3.sort()
print(numbers3)

leters = ['aaa','dddd','vvv','c','s','d','f','a','c']
leters[1] = 'x'
leters.sort()
print(leters)

numbers4 = [4.5,8.2,125.1,15.2,75,21.1,54,7,4]
numbers4[1] = 111.7
numbers4.sort()
print(numbers4)

tuple1 = ('dte','dfdf',25.1,1.1,)
print(tuple1)

tuple2 = ('dte','dfdf',25.1,1.1,)
print(type(tuple2))

print(tuple([45,25,86,27,38]))

print(tuple(numbers4))

print(list((35,56,78,1114,)))

print(list((tuple2)))

dict = {"aple": "red",}         #ключ и значение#
print(dict)

#теперь нам нужно вывести ключи (первые перед двуеточиями), используем кийс и цикл#
dict2 = {"aple": "red", "banana":"yelow","kivi":"green","lemon":"yelow",}
for k in dict2.keys():
    print(k)

#теперь нам нужно вывести ЗНАЧЕНИЯ (первые перед двуеточиями), используем валуэ и цикл#
dict3 = {"aple": "red", "banana":"yelow","kivi":"green","lemon":"yelow",}
for k in dict3.values():
    print(k)

#теперь нам нужно вывести Все (первые перед двуеточиями), используем айитемс и цикл#
dict4 = {"aple": "red", "banana":"yelow","kivi":"green","lemon":"yelow",}
for k in dict4.items():
    print(k)

#Если нужно вывести, к примеру, значение со второй пры по ключу то указываем ключ таким образом [vvv] ....#
dict5 = {"aple": "red", "banana":"yelow","kivi":"green","lemon":"yelow",}
print(dict5["banana"])

#Изменение значения для ключей в списке...#
dict6 = {"aple": "red", "banana":"yelow","kivi":"green","lemon":"yelow",}
dict6["banana"] = "green"
print(dict6)

#Удаление ключа и значения#
dict7 = {"aple": "red", "banana":"yelow","kivi":"green","lemon":"yelow",}
del(dict7["banana"])
print(dict7)



