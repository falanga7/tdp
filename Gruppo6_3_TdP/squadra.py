from Gruppo6_3_TdP.record_classifica import RecordClassifica

class Squadra:
    __slots__ = '_nome', '_record_classifica'

    def __init__(self, nome):

        if not isinstance(nome, str):
            raise ValueError("Il nome passato non è una stringa.")
        self._nome = nome
        """Oggetto utilizzato per la definizione delle giornate e l'aggiornamento della Classifica"""
        self._record_classifica = RecordClassifica(nome, 0, 0, 0, 0, 0, 0, 0, 0)

    def squadra(self):
        return self._nome


    def update_record(self, record):
        self._record_classifica + record


    def record(self):
        return self._record_classifica


    def __str__(self):
        return self._nome

