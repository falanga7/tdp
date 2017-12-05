class Giornata:
    __slots__ = '_date_partite','_classifica','_classifica_ht'

    def __init__(self,classifica,classifica_ht = None):
        self._classifica = classifica
        self._classifica_ht = classifica_ht


    def classifica(self):
        return self._classifica

    def classifica_ht(self):
        return self._classifica_ht