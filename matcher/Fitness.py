class Fitness:
    """
    Matrix for Fitness
    self._matrix[little][big]
    """
    def __init__(self, people):
        self.littles = []
        self.bigs = []
        for person in people.values():
            if person.status == 'l':
                self.littles.append(person)
            elif person.status == 'b':
                self.bigs.append(person)
        bignum = len(self.bigs)
        littlenum = len(self.littles)

        self.automatches = []

        for little in self.littles:
            if little.preferences[1].preferences[1] == little:
                big = little.preferences[1]
                self.automatches.append((little, big))
                self.littles.remove(little)
                self.bigs.remove(big)

        self._matrix = [[[0] for i in range(len(self.littles))] for j in range(len(self.bigs))]
        for l, little in enumerate(self.littles):
            for b, big in enumerate(self.bigs):
                fitness = little.rank_of(big, bignum)
                fitness += big.rank_of(little, littlenum)
                self._matrix[l][b] = fitness

    def get_bigs(self):
        return self.bigs

    def get_littles(self):
        return self.littles

    def get_automatches(self):
        return self.automatches

    def fitness_of(self, little, big):
        return self._matrix[self.littles.index(little)][self.bigs.index(big)]

    def fitness_list(self, littles, bigs):
        fitness = 0
        for little, big in zip(littles, bigs):
            fitness += self.fitness_of(little, big)
        return fitness
