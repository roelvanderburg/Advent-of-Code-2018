import numpy as np
from tqdm import tqdm

test_coordinates = np.loadtxt('./input', dtype= tuple,delimiter=',')

test_coordinates = [[int(x), int(y)] for x,y in test_coordinates]

# test_coordinates = [[1, 1],
#                     [1, 6],
#                     [8, 3],
#                     [3, 4],
#                     [5, 5],
#                     [8, 9]]

maximum_x = np.max(test_coordinates, axis=0)
max = np.max(maximum_x)
array = np.zeros(shape=(max+1, max+1))

for index, coordinate in enumerate(test_coordinates):
    array[coordinate[1], coordinate[0]] = index + 1

max_coordinate = np.max(array)


def manhattan_distance(p, q):

    if len(p) != len(q):
        print("Be sure that both vectors are the same dimension!")
        return

    return sum([abs(p[i]-q[i]) for i in range(len(p))])


# For every coordinate calculate:
def construct_distance_matrix(array):

    new_array = np.zeros(shape=(max+1, max+1))

    print(array)
    print(" - - - -- ")
    for x in tqdm(range(0, len(array))):
        for y in range(0, len(array)):
            shortest = []

            for index, i in enumerate(test_coordinates):
                shortest.append(manhattan_distance(p=[x, y], q=i))

            min = np.min(shortest)
            index_min = shortest.index(np.min(shortest))

            shortest = np.array(shortest)

            if len(shortest[shortest == min]) > 1:
                new_array[y, x] = 0
            else:
                new_array[y, x] = index_min + 1

    return new_array


bin_counts = np.bincount(construct_distance_matrix(array).flatten().astype(dtype='int64'))

new_array_2 = construct_distance_matrix(array)


def check_element_edge(array, i):
    """
    Check if element i is in the outskirts of the array
    :param array:
    :param i:
    :return:
    """
    lengths = len(array)
    if np.any(new_array_2[0, :] == i):
        return False
    if np.any(new_array_2[:,0] == i):
        return False
    if np.any(new_array_2[lengths - 1, :] == i):
        return False
    if np.any(new_array_2[:, lengths -1] == i):
        return False
    else:
        return True


dem_bools = [[bin_counts[i], check_element_edge(array, i)] for i in range(1,len(test_coordinates)+1)]

dem_bools = sorted(dem_bools, key = lambda x: x[0], reverse=True)
dem_bools = sorted(dem_bools, key = lambda x: x[1], reverse=True)
print(dem_bools)

def construct_distance_matrix(array, distance):

    new_array = np.zeros(shape=(max+1, max+1))

    print(array)
    print(" - - - -- ")
    for x in tqdm(range(0, len(array))):
        for y in range(0, len(array)):
            shortest = []

            for index, i in enumerate(test_coordinates):
                shortest.append(manhattan_distance(p=[x, y], q=i))

            total_length = sum(shortest)

            if total_length < distance:
                new_array[y, x] = 1


    return new_array

dat_array  = construct_distance_matrix(array, distance =10000)
region = np.count_nonzero(dat_array)
print(region)