#!/usr/bin/python
import sys
import numpy as np
from statistics import mean


def remove_outliers(original):
    original.sort()
    return original[1:-1]


test_num = 9  # const
workers = [1, 2, 4, 8, 16]
runs = 5

if len(sys.argv) != 3:
    print("Usage: python3 processResults.py <remove_outliers> <file_name>")

input_file = open(sys.argv[2], "r")

results = np.zeros((test_num, len(workers)))

for t in range(test_num):
    for w in range(len(workers)):
        times = []
        for r in range(5):
            input_file.readline()
            times.append(float((input_file.readline().split(" ")[1]).split("\n")[0]))
            input_file.readline()
        if sys.argv[1] == 1:
            times = remove_outliers(times)
        avg = mean(times)
        results[t, w] = avg

np.savetxt("local_results.csv", results, delimiter=",")

input_file.close()
