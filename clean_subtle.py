'''
BE SUBTLE is a dialogue corpus. This script extracts the dialogue lines according to the format provided by the dataset.
This script also shuffles the clean lines.
'''
import random
subtle = open("./subtle/por/subtle_100k.txt", "r")
new = open("./subtle/subtle_clean_big.txt", "w+")

lines = subtle.readlines()
random.shuffle(lines)
for i, line in enumerate(lines):
    if line.startswith(('I - ', 'R - ')):
        new.write(line[4:])
new.close()
subtle.close()
