import numpy as np
import re
from typing import List
from tqdm import tqdm
import time


class FabricMeasurements:

    def __init__(self, size: int, claims: str):

        file_object = open("./" + claims, mode='r')
        files = [file for file in file_object]
        self.claims_list = [re.findall(r'[0-9]+', string) for string in files]
        self.claims_list = [claim[1:] for claim in self.claims_list]

        self.fabric = np.zeros(shape=(size, size))

    def check_overlap(self):
        """
        Checks overlap between claim and already found
        :param matrix:
        :param claim:
        :return:
        """
        double_claims = 0

        for x, y, width, height in tqdm(self.claims_list):
            for i in range(int(x), int(x) + int(width)):
                for j in range(int(y), int(y) + int(height)):
                    self.fabric[i, j] += 1

        for idx,(x, y, width, heigth) in tqdm(enumerate(self.claims_list)):
            if np.all(self.fabric[int(x):int(x)+int(width), int(y):int(y)+int(heigth)] == 1):
                print("Idx ", idx+1)

        print(self.fabric)
        print(np.count_nonzero(self.fabric > 1))

        #
        # print(self.fabric, '\n', "claims".format(double_claims))
        print(double_claims)

        return double_claims

if __name__ == '__main__':
    measurer = FabricMeasurements(size=1000, claims='claims.txt')
    measurer.check_overlap()


