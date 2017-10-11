class DoubleLinkedList:
    """ Classe astratta che implementa l'ADT List."""

    def append(self, x):
        """Aggiunge un elemento alla fine della lista."""
        raise NotImplementedError('deve essere implementato dalla sottoclasse.')

    def extend(self, iterable):
        """Estende la lista aggiungendo tutti gli elementi da un iterable"""
        raise NotImplementedError('deve essere implementato dalla sottoclasse.')

    def insert(self, i, x):
        """Inserisce un elemento a una data posizione."""
        raise NotImplementedError('deve essere implementato dalla sottoclasse.')

    def remove(self, x):
        """Rimuove il primo elemento dalla lista il cui valore è x."""
        raise NotImplementedError('deve essere implementato dalla sottoclasse.')

    def pop(self, i=-1):
        """Rimuove un elemento dalla posizione specificata nella lista e lo ritorna."""
        raise NotImplementedError('deve essere implementato dalla sottoclasse.')

    def clear(self):
        """"Rimuove tutti gli elementi dalla lista."""
        raise NotImplementedError('deve essere implementato dalla sottoclasse.')

    def index(self, x, start=None, end=None):
        """Ritorna un indice nella lista dell'elemento x."""
        raise NotImplementedError('deve essere implementato dalla sottoclasse.')

    def count(self, x):
        """Ritorna il numero di volte che l'elemento x appare nella lista."""
        raise NotImplementedError('deve essere implementato dalla sottoclasse.')

    def sort(self, key=None, reverse=False):
        """Ordina gli elementi della lista."""
        raise NotImplementedError('deve essere implementato dalla sottoclasse.')

    def reverse(self):
        """Inverte la posizione degli elementi della lista."""
        raise NotImplementedError('deve essere implementato dalla sottoclasse.')

    def copy(self):
        """Ritorna una shallow copy della lista."""
        raise NotImplementedError('deve essere implementato dalla sottoclasse.')

