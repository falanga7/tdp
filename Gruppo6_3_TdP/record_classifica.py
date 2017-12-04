class RecordClassifica:

    __slots__ = '_squadra','_partite','_vittorie','_pareggi','_sconfitte','_goalfatti','_goalsubiti','_differenzareti','_punti'


    def __init__(self,squadra,partite,vittorie,pareggi,sconfitte,goalfatti,goalsubiti,differenzareti,punti):
        self._squadra = squadra
        self._partite = partite
        self._vittorie = vittorie
        self._pareggi = pareggi
        self._sconfitte = sconfitte
        self._goalfatti = goalfatti
        self._goalsubiti = goalsubiti
        self._differenzareti = differenzareti
        self._punti = punti


    def squadra(self):
        return self._squadra

    def partite(self):
        return self.partite

    def vittorie(self):
        return self._vittorie

    def pareggi(self):
        return self._pareggi

    def sconfitte(self):
        return self._sconfitte

    def goalfatti(self):
        return self._goalfatti

    def goalsubiti(self):
        return self._goalsubiti

    def differenzareti(self):
        return self._differenzareti

    def punti(self):
        return self._punti

    def set_squadra(self, squadra):
        self._squadra = squadra

    def set_partite(self, partite):
        self.partite = partite

    def set_vittorie(self, vittorie):
        self._vittorie = vittorie

    def set_pareggi(self, pareggi):
        self._pareggi = pareggi

    def set_sconfitte(self, sconfitte):
        self._sconfitte = sconfitte

    def set_goalfatti(self, goalfatti):
        self._goalfatti = goalfatti

    def set_goalsubiti(self, goalsubiti):
        self._goalsubiti = goalsubiti

    def set_differenzareti(self, differenzareti):
        self._differenzareti = differenzareti

    def set_punti(self, punti):
        self._punti = punti


