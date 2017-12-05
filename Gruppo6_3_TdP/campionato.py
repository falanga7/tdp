from Gruppo6_3_TdP.TdP_collections.hash_table.chain_hash_map import ChainHashMap


class Campionato:
    __slots__ = '_codice','_nome','_squadre','_partite','_giornate'

    def __init__(self, codice, nome, squadre, partite, giornate=None):

        if not isinstance(codice, str):
            raise ValueError("Il codice passato non è una stringa.")
        elif not isinstance(nome, str):
            raise ValueError("Il nome passato non è una stringa.")
        elif not isinstance(squadre, ChainHashMap):
            raise ValueError("Le squadre devono essere strutturate secondo una ChainHashMap.")
        elif not isinstance(giornate, list):
            raise ValueError("Le giornate devono essere strutturate secondo una Lista.")
        self._codice = codice
        self._nome = nome
        self._squadre = squadre
        self._partite = partite
        self._giornate = giornate

    def codice(self):
        return self._codice

    def nome(self):
        return self._nome

    def squadre(self):
        return self._squadre

    def partite(self):
        return self._partite

    def giornate(self):
        return self._giornate


    def set_partite(self,partite):
        if not isinstance(partite, ChainHashMap):
            raise ValueError("Le partite devono essere strutturate secondo una ChainHashMap.")
        self._partite = partite


    def set_giornate(self,giornate):
        if not isinstance(giornate, list):
            raise ValueError("Le partite devono essere strutturate secondo una ChainHashMap.")
        self._giornate = giornate

    def calcolo_giornate(self):

        for partite_giorno in self._partite.values():
            for partita in partite_giorno:
                print(partita.date(),partita.hometeam(),partita.awayteam())
