class higher_preference:
    """Methods for the preferenced or the proposers in the stable marriage
    problem"""
    def __init__(self, name):
        self.name = name
        self.engaged = False

    def __str__(self):
        return self.name
