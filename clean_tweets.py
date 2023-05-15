'''
This script removes links, @s and #s from the twitter dataset. It does NOT shuffle lines.
'''
import re

twitter = open("./twitter/twitter_raw.txt", "r")
new = open("./twitter/twitter_clean_big.txt", "w+")

lines = twitter.readlines()
for line in lines:
    string_without_links = re.sub(r'http\S+', '', line)
    new_line = ' '.join(filter(lambda word: not word.startswith(('@', '#')), string_without_links.split()))
    new.write(new_line + '\n')
new.close()
twitter.close()