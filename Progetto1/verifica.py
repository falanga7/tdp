from Progetto1.my_list import MyList
from Progetto1.util import *

# test di append
print("Creo l_uno e l_due e verifico che l'append sia uguale su entrambi:")
l_uno = MyList()
l_uno.append("d")
l_uno.append(2)
l_uno.append("abc")
l_uno.append(4)
l_due = MyList(l_uno)
l_due.append("x")
l_uno.append("y")
print("l_uno:", l_uno)
print("l_due:", l_due)

# test di extend
l_tre = MyList()
l_tre.append(3)
l_tre.append(None)
l_tre.append("g")
print(l_tre)
l_uno.extend(l_tre)
l_due.extend(l_tre)
rl=randList(1, 10, 3)
rkl=rand_keys_list(3, 1, 10)
rs=random_string(5)
rwl=rand_words_list(10, 3, 7)
rd=rand_dict(12)

print(l_tre)
l_quattro = l_tre.copia()
l_quattro.append(1000)
print(l_tre)
print(l_quattro)