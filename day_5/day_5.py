import sys
import string

iMaxStackSize = 5000
sys.setrecursionlimit(iMaxStackSize)

fd = open('genome.txt','rU', encoding='latin-1')
chars = []
for line in fd:
    for c in line:
        chars.append(c)


def solve_genome(genome_list: list):
    """
    Finds adjecent capital and lower case letters, deletes them from the array and starts over till no more letters
    :return:
    """

    i = 0
    while i < (len(genome_list)-1):

        if genome_list[i].islower() and not genome_list[i + 1].islower() and i >= 0:
            if genome_list[i] == genome_list[i + 1].lower():
                del genome_list[i: i + 2]
                if i != 0:
                    i -= 2

        if not genome_list[i].islower() and  genome_list[i + 1].islower() and i >= 0:
            if genome_list[i].lower() == genome_list[i + 1]:
                del genome_list[i: i + 2]
                if i != 0:
                    i -= 2

        i += 1

    # # Waarom is dit nodig ???
    # i = 0
    # if genome_list[i].islower() and not genome_list[i + 1].islower() and i >= 0:
    #     if genome_list[i] == genome_list[i + 1].lower():
    #         del genome_list[i: i + 2]
    #         # if i != 0:
    #         #     i -= 2
    #
    # if not genome_list[i].islower() and genome_list[i + 1].islower() and i >= 0:
    #     if genome_list[i].lower() == genome_list[i + 1]:
    #         del genome_list[i: i + 2]


    return len(genome_list)


the_dictionary = {}
tha_list = []
for lowercase in string.ascii_lowercase:
    uppercase = lowercase.upper()
    new_dict = [char for char in chars if char != lowercase and char != uppercase]
    the_dictionary.update({lowercase: solve_genome(new_dict)})
    tha_list.append(solve_genome(new_dict))

# TODO -2 on results
the_dictionary = sorted(the_dictionary.items(), key=lambda x: x[1])
print(the_dictionary)


