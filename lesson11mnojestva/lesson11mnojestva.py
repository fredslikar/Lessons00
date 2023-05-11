numbers1 = {1, 2, 4, 67}    #�������� ��������� ��������� ��������. ���������� ��������� ����� ���� ����� � ��. �������, �� �� ����� �����������
print(numbers1)          

print(type(numbers1))    #������� ��� ���������

numbers2 = set()    #�������� ������ ���������, ��� ����� ����� ��������������� �������� ���
print(type(numbers2))

numbers3 = set([1, 1, 2, 4, 2, 55, 8, 2, 7, 3, 0])        #���������� ��� ������ �� ���������, ��� ���� �������� ��, ��� �� �������� �� ����������� �� ����������� ��������(���� ����������)
print(numbers3)   #������� ��� � ��� ���������� (�������� ���������)
for i in numbers3:                #������� ��������� ���������� � ������
    print(i)
print(3 in numbers3)              #��������� ���� �� �� ��������� ����� ��� (��� ��� �����)
print(58 in numbers3)             #��������� ���� �� �� ��������� ����� 58 (��� ��� �����)

numbers3.add(58)                  #��������� ������� 58 � ��������� ��������� � ������� ������ ���
print(numbers3)

numbers3.discard(33)              #����� ������� ���������� ����� ������� ��� �����(������ ���� ���������� �����, �� ���� �������� ���, �� ����� ������)
print(numbers3)

numbers3.remove(58)              #������ ���� ���������� �����, �� ���� �������� ���, �� ����� ������
print(numbers3)

numbers3.pop()                  #� ������� ������ ��� ������� ������ ������� �� ���������
print(numbers3)

numbers3.clear()                  #� ������� ������ clear ������� ��� �������� ���������
print(numbers3)


numbers4 = {1, 8, 7, 6, 3, 2, 1, 0}
numbers5 = {4, 33, 77, 6, 3, 2, 1, 0}
numbers6 = numbers1.union(numbers4.union(numbers5))                  #����������� ���������� �������� �� ��� ��� ����� ���������� ����� ����� (��� �������� ���� ��� ���������� ������������ � ����� ����������)
print(numbers6)

                                                                     
numbers7 = {48, 89, 227, 67, 3, 2, 1, 0}                             #����������� ���������� �������� �� ��� ��� ����� ���������� ������������ �����
numbers8 = {4, 433, 377, 677, 3, 2, 1, 0}
numbers9 = numbers7 | numbers8 | numbers6                  
print(numbers9)

numbers10 = numbers6.intersection(numbers7.intersection(numbers8))
numbers11 = numbers6.intersection(numbers7)
print(numbers10)                                                        #������ ����������� ��������, �.�. �������� � ����� ��������� ������ ��� ��������� ������� � �������� � �� ���� ��������� ����������
print(numbers11) 


numbers10 = numbers6 & numbers7 & numbers8
numbers11 = numbers6 & numbers7
print(numbers10)                                                        #���� ����� � �������������� ������� & (������ ����������� ��������, �.�. �������� � ����� ��������� ������ ��� ��������� ������� � �������� � �� ���� ��������� ����������
print(numbers11) 

numbers10 = numbers6 - numbers7 - numbers8
numbers11 = numbers6 - numbers7
print(numbers10)                                                        #�������� � ������ ��������� �� ��������, ������� ���� � ������ ��������� ���� �����
print(numbers11)

numbers11 = numbers6.copy()                                                        #�������� ���� ��������� � ������ � ������� ����, �� � ������ ��� ��� ������ � ������� = (���� �� ���� � ��� �������)
print(numbers11)
print(numbers6)

numbers11 = numbers6                                                        #�������� ���� ��������� � ������ � ������� ����, �� � ������ ��� ��� ������ � ������� = (���� �� ���� � ��� �������)
print(numbers11)
print(numbers6)

print(len(numbers11))                                                        #��� ������ ���������� ��������� � ��������� ���������� ���

numbers12 = frozenset({3, 2, 7, 4, 3, 8})                                    #������� ���������, ������� ������ ����� �������� � ������� ������� ���������
print(numbers12)






