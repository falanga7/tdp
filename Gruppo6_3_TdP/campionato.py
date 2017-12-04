from Gruppo6_3_TdP.TdP_collections.hash_table.chain_hash_map import ChainHashMap


class Campionato:
    __slots__ = '_codice','_nome','_squadre'

    def __init__(self, codice, nome, squadre):

        if not isinstance(codice, str):
            raise ValueError("Il codice passato non è una stringa.")
        elif not isinstance(nome, str):
            raise ValueError("Il nome passato non è una stringa.")
        elif not isinstance(squadre, ChainHashMap):
            raise ValueError("Le squadre devono essere strutturate secondo una ChainHashMap.")
        self._codice = codice
        self._nome = nome
        self._squadre = squadre

    def codice(self):
        return self._codice

    def nome(self):
        return self._nome

    def squadre(self):
        return self._squadre

