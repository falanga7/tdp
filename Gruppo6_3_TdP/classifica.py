from Gruppo6_3_TdP.record_classifica import RecordClassifica

class Classifica:
    __slots__ = '_lista'

    def __init__(self):
        self._lista = []

    def lista(self):
        return self._lista

    def ordina(self, param, reverse=False):
        def punti(qualcosa):
            return qualcosa.punti()
        if param == 0:

            self._lista.sort(key=punti,reverse=reverse)

    def aggiungi_record(self, record):
        self._lista.append(record)

