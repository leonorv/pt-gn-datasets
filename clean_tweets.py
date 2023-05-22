'''
This script removes links, @s and #s from the twitter dataset. It does NOT shuffle lines.
'''
import re

twitter = open("./twitter/twitter_raw.txt", "r")
new = open("./twitter/twitter_clean_big.txt", "w+")

def remove_emoji_and_smile(string):
    emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F" # emoticons
        u"\U0001F300-\U0001F5FF" # symbols & pictographs
        u"\U0001F680-\U0001F6FF" # transport & map symbols
        u"\U0001F1E0-\U0001F1FF" # flags (iOS)
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        "]+", flags=re.UNICODE)
    smile_pattern = re.compile(":\)+")
    other_smile_pattern = re.compile("[:;][)(DP]")
    string = emoji_pattern.sub(r'', string)
    string = smile_pattern.sub(r'', string)
    string = other_smile_pattern.sub(r'', string)
    return string

lines = twitter.readlines()
for line in lines:
    string_without_links = re.sub(r'http\S+', '', line)
    new_line = ' '.join(filter(lambda word: not word.startswith(('@', '#')), string_without_links.split()))
    new.write(remove_emoji_and_smile(new_line) + '\n')
new.close()
twitter.close()