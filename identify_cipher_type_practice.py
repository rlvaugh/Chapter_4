"""Load ciphertext & use fraction of ETAOIN present to classify cipher type."""
import sys
from collections import Counter

# set arbitrary cutoff fraction of 6-most common letters in English
# ciphertext with target fraction or greater = transposition cipher
CUTOFF = 0.5

# load ciphertext
def load(filename):
    """Open text file, check for errors, & make  list."""
    try:
        with open(filename) as my_file:
            my_list = my_file.read().strip()
            return my_list
    except IOError as e:
        print("Error opening {} {}. Terminating program.".format(filename, e),
              file=sys.stderr)
        sys.exit(1)

ciphertext = load('cipher_a.txt')

# count 6 most-common letters in ciphertext
six_most_frequent = Counter(ciphertext.lower()).most_common(6)
print("\nSix most-frequently-used letters in English = ETAOIN")
print('\nSix most frequent letters in ciphertext =')
print(*six_most_frequent, sep='\n')

# convert list of tuples to set of letters for comparison
cipher_top_6 = {i[0] for i in six_most_frequent}

TARGET = 'etaoin'
count = 0
for letter in TARGET:
    if letter in cipher_top_6:
        count += 1

if count/len(TARGET) >= CUTOFF:
    print("\nThis ciphertext most-likely produced by a TRANSPOSITION cipher")
else:
    print("This ciphertext most-likely produced by a SUBSTITUTION cipher") 
