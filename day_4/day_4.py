from datetime import datetime
import re

file_object = open("./guards", mode='r')
files = [file for file in file_object.read().split('\n')]
# Sort on date in position 1 to 17
sorted_list = sorted(files, key=lambda x: x[1:17])

print(sorted_list[:10])

FMT = '%H:%M'
guard_dictionary = {}
for idx, shift in enumerate(sorted_list):
    if re.search(r'begins', shift):
        guard_nb = re.findall(r'[0-9]+', shift[18:])
        t1 = shift[10:17]
        for i in range(1,10):
            if re.search(r'falls', shift[idx+i]):
                



tdelta = datetime.strptime(t2, FMT) - datetime.strptime(t1  , FMT)
print(tdelta)







