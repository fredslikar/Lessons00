a = 45
b = 5
def f(a):
    a = a + 2
    print (a)

f(b)

name = 'Hello, world!'
for i in name :
    print (i)

name = 'Hello, world!'
for i in range(1,11) :
    print (name)


i = 0
while i<=11:
    print (i)
    i=i+2

i = 0
while i<=11:
    print (i)
    i=i+1
    break

i = 1
while i<=10:
    if i != 5:
        print (i)
    i=i+1
    continue
