from Gruppo6_3_TdP.TdP_collections.hash_table.chain_hash_map import ChainHashMap


class Campionato:
    __slots__ = '_codice', '_squadre'

    def __init__(self, codice, squadre):

        if not isinstance(codice, str):
            raise ValueError("Il codice passato non è una stringa.")
        elif not isinstance(squadre, ChainHashMap):
            raise ValueError("Le squadre devono essere strutturate secondo una ChainHashMap.")
        self._codice = codice
        self._squadre = squadre

    def codice(self):
        return self._codice

    def squadre(self):
        return self._squadre