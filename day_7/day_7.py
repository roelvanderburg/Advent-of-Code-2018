import numpy as np
import string
import re

np.set_printoptions(edgeitems=10, linewidth=300)

test_input = [  'Step C must be finished before step A can begin.',
                'Step C must be finished before step F can begin.',
                'Step A must be finished before step B can begin.',
                'Step A must be finished before step D can begin.',
                'Step B must be finished before step E can begin.',
                'Step D must be finished before step E can begin.',
                'Step F must be finished before step E can begin.']


# test_input = np.loadtxt('./input', dtype= tuple,delimiter=',')
# print(test_input)

input_cleaned = []
for input in test_input:
    dat = re.findall(pattern=r'[A-Z]', string=input[1:])
    input_cleaned.append(re.findall(pattern=r'[A-Z]', string=input[1:]))
    print(input_cleaned)


print("- - - - -- ")
input_cleaned = sorted(input_cleaned, key=lambda x: x[1])


alpha_time_dictionary = {alpha: i+1 for i, alpha in enumerate(string.ascii_uppercase)}

final_list = []
first_elements = []
while True:
    ones = [element[0] for element in input_cleaned]
    twos = [element[1] for element in input_cleaned]

    # Next option element only present in the left side.
    option_elements = list(set(ones) - set(twos))

    options = [option for option in input_cleaned if option[0] in option_elements]
    chosen = sorted(options, key=lambda x: x[0])

    firstz = list(set([x[0] for x in chosen]))
    firstz = sorted(firstz, key=lambda x: x[0])


    if firstz != []:
        first_elements.append(firstz)

    print("Options Sorted: ", chosen)
    try:

        element = chosen[0][0]
        final_list.append(element)
        input_cleaned = [x for x in input_cleaned if x[0] != element]

    except:
        print(final_list)
        # print(''.join(final_list))
        break

times = [alpha_time_dictionary[char] for char in final_list]

print(first_elements)

time_matrix = np.zeros(shape=(2, 40))
print(time_matrix)
workers = 2

print(id(workers))


class Worker:

    def __init__(self, id: int):
        self.occupied = False
        self.id = id

    def check(self):
        return self.occupied

    def make_busy(self):
        self.occupied = True

    def make_free(self):
        self.occupied = False


for time_i in range(0, 40):
    for option_list in first_elements:

        option = option_list[0]

# print(time_matrix)

