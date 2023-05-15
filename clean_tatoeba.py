'''
Tatoeba is a short, simple, sentences dataset. This script cleans the number and language tag at the start of each line.
This script shuffles the obtained lines.
'''
import random

tatoeba = open("./tatoeba/por_sentences.tsv", "r")
new = open("./tatoeba/tatoeba_clean_big.txt", "w+")

lines = tatoeba.readlines()
random.shuffle(lines)
for line in lines:
    new.write(line.lstrip(' \t0123456789')[4:])
new.close()
tatoeba.close()