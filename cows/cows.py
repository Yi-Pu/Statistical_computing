# Your driver code should go here
from crowded_cows import crowded_cows
import sys

# Get parameters
test_k = int(sys.argv[1])

# opening the file in read mode
my_file = open(str(sys.argv[2]), "r")

# reading the file
data = my_file.read()

# replacing end of line('/n') with ' ' and
# splitting the text it further when '.' is seen.
test_cows = data.split("\n")

# Print the output
print(crowded_cows(test_cows, k=test_k))

# Some other examples
print(
    "crowded_cows([7, 3, 4, 2, 3, 4], 3) = " +
    str(crowded_cows([7, 3, 4, 2, 3, 4], 3)))
print(
    "crowded_cows([7, 3, 4, 2, 3, 10, 4], 3)  = " +
    str(crowded_cows([7, 3, 4, 2, 3, 10, 4], 3)))
print(
    "crowded_cows([7, 3, 1, 0, 4, 2, 16, 28, 3, 4], 3) = " +
    str(crowded_cows([7, 3, 1, 0, 4, 2, 16, 28, 3, 4], 3)))
