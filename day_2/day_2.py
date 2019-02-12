import numpy as np
from tqdm import tqdm
import pandas as pd
import collections
from typing import List
import string

lines = np.loadtxt('./checksum_2018_day_2', dtype=str, delimiter='\n')


def check_letters(line: str):
    add = [0,0]
    for letter in string.ascii_letters:
        counter =0
        for character in line:
            if character == letter:
                counter += 1
        if counter == 3:
            add[1] = 1
        if counter == 2:
            add[0] = 1

    return add

def check_identical(test_match: str, all_ids: List):
    """
    :param test_match: input string to match against all oter ids
    :param all_ids: list of all ids
    :return:
    """
    for idx, line in enumerate(all_ids):
        counter = 0
        for idy, (char_1, char_2) in enumerate(zip(line, test_match)):
            if char_1 != char_2:
                counter += 1
            if counter >= 2:
                break
            if counter == 1 and idy == len(test_match)-1:
                print('Match found at idx :', idx, "The line is {}, and test_string {}".format(line, test_match))
                return



for line in lines:
    check_identical(line, lines)


tzyvunogzariwkpcbdewsmjhxi
tzyvunogzariwkpcbdewmjhxi








full_counts = []
for line in lines:
    full_counts.append(check_letters(line))

one = sum([first[0] for first in full_counts])
two = sum([first[1] for first in full_counts])
print(one*two)




