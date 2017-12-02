class Squadra:
    __slots__ = '_nome', '_partite'

    def __init__(self, nome):

        if not isinstance(nome, str):
            raise ValueError("Il nome passato non è una stringa.")
        self._nome = nome
        self._partite = 0

    def squadra(self):
        return self._nome

    def __add__(self, b):
        self._partite = self._partite + b
        return self._partite

    def __iadd__(self, b):
        self._partite = self._partite + b
        return self._partite

    def __radd__(self, b):
        self._partite = self._partite + b
        return self._partite

    def __str__(self):
        return self._nome

