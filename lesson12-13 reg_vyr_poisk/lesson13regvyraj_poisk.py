#���������� ��������� - �������� ���� ��� ������������, ������� �������� � ���� ��������
#���������� ��������� ����� ����� ������� �� ���������� �� ������� ������������� ��������������
#���������� ��������� - ��� ������, ������� ������ ������ ������ �������� � �����-���� ������ (������ �� �������� �������������� �����)
#����� ������������� ������ �� 
#������� ������� �
#������ ����� - ����, �� ���� �� ��������� ������� ���������� ������ � ������ ������ (� ������ ��������� ��, ��� ����� ������ � ����� ������� ��� ����� ������ - � ����� ������ ������ �) 
#���� ������� � ������ �� ����� - ������ ����
#���������� ��������� ���������������� - ����� ������� ��� ��������� �����



#����� ���� - ���� �� ���������� ���� ������ � ���������� ������ ���������
#���� ����� ������� ��� �������� ������� ���� ������ ������� ��������, �� � �������� � ���������� ������� ��������� ����
import re
x = "s8b7a65188 jfklsjjl------------sfhsfilDJKFJDKJLSDFe yo pauf io \7\ajkfjl jla jf j jafFF8846FFFsdfs        _____+++---fw fFF!!!! yu foi488ac/dsfs/dsfsdf/dfs/dfsf/sdfsdf/dfds/dfdf/sdsa/asdf"

#����� �� - �������� ��� ���� ������ ����������� "�����" - ������ � ������� ��������� �������������(��� �� ��������� ���������� ����� ��������������� ����� ��������� � �. �. � ������������)
#��������� ������� �������� ���� �� ���� ������ � ������� ������ (�.��)

result0 = re.search(r"s.h", x)  
print (result0)

result1 = re.search(r"s..h", x)  
print (result1)

#�������� ���� � - ������� ����� ������ �����, ���� ������ ��������� ��� - ������ ������� ������ ���������������� �����

result2 = re.search(r"\d", x)  
print (result2)

result3 = re.search(r"\d\d", x)  
print (result3)

result4 = re.search(r"\d\d\d\d", x)  
print (result4)

#�������� ���� ������� � - ������� ����� ������ ������, ����� �����, ���� ������ ��������� ��� - ������ ������� ������ ���������������� ������

result5 = re.search(r"\D", x)  
print (result5)

result6 = re.search(r"\D\D\D\D", x)  
print (result6)

#�������� ���� c - ������� ����� ������ ���������� ������ (������, ���� ��������� � ����� ������)

result7 = re.search(r"\s", x)  
print (result7)

#�������� ���� ������� � - ������� ����� ������ ������������ ������ (������, ���� ��������� � ����� ������)

result7 = re.search(r"\S", x)  
print (result7)

#�������� ���� w - ������� ����� �����, ����� ��� ������ �������������

result8 = re.search(r"\w", x)  
print (result8)
result9 = re.search(r"\w\w\w\w\w\w\w\w\w\w\w\w", x)  
print (result9)

#�������� ���� ������� W - ������� ����� ������, ����� �����, ����� ��� ������� �������������

result10 = re.search(r"\W", x)  
print (result10)
result11 = re.search(r"\W\W\W", x)  
print (result11)

#�������� ���� � � �� ��� ������� - �������� ������ ������ ��� ����� ����� (����� ���������� ���������) �� ��������� ��������

result12 = re.search(r"\bjf", x)  
print (result12)

#�������� ���� ������� � � �� ��� ������� - �������� ������ �������� � ������� ����� (�.�. ��������) (����� ���������� ���������) �� ��������� ��������

result13 = re.search(r"\Bjf", x)  
print (result13)


result14 = re.search(r"\Bfk", x)  
print (result14)

#�������� ���� �* - ������� ���� ��� ����� ��������� ����

result15 = re.search(r"\d*", x)  
print (result15)

#�������� ���� �+ - ������� ���� ��� ����� ��������� ����

result16 = re.search(r"\d+", x)  
print (result16)

#� ���������� ������� ��������� ���������� ����� ��������, ������� �� ����, � ����� �� ��� ��� ���������� ����� �������

result17 = re.search(r"[s8aaas]", x)  
print (result17)

#� ���������� ������������ ����� ������� �������� ����� ��� ����, �� �������� ������ ��������� ����� ����� ��������

result18 = re.search(r"[4-8]", x)  
print (result18)

result18 = re.search(r"[a-f]", x)  
print (result18)

#� ���������� ������������ ����� ������� �������� ����� ��� ����, �� �������� ������ ��������� ����� ����� ��������
#���� ����� ����� ������ ������, ����� ��������� ��� ��������� ��������, �� ����� ���� ������������ ���� ^

result19 = re.search(r"[^4-8]", x)  
print (result19)

result20 = re.search(r"[^a-f]", x)  
print (result20)

#���� ����� ����� ���� ����� ������ ���� ������, �� ����� ���� ���������� ������������ �����, ������� �������� ������, ��� � ����� �������(��������� �� ���������� ����� ����)

result21 = re.search(r"[4|8]", x)  
print (result21)

result22 = re.search(r"[x|f|4]", x)  
print (result22)

#������������� - ���������� ���������� ������������ ��������� � ������ (������������ ����� � �������� ������)
#�������� ������������� ������, ��. ����

result23 = re.search(r"\d{4}", x)  
print (result23)

result24 = re.search(r"\d\d\d\d", x)  
print (result24)

result25 = re.search(r"\w\w\w\w\w\w\w\w\w\w\w\w", x)  
print (result25)

result26 = re.search(r"\w{12}", x)  
print (result26)

#���� ����� �������, ��������, �� 1 �� 12 ���������� �� ���������� ���� �������� ����� ������� � �������� �������


result27 = re.search(r"\w{1,12}", x)  
print (result27)

#���� ����� ������� �� ��������� �����, �� ��� �������� ���������� �� ����� ��� �����, ��������

result28 = re.search(r"\w{12,}", x)  
print (result28)

#���� �� ������� �� ��������� �����, �� ��� �������� ���������� �� ����� ��� �����, ��������

result29 = re.search(r"\d{,4}", x)  
print (result29)

#������� ����� ������� ��� �����, ������� ���������� �� ��������� ����� � ��������� �����

p = "Hi! How are you? Sanks, I'm fine! Avto is good!"

#��� ����� ���������� ����� ��������

result30 = re.findall(r"[qwrtpsdfghjklzxcvbnmyQWRTYPSDFGHJKLZXCVBNM]\w+", p)
print (result30)



