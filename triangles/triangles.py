"""This file is to print of triangle of numbers"""

import sys

if len(sys.argv) > 1:
    print("The first input argument was: " + sys.argv[1])

k = 0  # Initial value
for i in range(int(sys.argv[1])):
    for j in range(i+1):
        k += 1
        print(k, end=" ")
    print("")
