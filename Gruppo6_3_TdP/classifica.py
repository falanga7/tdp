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

        def vittorie(qualcosa):
            return qualcosa.vittorie()

        def vittorie_in_casa(qualcosa):
            return qualcosa.vittorie_casa()

        def vittorie_in_trasferta(qualcosa):
            return qualcosa.vittorie_trasferta()

        def goal_fatti(qualcosa):
            return qualcosa.goalfatti()

        def goal_subiti(qualcosa):
            return qualcosa.goalsubiti()

        def differenza_reti(qualcosa):
            return qualcosa.goalfatti() - qualcosa.goalsubiti()

        if param == 0:
            self._lista.sort(key=punti, reverse=reverse)
        elif param == 1:
            self._lista.sort(key=vittorie, reverse=reverse)
        elif param == 2:
            self._lista.sort(key=vittorie_in_casa, reverse=reverse)
        elif param == 3:
            self._lista.sort(key=vittorie_in_trasferta, reverse=reverse)
        elif param == 4:
            self._lista.sort(key=goal_fatti, reverse=reverse)
        elif param == 5:
            self._lista.sort(key=goal_subiti, reverse=reverse)
        elif param == 6:
            self._lista.sort(key=differenza_reti, reverse=reverse)

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
