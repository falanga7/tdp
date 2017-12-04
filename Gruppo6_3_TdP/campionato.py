from Gruppo6_3_TdP.TdP_collections.hash_table.chain_hash_map import ChainHashMap


class Campionato:
    __slots__ = '_codice','_nome','_squadre','_partite'

    def __init__(self, codice, nome, squadre, partite = None):

        if not isinstance(codice, str):
            raise ValueError("Il codice passato non è una stringa.")
        elif not isinstance(nome, str):
            raise ValueError("Il nome passato non è una stringa.")
        elif not isinstance(squadre, ChainHashMap):
            raise ValueError("Le squadre devono essere strutturate secondo una ChainHashMap.")
        self._codice = codice
        self._nome = nome
        self._squadre = squadre
        self._partite = partite

    def codice(self):
        return self._codice

    def nome(self):
        return self._nome

    def squadre(self):
        return self._squadre

    def partite(self):
        return self._partite

    def set_partite(self,partite):
        if not isinstance(partite, ChainHashMap):
            raise ValueError("Le partite devono essere strutturate secondo una ChainHashMap.")
        self._partite = partite
