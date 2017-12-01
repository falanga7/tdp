class Partita:
    __slots__ = '_codice', '_squadre'

    def __init__(self, hometeam, awayteam, fthg, ftag, ftr, hthg, htag, htr):
        self._hometeam = hometeam
        self._awayteam = awayteam
        self._fthg = fthg

    def codice(self):
        return self._codice

    def squadre(self):
        return self._squadre