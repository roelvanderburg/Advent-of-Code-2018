import numpy as np
from tqdm import tqdm
from itertools import *

print(list(map(pow, range(10), repeat(2))))
frequencies = np.loadtxt('./data/frequencies.txt')

print("Min: ", np.min(frequencies))
print("Max: ", np.max(frequencies), '\n')


freq = 0
# {} dictionary, creates set
seen = {0}
for frequencies in tqdm(cycle(frequencies)):
    freq += frequencies
    if freq in seen:
        print(seen)
        print(freq)
        break
    seen.add(freq)
