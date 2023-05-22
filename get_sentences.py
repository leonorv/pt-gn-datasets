'''
Sentence tokenizer for any file
- used for DIP and Publico datasets
This script shuffles the obtained lines
'''
import random
from nltk import tokenize

#new = open("./publico/publico_raw_sentences.txt", "w+")
#with open("./publico/publico94.txt") as f:
new = open("./dip/dip_raw_sentences.txt", "w+")
with open("./dip/dip_raw_random_20000.txt") as f:
        lines = f.readlines()
        random.shuffle(lines)

        for line in lines:
                
            for sentence in tokenize.sent_tokenize(line):
                  if sentence.strip():
                    new.write(sentence)
                    new.write('\n')
new.close()