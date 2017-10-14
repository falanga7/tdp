from Progetto1.my_list import MyList
from Progetto1.util import *

# # test di append
# print("Creo l_uno e l_due e verifico che l'append sia uguale su entrambi:")
# l_uno = MyList()
# l_uno.append("d")
# l_uno.append(2)
# l_uno.extend("abc")
# l_uno.append(4)
# print("l_uno:", l_uno)
# l_due = MyList(l_uno)
# l_due.append("x")
# l_uno.append("y")
# print("l_uno:", l_uno)
# print("l_due:", l_due)
#
# # test di extend
# l_tre = MyList()
# l_tre.append(3)
# l_tre.append(None)
# l_tre.append("g")
# print(l_tre)
# l_uno.extend(l_tre)
# l_due.extend(l_tre)
# rl=randList(1, 10, 3)
# rkl=rand_keys_list(3, 1, 10)
# rs=random_string(5)
# rwl=rand_words_list(10, 3, 7)
# rd=rand_dict(12)
#
# print(l_tre)
# l_quattro = l_tre.copia()
# l_quattro.append(1000)
# print(l_tre)
# print(l_quattro)

a = MyList()
a.append(1)
a.append(2)
a.append(3)
a.append(4)
a.append(5)
a.append(6)
b = ['M','a']
c = {'8','9','10'}
print(a)
print(b)
c = a + b


a+=b
print(a)
print(b)
print(c)
print(a==a)
print(a.__contains__('f'))
#print(a[2])
#a.insert(3, 18)
#print(a)
#a.reverse()
#a.insert(2, 22)
#print(a)
#a.insert(-4, 999)
#print(a.count(1))
# a.append(7)
# print(a)
# print(a)
# a.insert(1,100)
# print(a)
# a.remove(100)
# b=a.copy()
# b.append(888)
# print(a)
# print(b)
# b.extend(a)
# print(b)

