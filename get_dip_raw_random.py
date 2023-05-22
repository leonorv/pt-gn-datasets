'''
DIP is a literary dataset. This script selects random lines from all works in the folder, checks if the lines are empty, and creates a new file.
This script does NOT generate a clean dataset.
'''
import random
import os
import glob

def get_nonempty_lines(file_path):
    with open(file_path) as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]
    return lines

def get_all_nonempty_lines(file_paths):
    all_lines = []
    for file_path in file_paths:
        all_lines.extend(get_nonempty_lines(file_path))
    return all_lines

#file_paths = glob.glob("./dip/*")
file_paths = ["./dip/obra000.txt", "./dip/obra005.txt", "./dip/obra007.txt", "./dip/obra019.txt", "./dip/obra024.txt", "./dip/obra039.txt", "./dip/obra049.txt", "./dip/obra056.txt", "./dip/obra065.txt", "./dip/obra078.txt", "./dip/obra086.txt", "./dip/obra090.txt", "./dip/obra091.txt", "./dip/obra093.txt","./dip/obra096.txt" ]
all_lines = get_all_nonempty_lines(file_paths)
total_lines = len(all_lines)
print(total_lines)

line_numbers = random.sample(range(total_lines), 20000)
random_lines = [all_lines[i] for i in line_numbers]

with open('./dip/dip_raw_20000.txt', 'w') as f:
    f.write('\n'.join(random_lines))