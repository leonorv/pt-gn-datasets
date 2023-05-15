'''
Publico is a journalistic dataset. This script attempts to clean:
- sentences that are too short (one or two characters long or only one word)
- sentences that were mis-tokenized by the get_sentences.py script
'''

publico = open("./publico/publico_raw_sentences.txt", "r")
new = open("./publico/publico_clean_big.txt", "w+")

for line in publico.readlines():
    if line.startswith(('<', '[', '(', ')')) or len(line.split()) <= 1 or len(line) <= 2:
        continue
    new.write(line)
new.close()
publico.close()