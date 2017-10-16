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
l_uno.insert(-2, 99)
l_due.insert(-2, 99)
print("Testo la insert con indici negativi 1: l_uno:", l_uno, "l_due: ", l_due)
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
print("Stampo index(3.2, -4, -1) per indici negativi: l_uno:", l_uno.index(3.2, -4, -1), "l_due: ", l_uno.index(3.2, -4, -1))
l_uno.pop()
l_due.pop()
print("Ne faccio il pop(): l_uno:", l_uno, "l_due: ", l_due)
l_uno.pop(0)
l_due.pop(0)
print("Faccio il pop in posizione 0: l_uno:", l_uno, "l_due: ", l_due)
l_uno.pop(2)
l_due.pop(2)
print("Faccio il pop in posizione 2: l_uno:", l_uno, "l_due: ", l_due)
l_uno.pop(-2)
l_due.pop(-2)
print("Faccio il pop in posizione -2: l_uno:", l_uno, "l_due: ", l_due)
# test di copy()
l_uno.insert(0, rl)
l_due.insert(0, rl)
l_tre = l_uno.copy()
l_quattro = l_due.copy()
print("Creo due copie di l_uno e l_due: l_tre dopo aver inserito una "
      "lista in posizione 0:\n l_tre: ", l_tre, "l_quattro: ", l_quattro)
l_tre[2] = 44
l_tre[0][1] = 33
l_quattro[2] = 44
l_quattro[0][1] = 33

print("Modifico l_tre[2]e l_tre[0][1] anche su l_quattro e"
      " stampo le sequenze: \n l_uno:", l_uno, "l_due: ", l_due, "\nl_tre:", l_tre, "l_quattro", l_quattro)

# test di  len, e bool

print("Restituisco la lungezza di l_uno:", len(l_uno), "l_due: ", len(l_due))
l_tre.clear()
print("Restituisco bool di l_uno, l_due e l_tre(dopo aver fatto il clear()): \n"
      " l_uno:", bool(l_uno), "l_due: ", bool(l_due), "l_tre: ", bool(l_tre))
# test di __add__ e __iadd__
l_tre, l_quattro = l_uno, l_due
l_tre += [10, 23]
l_quattro += [10, 23]
print("Faccio una copia di l_uno e l_due in l_tre e l_quattro e poi"
      "l_tre += [10,23] = l_quattro: \n l_uno:", l_uno, "l_due: ", l_due, "\nl_tre:", l_tre, "l_quattro", l_quattro)
l_tre = l_tre + [11, 24]
l_quattro = l_quattro + [11, 24]

print("Ora faccio l_tre = l_tre + [11, 24] = l_quattro "
      "e stampo il risultato: \n l_uno:", l_uno, "l_due: ", l_due, "\nl_tre:", l_tre, "l_quattro", l_quattro)

# test di __le__ , __lt__ , __eq__ , ___ne__, __ge__, __gt__

print("Stampo l_uno == l_due: ", l_uno == l_due)


print("Testo la funzione stampa suffissi (iterativa) sulla 4 liste create precedentemente")
print("l_uno:", l_uno)
print ("Suffissi list_uno")
print(l_uno.stampaSuffissiIterativa())
print("l_due:", l_due)
print ("Suffissi list_due")
print(l_due.stampaSuffissiIterativa())
print("l_tre:", l_tre)
print ("Suffissi list_tre")
print(l_tre.stampaSuffissiIterativa())
print("l_quattro:", l_quattro)
print ("Suffissi list_quattro")
print(l_quattro.stampaSuffissiIterativa())

l_test = MyList("MarioCantalupo")
print ("l_test = ",l_test)
print ("Test iterativo")
print(l_test.stampaSuffissiIterativa())
#print ("Test ricorsivo")
#print(l_test.stampaSuffissiRicorsiva())
l_test[len(l_test):]=111
print (l_test)