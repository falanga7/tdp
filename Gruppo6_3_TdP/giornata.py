class Giornata:
    __slots__ = '_date_partite','_classifica'

    def __init__(self,classifica,date_partite = None):
        self._classifica = classifica
        self._date_partite = date_partite

    def classifica(self):
        return self._classifica

    def set_date_partite(self,date_partite):
        self._date_partite = date_partite

    def date_partite(self):
        return self._date_partite

    def aggiungi_data(self,data):
        self._date_partite.append(data)

