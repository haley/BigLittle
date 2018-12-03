import csv
import os
from Participant import Participant


def importCSV():
    people = {}

    path = os.getcwd()[0:-7] + 'matchdata'
    os.chdir(path)
    bignames = []
    littlenames = []
    otherfields = 5
    with open('BigLittleQuestionnaire.csv') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        first = True
        for row in spamreader:
            if first:
                for elem in row[otherfields:]:
                    if "If you're a little" in elem:
                        bigname = elem[elem.index('[') + 1: elem.index(']')]
                        bignames.append(bigname)
                        if bigname not in people:
                            people[bigname] = Participant(bigname)
                            people[bigname].status = 'b'

                    else:
                        littlename = elem[elem.index('[') + 1: elem.index(']')]
                        littlenames.append(littlename)
                        if littlename not in people:
                            people[littlename] = Participant(littlename)
                            people[littlename].status = 'l'
                first = False

            else:
                name = None
                start = None
                end = None
                if row[1] == 'Big':
                    name = row[2]
                    start = otherfields
                    end = otherfields + len(littlenames)
                    arr = littlenames
                elif row[1] == 'Little':
                    name = row[3]
                    start = otherfields + len(littlenames)
                    end = start + len(bignames)
                    arr = bignames
                for i, elem in enumerate(row[start: end]):
                    if elem != '':
                        rank = int(elem[0])
                        people[name].add_preference(people[arr[i]], rank)
    return people
