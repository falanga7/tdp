from Progetto1.my_list import MyList
from Progetto1.util import *


rl = randList(1, 10, 3)
rkl = rand_keys_list(3, 1, 10)
rs = random_string(5)
rwl = rand_words_list(10, 3, 7)
rd = rand_dict(12)

# test di append(x) + clear()
print("Creo l_uno e l_due e verifico che l'append sia uguale su entrambi:")
l_uno = MyList()
l_uno.append("d")
l_uno.append(2)
l_uno.extend("abc")
l_uno.append(4)
print("l_uno:", l_uno)
l_due = MyList(l_uno)
print("l_due:", l_due)
l_due.append("dieci")
print("l_due con append di dieci:", l_due, "!= l_uno:", l_uno)
l_uno.append("dieci")
print("l_uno con append di dieci:", l_uno, "== l_due:", l_due)
l_uno.append(rl)
print("append con lista causale su l_uno:", l_uno)
l_uno.clear()
l_uno.append(rkl)
print("clear + append con random key list:", l_uno)
l_uno.append(rs)
print("append di stringa causale:", l_uno)
l_uno.append(rwl)
print("append di parole causali", l_uno)
l_uno.append(rd)
print("append di un dizionario causale", l_uno)
l_uno.clear()
l_due.clear()
print("clear su l_uno e l_due: l_uno:", l_uno, "== l_due:", l_due)
# test di insert(i,x)
# test con indice non definito
# l_uno.insert(3, 4)
l_uno.append(5.4)
l_uno.append(3.2)
l_due = MyList(l_uno)
print("Ridefinisco l_uno:", l_uno, "e l_due:", l_due)
l_uno.insert(0, "bc")
l_due.insert(0, "bc")
print("Testo la insert in posizione 0: l_uno:", l_uno, "l_due: ", l_due)
l_uno.insert(3, 22)
l_due.insert(3, 22)
print("Testo la insert in posizione 3: l_uno:", l_uno, "l_due: ", l_due)
l_uno.insert(1, 50)
l_due.insert(1, 50)
print("Testo la insert in posizione 1: l_uno:", l_uno, "l_due: ", l_due)
# test remove(x)
l_uno.remove(50)
l_due.remove(50)
print("Testo la rimozione di 50 : l_uno:", l_uno, "l_due: ", l_due)
l_uno.remove("bc")
l_due.remove("bc")
print("Testo la rimozione di bc: l_uno:", l_uno, "l_due: ", l_due)
l_uno.remove(22)
l_due.remove(22)
print("Testo la rimozione di 22: l_uno:", l_uno, "l_due: ", l_due)
# test di pop([i]) ed extend(iterable), count(x), reverse(), __setitem__,  index(x[, start[, end]])
l_uno.extend(rl)
l_due.extend(rl)
print("Estendo le due liste con una lista causale: l_uno:", l_uno, "l_due: ", l_due)
l_uno.reverse()
l_due.reverse()
print("Ne stampo il reverse: l_uno", l_uno, "l_due: ", l_due)

l_uno[0] = 3
l_uno[2] = 3
l_uno[4] = 3
l_due[0] = 3
l_due[2] = 3
l_due[4] = 3
print("Imposto tre 3 alle liste con l'operatore __setitem__: l_uno:  ", l_uno, "l_due: ", l_due)
print("Stampo il numero di 3 nelle liste: l_uno: ", l_uno.count(3), "l_due: ", l_due.count(3))
print("Stampo index(3): l_uno:", l_uno.index(3), "l_due: ", l_due.index(3))
print("Stampo index(3,1,3): l_uno:", l_uno.index(3, 1, 3), "l_due: ", l_due.index(3, 1, 3))
l_uno.pop()
l_due.pop()
print("Ne faccio il pop(): l_uno:", l_uno, "l_due: ", l_due)
l_uno.pop(0)
l_due.pop(0)
print("Faccio il pop in posizione 0: l_uno:", l_uno, "l_due: ", l_due)
l_uno.pop(2)
l_due.pop(2)
print("Faccio il pop in posizione 2: l_uno:", l_uno, "l_due: ", l_due)
# l_uno.insert(3, 22)
# l_due.insert(3, 22)
# print("Testo la insert in posizione 3: l_uno:", l_uno, "l_due: ", l_due)
# l_uno.insert(1, 50)
# l_due.insert(1, 50)







# # test di extend
# l_tre = MyList()
# l_tre.append(3)
# l_tre.append(None)
# l_tre.append("g")
# print(l_tre)
# l_uno.extend(l_tre)
# l_due.extend(l_tre)

#
# print(l_tre)
# l_quattro = l_tre.copia()
# l_quattro.append(1000)
# print(l_tre)
# print(l_quattro)
#
# a = MyList()
# a.append(7)
# a.append(2)
# a.append(3)
# a.append(4)
# a.append(5)
# a.append(6)
# print(a)
# a._insertion_sort()
# print(a)
# b = ['M','a']
# c = {'8','9','10'}
# print(a)
# print(b)
# c = a + b
#
#
# a+=b
# print(a)
# print(b)
# print(c)
# print(a==a)
# print(a.__contains__('f'))

# a += b
# print(a)
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

