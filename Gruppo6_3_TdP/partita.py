import datetime


class Partita:
    __slots__ = '_date', '_hometeam', '_awayteam', '_fthg', '_ftag', '_ftr', '_hthg', '_htag', '_htr'

    def __init__(self, date, hometeam, awayteam, fthg, ftag, ftr, hthg=None, htag=None, htr=None):
        try:
            datetime.datetime.strptime(date, '%d/%m/%Y')
        except ValueError:
            raise ValueError("La data non è in un formato valido, dovrebbe essere DD/MM/YYYYY")
        if not isinstance(fthg, int):
            raise ValueError("I goal della squadra locale alla fine della partita non sono in un formato valido.")
        elif not isinstance(ftag, int):
            raise ValueError("I goal della squadra ospite alla fine della partita non sono in un formato valido.")
        elif not isinstance(hthg, int):
            raise ValueError("I goal della squadra locale a metà partita non sono in un formato valido.")
        elif not isinstance(htag, int):
            raise ValueError("I goal della squadra ospite a metà della partita non sono in un formato valido.")
        """if not ftr == "H" or not ftr == "D" or not ftr == "A":
            raise ValueError("Il risultato finale non è in un formato valido.")
        elif not htr == "H" or not htr == "D" or not htr == "A":
            raise ValueError("Il risultato del primo tempo non è in un formato valido.")"""
        self._date = date
        self._hometeam = hometeam
        self._awayteam = awayteam
        self._fthg = fthg
        self._ftag = ftag
        self._ftr = ftr
        self._hthg = hthg
        self._htag = htag
        self._htr = htr

    def date(self):
        return self._date

    def hometeam(self):
        return self._hometeam

    def awayteam(self):
        return self._awayteam

    def fthg(self):
        return self._fthg

    def ftag(self):
        return self._ftag

    def ftr(self):
        return self._ftr

    def hthg(self):
        return self._hthg

    def htag(self):
        return self._htag

    def htr(self):
        return self._htr
