class Participant:
    """Methods for the participants"""

    def __init__(self, name):
        self.name = name
        self._preferences = []
        self._status = None

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    @property
    def preferences(self):
        return self._preferences

    def add_preference(self, preference, rank):
        if rank >= len(self._preferences):
            add = [0] * (rank - len(self._preferences) + 1)

            self._preferences.extend(add)
        self._preferences[rank] = preference

    def rank_of(self, person, most):
        if person in self._preferences:
            return self._preferences.index(person)
        else:
            return most
