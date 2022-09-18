
from typing import List
import re
from string import punctuation
from emoji import demojize, is_emoji

def tag_by_regex(token: str, regex: str) -> bool:
    """Marcacion de un token que satisface una expresion regular"""
    if re.match(regex, token):
        return True
    else:
        return False

def tweet_clean(tweet:str) -> str:
    """Funcion de limpieza de tweets"""

    # Expresiones regulares
    regex_url = r'http(s)?://.+'
    regex_mention = r'@.+'

    clean_sentence = []

    for token in tweet.split():
        if (not tag_by_regex(token, regex_url)) and (not tag_by_regex(token, regex_mention)):
            clean_sentence.append(token)
    
    clean_sentence = ' '.join(clean_sentence)
    
    return clean_sentence

def remove_punctuation(text: str, punctuation_string: str = punctuation) -> str:
    """Funcion de eliminacion de simbolos de puntuacion"""
    text = re.sub(rf'[{punctuation_string}]', ' ', text)
    text = text.strip()
    return text

def homologacion_emoji(tweet:str) -> str:
    '''Funcion que emplaza los emoji por texto'''
    # Identificacion de emojis
    emoji_set = set()
    for i in tweet:
        if is_emoji(i):
            emoji_set.add(i)

    # Reemplazo de emoji por texto
    for emoji in emoji_set:
        tweet = tweet.replace(emoji, f' {demojize(emoji)} ')
    tweet = re.sub(r' +', r' ', tweet)
    tweet = tweet.strip()

    return tweet
    
def homologacion_diacriticos(text: str) -> str:
    '''Funcion que elimina los acsentos diacriticos'''
    text = re.sub('á','a', text)
    text = re.sub('à','a', text)
    text = re.sub('é','e', text)
    text = re.sub('è','e', text)
    text = re.sub('í','i', text)
    text = re.sub('ì','i', text)
    text = re.sub('ó','o', text)
    text = re.sub('ò','o', text)
    text = re.sub('ú','u', text)
    text = re.sub('ù','u', text)
    text = re.sub('ü','u', text)
    return text

def remove_stopwords(sentences: str, stopwords: List[str]) -> str:
    '''Eliminacion  de stopwords'''
    sentences_no_sw = [word for word in sentences.split() if word not in stopwords]
    sentences_no_sw = ' '.join(sentences_no_sw)
    return sentences_no_sw

def remove_numbers(sentences: str):
    clean_sentences = re.sub(r'[0-9]', ' ', sentences)
    clean_sentences = re.sub(r' +', r' ', clean_sentences)
    clean_sentences = clean_sentences.strip()

    return clean_sentences