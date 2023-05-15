'''
DIP is a literary dataset. This script attempts to clean:
- tags (chapter indications, language tags, etc)
- sentences that are one word or character long
- author notes
'''

dip = open("./dip/dip_raw_sentences.txt", "r")
new = open("./dip/dip_clean_big.txt", "w+")

for line in dip.readlines():
    if line.startswith(('<', '[', '(')) or len(line.split()) <= 1:
        continue
    if line.startswith("-") or line[0].isalpha():
        new.write(line)
new.close()
dip.close()

