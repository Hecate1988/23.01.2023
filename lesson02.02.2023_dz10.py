import keyword
from keyword import kwlist
a = input("Введите строку")
c =  a == a.lower() and (a.isalnum() or a.find('_') != -1) and not a.isdigit() and not a[0].isdigit() and not keyword.iskeyword(a)
print(c)
