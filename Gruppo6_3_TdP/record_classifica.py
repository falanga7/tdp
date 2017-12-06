class RecordClassifica:

    __slots__ = '_squadra','_partite','_vittorie','_pareggi','_sconfitte','_goalfatti','_goalsubiti','_punti',\
                '_vittorie_ht', '_pareggi_ht', '_sconfitte_ht', '_goalfatti_ht', '_goalsubiti_ht', '_punti_ht',\
                '_partite_casa', '_vittorie_casa', '_pareggi_casa', '_sconfitte_casa', '_goalfatti_casa', '_goalsubiti_casa', '_punti_casa',\
                '_partite_trasferta', '_vittorie_trasferta', '_pareggi_trasferta', '_sconfitte_trasferta', '_goalfatti_trasferta', '_goalsubiti_trasferta', '_punti_trasferta'

    def __init__(self, squadra, partite = 0, vittorie = 0, pareggi = 0, sconfitte = 0, goalfatti = 0, goalsubiti = 0, punti = 0,
                 vittorie_ht=0, pareggi_ht=0, sconfitte_ht=0, goalfatti_ht=0, goalsubiti_ht=0, punti_ht=0,
                 partite_casa=0, vittorie_casa=0, pareggi_casa=0, sconfitte_casa=0, goalfatti_casa=0, goalsubiti_casa=0, punti_casa=0,
                 partite_trasferta=0, vittorie_trasferta=0, pareggi_trasferta=0, sconfitte_trasferta=0, goalfatti_trasferta=0, goalsubiti_trasferta=0, punti_trasferta=0):
        self._squadra = squadra
        self._partite = partite
        self._vittorie = vittorie
        self._pareggi = pareggi
        self._sconfitte = sconfitte
        self._goalfatti = goalfatti
        self._goalsubiti = goalsubiti
        self._punti = punti
        self._vittorie_ht = vittorie_ht
        self._pareggi_ht = pareggi_ht
        self._sconfitte_ht = sconfitte_ht
        self._goalfatti_ht = goalfatti_ht
        self._goalsubiti_ht = goalsubiti_ht
        self._punti_ht = punti_ht
        self._partite_casa = partite_casa
        self._vittorie_casa = vittorie_casa
        self._pareggi_casa = pareggi_casa
        self._sconfitte_casa = sconfitte_casa
        self._goalfatti_casa = goalfatti_casa
        self._goalsubiti_casa = goalsubiti_casa
        self._punti_casa = punti_casa
        self._partite_trasferta = partite_trasferta
        self._vittorie_trasferta = vittorie_trasferta
        self._pareggi_trasferta = pareggi_trasferta
        self._sconfitte_trasferta = sconfitte_trasferta
        self._goalfatti_trasferta = goalfatti_trasferta
        self._goalsubiti_trasferta = goalsubiti_trasferta
        self._punti_trasferta = punti_trasferta


    def __iadd__(self, other):
        if not isinstance(other,RecordClassifica):
            raise ValueError("La somma può essere effettuata solo su oggetti di tipo RecordClassifica")
        self._partite += other._partite
        self._vittorie += other._vittorie
        self._pareggi += other._pareggi
        self._sconfitte += other._sconfitte
        self._goalfatti += other._goalfatti
        self._goalsubiti += other._goalsubiti
        self._punti += other._punti
        self._vittorie_ht += other._vittorie_ht
        self._pareggi_ht += other._pareggi_ht
        self._sconfitte_ht += other._sconfitte_ht
        self._goalfatti_ht += other._goalfatti_ht
        self._goalsubiti_ht += other._goalsubiti_ht
        self._punti_ht += other._punti_ht
        self._partite_casa += other._partite_casa
        self._vittorie_casa += other._vittorie_casa
        self._pareggi_casa += other._pareggi_casa
        self._sconfitte_casa += other._sconfitte_casa
        self._goalfatti_casa += other._goalfatti_casa
        self._goalsubiti_casa += other._goalsubiti_casa
        self._punti_casa += other._punti_casa
        self._partite_trasferta += other._partite_trasferta
        self._vittorie_trasferta += other._vittorie_trasferta
        self._pareggi_trasferta += other._pareggi_trasferta
        self._sconfitte_trasferta += other._sconfitte_trasferta
        self._goalfatti_trasferta += other._goalfatti_trasferta
        self._goalsubiti_trasferta += other._goalsubiti_trasferta
        self._punti_trasferta += other._punti_trasferta
        return self

    def copy(self):
        return RecordClassifica(self._squadra,self._partite,self._vittorie,self._pareggi,self._sconfitte,self._goalfatti,self._goalsubiti,self._punti,
                                self._vittorie_ht, self._pareggi_ht, self._sconfitte_ht, self._goalfatti_ht,
                                self._goalsubiti_ht, self._punti_ht,self._partite_casa,self._vittorie_casa,self._pareggi_casa,self._sconfitte_casa,self._goalfatti_casa,
                                self._goalsubiti_casa,self._punti_casa,self._partite_trasferta, self._vittorie_trasferta, self._pareggi_trasferta, self._sconfitte_trasferta,
                                    self._goalfatti_trasferta,self._goalsubiti_trasferta, self._punti_trasferta)

    def squadra(self):
        return self._squadra

    def partite(self):
        return self._partite

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

    def punti(self):
        return self._punti

    def set_squadra(self, squadra):
        self._squadra = squadra

    def set_partite(self, partite):
        self._partite = partite

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

    def set_punti(self, punti):
        self._punti = punti

    def vittorie_ht(self):
        return self._vittorie_ht

    def pareggi_ht(self):
        return self._pareggi_ht

    def sconfitte_ht(self):
        return self._sconfitte_ht

    def goalfatti_ht(self):
        return self._goalfatti_ht

    def goalsubiti_ht(self):
        return self._goalsubiti_ht

    def punti_ht(self):
        return self._punti_ht

    def set_vittorie_ht(self, vittorie_ht):
        self._vittorie_ht = vittorie_ht

    def set_pareggi_ht(self, pareggi_ht):
        self._pareggi_ht = pareggi_ht

    def set_sconfitte_ht(self, sconfitte_ht):
        self._sconfitte_ht = sconfitte_ht

    def set_goalfatti_ht(self, goalfatti_ht):
        self._goalfatti_ht = goalfatti_ht

    def set_goalsubiti_ht(self, goalsubiti_ht):
        self._goalsubiti_ht = goalsubiti_ht

    def set_punti_ht(self, punti_ht):
        self._punti = punti_ht

    def partite_casa(self):
        return self._partite_casa

    def vittorie_casa(self):
        return self._vittorie_casa

    def pareggi_casa(self):
        return self._pareggi_casa

    def sconfitte_casa(self):
        return self._sconfitte_casa

    def goalfatti_casa(self):
        return self._goalfatti_casa

    def goalsubiti_casa(self):
        return self._goalsubiti_casa

    def punti_casa(self):
        return self._punti_casa

    def set_partite_casa(self, partite_casa):
        self._partite_casa = partite_casa

    def set_vittorie_casa(self, vittorie_casa):
        self._vittorie_casa = vittorie_casa

    def set_pareggi_casa(self, pareggi_casa):
        self._pareggi_casa = pareggi_casa

    def set_sconfitte_casa(self, sconfitte_casa):
        self._sconfitte_casa = sconfitte_casa

    def set_goalfatti_casa(self, goalfatti_casa):
        self._goalfatti_casa = goalfatti_casa

    def set_goalsubiti_casa(self, goalsubiti_casa):
        self._goalsubiti_casa = goalsubiti_casa

    def set_punti_casa(self, punti_casa):
        self._punti = punti_casa

    def partite_trasferta(self):
        return self._partite_trasferta

    def vittorie_trasferta(self):
        return self._vittorie_trasferta

    def pareggi_trasferta(self):
        return self._pareggi_trasferta

    def sconfitte_trasferta(self):
        return self._sconfitte_trasferta

    def goalfatti_trasferta(self):
        return self._goalfatti_trasferta

    def goalsubiti_trasferta(self):
        return self._goalsubiti_trasferta

    def punti_trasferta(self):
        return self._punti_trasferta

    def set_partite_trasferta(self, partite_trasferta):
        self._partite_trasferta = partite_trasferta

    def set_vittorie_trasferta(self, vittorie_trasferta):
        self._vittorie_trasferta = vittorie_trasferta

    def set_pareggi_trasferta(self, pareggi_trasferta):
        self._pareggi_trasferta = pareggi_trasferta

    def set_sconfitte_trasferta(self, sconfitte_trasferta):
        self._sconfitte_trasferta = sconfitte_trasferta

    def set_goalfatti_trasferta(self, goalfatti_trasferta):
        self._goalfatti_trasferta = goalfatti_trasferta

    def set_goalsubiti_trasferta(self, goalsubiti_trasferta):
        self._goalsubiti_trasferta = goalsubiti_trasferta

    def set_punti_trasferta(self, punti_trasferta):
        self._punti_trasferta = punti_trasferta


