from Fitness import Fitness
import random
import bisect
import datetime


class Genetic:
    def __init__(self, bigs, littles, fitness):
        self.bigs = bigs
        self.littles = littles
        self.fitness = fitness

    def generate_sample(self, populationsize):
        sample = []
        for i in range(populationsize):
            entry = self.shuffle(self.littles)
            sample.append((self.fitness.fitness_list(entry, self.bigs), entry))
        return sample

    def shuffle(self, unshuffled):
        shuffled = unshuffled.copy()
        random.shuffle(shuffled)
        return shuffled

    def crossover(self, parent1, parent2):
        baby1 = [None] * len(parent1)
        baby2 = baby1.copy()
        baby1has = set()
        baby2has = set()
        start = random.randrange(0, len(parent1))
        if start == len(parent1) - 1:
            end = len(parent1)
        else:
            end = random.randrange(start + 1, len(parent1))
        for i in range(start, min(end + 1, len(parent1))):
            baby1[i] = parent1[i]
            baby1has.add(parent1[i])
            baby2[i] = parent2[i]
            baby2has.add(parent2[i])
        p1 = 0
        p2 = 0
        for elem1, elem2 in zip(parent1, parent2):
            if p1 < len(baby1) and baby1[p1] is not None:
                p1 += end - start + 1
            if p2 < len(baby2) and baby2[p2] is not None:
                p2 += end - start + 1
            if p2 < len(baby1) and elem1 not in baby2has:
                baby2[p2] = elem1
                p2 += 1
            if p1 < len(baby1) and elem2 not in baby1has:
                baby1[p1] = elem2
                p1 += 1
        return baby1, baby2

    def breed(self, sample):
        i = 0
        bred = []
        while i < len(sample) - 1:
            babies = self.crossover(sample[i], sample[i + 1])
            bred.append((self.fitness.fitness_list(babies[0], self.bigs), babies[0]))
            bred.append((self.fitness.fitness_list(babies[1], self.bigs), babies[1]))
            i += 2
        return bred

    def duplicate(self, sample):
        upsize = sample.copy()
        for i in range(10):
            upsize.extend(sample)
        return self.shuffle(upsize)

    def cull(self, sample):
        top = []
        min = sample[0]
        for elem in sample:
            if elem[0] < min[0]:
                min = elem
            if len(top) < 10:
                bisect.insort(top, elem[0])
            elif elem[0] < top[9]:
                top.pop(9)
                bisect.insort(top, elem[0])
        culled = []
        for elem in sample:
            if elem[0] in top and len(culled) < 10:
                culled.append(elem[1])
        return culled, min

    def best(self, end):
        population = self.generate_sample(100)
        while datetime.datetime.now() < end:
            population, min = self.cull(population)
            # print(min)
            population = self.duplicate(population)
            population = self.breed(population)
            # print(population)
        for little, big in zip(min[1], self.bigs):
            print(little, big)
        for match in self.fitness.get_automatches():
            print(match[0], match[1])
        print(min[0])
