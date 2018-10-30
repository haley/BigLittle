class participant:
    """Methods for the participants"""
    def __init__(self, name, priority=False):
        self.name = name
        self.engaged = False
        self.mate_priority = -1
        # self.suitors = []
        self._priority = priority
        self.best_mate = 0

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
        self.next_best = suitors[self.best_mate]
        self.suitors = suitors

    @property
    def mate(self):
        return self._mate

    @mate.setter
    def mate(self, participant):
        self.engaged = True
        self._mate = participant

    def mate_priority(self, potential_mate):
        return self.preferences().index(potential_mate)

    def next_best(self):
        next = self.preferences[self.best_mate]
        self.best_mate += 1
        return next

    def proposed_to_by(self, new_mate):
        if not self.engaged:
            self.mate(new_mate)
        elif self.mate_priority(new_mate) >= 0 and self.mate_priority(new_mate) < self.mate_priority(self.mate()):
            self.mate()

    def propose_to_next(self, less_preferred_group):
