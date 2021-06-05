#!/usr/bin/python
import sys
import numpy as np
from statistics import mean


def remove_outliers(original):
    original.sort()
    return original[1:-1]

def get_speedup(first, avg):
    return first/avg;


test_num = 4  # const
workers = [1, 2, 4, 8, 16, 32]
runs = 5

if len(sys.argv) != 3:
    print("Usage: python3 processResults.py <remove_outliers> <file_name>")

input_file = open(sys.argv[2], "r")

results = np.zeros((test_num, len(workers)))

speedups = np.zeros((test_num, len(workers)))

for t in range(test_num):
    for w in range(len(workers)):
        times = []
        for r in range(5):
            times.append(float((input_file.readline().split(" ")[1]).split("\n")[0]))
            input_file.readline()
            input_file.readline()
        times = remove_outliers(times)
        avg = mean(times)
        results[t, w] = avg
        if w != 0:
            speedups[t, w] = get_speedup(results[t, 0], avg)


#np.savetxt("cluster_results.csv", results, delimiter=",")

np.savetxt("speedups.csv", speedups, delimiter=",")

input_file.close()
