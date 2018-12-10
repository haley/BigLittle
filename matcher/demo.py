from ImportFormCSV import importCSV
from Fitness import Fitness
from Genetic import Genetic
import datetime
people = importCSV()
fitness = Fitness(people)
bigs, littles = fitness.bigs, fitness.littles
genetic = Genetic(bigs, littles, fitness)

# IMPORT CSV
# print('PEOPLE', people)
#
# # CREATE FITNESS
# print('BIGS:', bigs)
# print('LITTLES: ', littles)
# print('AUTO MATCHED', fitness.get_automatches())
#
#
# # GENERATE A SAMPLE
# print(genetic.generate_sample(5))
#
#
# CROSSOVER
# a = ['a', 'b', 'f', 'e', 'd', 'c']
# b = ['c', 'b', 'e', 'a', 'd', 'f']
# print('BEFORE')
# print(a)
# print(b)
# print('AFTER')
# crossed = genetic.crossover(a, b)
# for cross in crossed:
#     print(cross)
