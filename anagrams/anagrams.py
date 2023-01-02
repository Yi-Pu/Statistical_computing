# Your driver code (including input / output handling) should go here

import sys
from find_anagrams import find_anagrams

# opening the file in read mode
my_file = open(str(sys.argv[1]), "r")

# reading the file
data = my_file.read()

# replacing end of line('/n') with ' ' and
# splitting the text it further when '.' is seen.
test_worsds = data.split("\n")

anagrams = find_anagrams(test_worsds)

# open file in write mode
fp = open(
    '/Users/yipu/statistical_computing/anagrams-Yi-Pu/anagram sets2.txt',
    'w')
for item in anagrams:
    # write each item on a new line
    fp.write("%s\n" % item)
