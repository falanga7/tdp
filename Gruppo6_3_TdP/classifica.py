from Gruppo6_3_TdP.record_classifica import RecordClassifica

class Classifica:
    __slots__ = '_lista'

    def __init__(self,lista):
        self._lista = []
        if isinstance(lista[0],str):
            for squadra in lista:
                self._lista.append(RecordClassifica(squadra))
        elif isinstance(lista[0],RecordClassifica):
            for record in lista:
                self._lista.append(record)

    def lista(self):
        return self._lista

    def ordina(self, param, reverse=False):
        def punti(qualcosa):
            return qualcosa.punti()
        if param == 0:

            self._lista.sort(key=punti,reverse=reverse)

    def aggiungi_record(self, record):

        for r in self._lista:
            if r.squadra() == record.squadra():
                self._lista.remove(r)
                self._lista.append(record)
                break


    def __str__(self):

        for record in self._lista:
            print(record.squadra(),record.partite())

        return  ""
