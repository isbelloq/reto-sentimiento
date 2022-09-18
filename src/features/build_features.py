from typing import List
import pandas as pd
from src.features.processing_text import *

def processing_text_pipeline(df: pd.DataFrame, text_column: str, punctuation_string: str, stopwords: List[str]) -> pd.DataFrame:
    '''Funcion de preprosesamiento de texto'''
    prepros_df = df.copy()

    # Limpieza de texto
    prepros_df['pre_text'] = prepros_df[text_column].str.lower()
    prepros_df['pre_text'] = prepros_df['pre_text'].apply(tweet_clean)
    prepros_df['pre_text'] = prepros_df['pre_text'].apply(lambda x: remove_punctuation(x, punctuation_string))
    prepros_df['pre_text'] = prepros_df['pre_text'].apply(lambda x: remove_stopwords(x, stopwords))
    prepros_df['pre_text'] = prepros_df['pre_text'].apply(remove_numbers)

    # Homologacion
    prepros_df['pre_text'] = prepros_df['pre_text'].apply(homologacion_emoji)
    prepros_df['pre_text'] = prepros_df['pre_text'].apply(homologacion_diacriticos)

    return prepros_df