class participant:
    """Methods for the participants"""
    def __init__(self, name, priority=False):
        self.name = name
        self.engaged = False
        # self.suitors = []
        self._priority = priority

    def __str__(self):
        return self.name

    @property
    def priority(self):
        return self._priority

    @priority.setter
    def priority(self, status):
        self._priority = status

    @property
    def preferences(self):
        return self.suitors

    @preferences.setter
    def preferences(self, suitors):
        self.suitors = suitors

    @property
    def mate(self):
        return self._mate

    @mate.setter
    def mate(self, participant):
        self._mate = participant
