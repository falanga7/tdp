class Giornata:
    __slots__ = '_data_inizio','_data_fine','_partite'

    def __init__(self,data_inizio,data_fine,partite):
        self._data_inizio = data_inizio
        self._data_fine = data_fine
        self._partite = partite

