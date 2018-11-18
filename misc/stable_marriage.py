import re
import participant


def main():

    path = '/users/HaleyFletcher/Documents/Professional/BigLittle/test_simple.txt'
    test_file = open(path, 'r')

    info = test_file.read()

    priority = re.findall(r'(?<=B\n).*', info, re.M)
    all = re.findall(r'(?<=[BL]\n).*', info, re.M)

    preferred_group = []
    less_preferred_group = []

    for person in all:
        new_person = participant.participant(person)
        if person in priority:
            new_person.priority = True
            preferred_group.append(new_person)
        else:
            new_person.priority = False
            less_preferred_group.append(new_person)
        regex = r'(?<=[BL]\n' + new_person.name + r'\n)([^BL]*\n)*(?=end)'
        preferences = re.findall(regex, info, re.M)
        for match in preferences:
            new_person.preferences = match.splitlines()

        # print(preferences)
        # new_person.preferences = preferences.splitlines()

    all_matched = False
    while not all_matched:
        for person in preferred_group:
            

main()
