from ImportFormCSV import importCSV
from Fitness import Fitness
from Genetic import Genetic
import datetime
# import time

people = importCSV()


fitness = Fitness(people)
bigs, littles = fitness.bigs, fitness.littles


now = datetime.datetime.now()
delta = datetime.timedelta(seconds=2)
# print(now)
# while datetime.datetime.now() < now + delta:
genetic = Genetic(bigs, littles, fitness)
genetic.best(now + delta)
# sample = genetic.generate_sample(50)
# print(sample)
# cull, min = genetic.cull(sample)
# print('CULL')
# print(cull)
# print('BREED')
# print(genetic.breed(cull))
# print(cull)
# crossed = genetic.crossover(a, b)
# for cross in crossed:
#     print(cross)
#
# print(genetic.duplicate(b))
