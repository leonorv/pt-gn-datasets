# pt-gn-datasets
This repository contains the parallel datasets created by the rule-based model hosted on https://github.com/leonorv/pt-gender-neutralizer/. 
Please refer to that repository for more information on the project as a whole.

Each of the clean_X.py script perform the cleaning described in the section **Data Cleaning**.

The **dev_5k** folder contains 5k sentences from each of the data categories, for development purposes. The **rbm_5k** folder contains the gender-neutral version of the sentences from the **dev_5k** files. These 2 folders are a parallel dataset, where the binary-gendered version is on the **dev_5k** files, and the gender-neutral version as outputed by our rule-based model is in the **rbm_5k** files. 

The **gendered_annotation** folder contains an extra 100 sentences from each category, for manual annotation purposes.

# Categories
The dataset is split into 5 categories of textual data:
- **Literary:** We used a random sample of sentences from random works found in the DIP collection (https://www.linguateca.pt/aval_conjunta/dip/colecao.html). The raw data can be found in the **dip** folder.
- **Journalistic:** We used a random sample of sentences found in the NaturaPublico94 dataset, found in the Projecto Natura page (https://natura.di.uminho.pt/~jj/pln/corpora/NaturaPublico94). The raw data can be found in the **publico** folder.
- **Dialogues:** We used a random sample of extracted sentences from the subTle corpus (https://www.inesc-id.pt/ficheiros/publicacoes/10062.pdf). The raw data can be found in the **subtle** folder.
- **Social Media:** We used a random sample of tweets from Portuguese Tweets for Sentiment Analysis (https://www.kaggle.com/datasets/augustop/portuguese-tweets-for-sentiment-analysis). Only tweets without "theme" were selected. The raw data can be found in the **twitter** folder.
- **Simple Sentences:** We used a random sample from the portuguese Tatoeba dataset (https://tatoeba.org/pt-br/downloads). The raw data can be found in the **tatoeba** folder. 

# Data cleaning
All of the data categories went through a different cleaning process, due to their own specificities.

## Literary
We have removed:
- Tags (chapter indications, language tags, etc)
- Sentences that are one word or character long
- Author notes

## Journalistic
We have removed:
- Sentences that are too short (one or two characters long or only one word)
- Sentences that were mis-tokenized by NLTK

## Dialogues
We have extracted the dialogue text, ignoring speaker tags.

## Social Media
We have removed:
- Links
- Mentions
- Hashtags

## Simple sentences
No data cleaning was needed
