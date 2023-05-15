'''
This script extracts the tweets column. It does not clean or randomize the entries.
'''

import pandas as pd

df = pd.read_csv('./twitter/NoThemeTweets.csv')

with open("./twitter/twitter_raw.txt", "w") as f_out:
    f_out.write("\n".join(df["tweet_text"]))
