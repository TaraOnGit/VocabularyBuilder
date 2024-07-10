import numpy as np
import pandas as pd

class FetchWords:
    def word_list(self):

        words_df = pd.read_csv('words_synonyms.csv')

        wordlist = list(words_df['Words']) + list(words_df['Synonym1']) + list(words_df['Synonym2'])
        wordlist = list(set(wordlist))

        return wordlist

    def get_synonyms(self,word):
        words_df = pd.read_csv('words_synonyms.csv')
        word = word

        temp_df = (words_df[words_df['Words'] == word])
        if (temp_df.shape[0] == 0):
            temp_df = (words_df[words_df['Synonym1'] == word])
            if (temp_df.shape[0] == 0):
                temp_df = (words_df[words_df['Synonym2'] == word])
                if (temp_df.shape[0] == 0):
                    return 'No Synonyms Found'
        if (temp_df.shape[0] != 0):
            return list(temp_df['Words'].values),list(temp_df['Synonym1'].values),list(temp_df['Synonym2'].values)

fw = FetchWords()
print(fw.get_synonyms('Abate'))
