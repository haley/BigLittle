import re
import higher_preference
import lower_preference

def main():
    path = '/users/HaleyFletcher/Documents/Professional/BigLittle/BigLittle/test_simple.txt'
    test_file = open(path, 'r')

    info = test_file.read()

    preference = re.findall(r'(?<=B\n).*', info, re.M)
    less_preference = re.findall(r'(?<=L\n).*', info, re.M)

    preferred_group = []
    less_preferred_group = []

    for person in preference:
        new_person = higher_preference.higher_preference(person)
        preferred_group.append(new_person)

    for person in less_preference:
        new_person = lower_preference.lower_preference(person)
        less_preferred_group.append(new_person)

    


main()
