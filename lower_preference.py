class lower_preference:
    """Methods for the group that is not preferenced or the proposees in the
    Stable marriage problem"""
    def __init__(self, name):
        self.name = name
        self.engaged = False

    def __str__(self):
        return self.name
