from Gruppo6_2_TdP.TdP_collections.map.avl_tree import AVLTreeMap
from Gruppo6_2_TdP.pkg_i.util import rand_words_list
from Gruppo6_2_TdP.TdP_collections.map.red_black_tree import RedBlackTreeMap
import time


def test_trees_insertion(n):

    # genero una lista casuale di n valori che poi inserirò in entrambi gli alberi
    rwl = rand_words_list(n, 10, 10)

    # istanzio un albero AVL ed un albero RB
    avl_tree = AVLTreeMap()
    rb_tree = RedBlackTreeMap()

    # misuro quanto tempo è necessario per l'inserimento di n valori ordinati
    # AVL Tree
    start_time = time.time()
    for i in range(1, n):
        avl_tree[i] = rwl[i]
    avl_time = time.time() - start_time

    # RB Tree
    start_time = time.time()
    for i in range(1, n):
        rb_tree[i] = rwl[i]
    rb_time = time.time() - start_time

    print("Il tempo impiegato per {0} inserimenti in un AVL Tree è {1}".format(n, avl_time))
    print("Il tempo impiegato per {0} inserimenti in un RB Tree è {1}".format(n, rb_time))
    print("Il rapporto tra i due tempi è:", round(rb_time/avl_time, 2))


test_trees_insertion(1000)
test_trees_insertion(10000)
test_trees_insertion(100000)
test_trees_insertion(1000000)



