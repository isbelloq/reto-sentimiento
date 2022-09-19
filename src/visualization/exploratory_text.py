from nltk import FreqDist, ngrams
import pandas as pd

def top_frec(corpus: str, igram: int = 1, top: int = 10) -> pd.DataFrame:
    '''Extraccion de top n de frecuencias de un corpus'''

    corpus_ngram = ngrams(corpus.split(), igram)
    corpus_freq = FreqDist(corpus_ngram)
    corpus_df = pd.DataFrame(corpus_freq.most_common(top), columns = ['ngram', 'frec'])
    corpus_df['ngram'] = corpus_df['ngram'].str.join(' ')
    
    return corpus_df