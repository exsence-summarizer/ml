import spacy
from spacy.lang.en import STOP_WORDS as sw
from string import punctuation



def summarizeType2(text):
    # stopwords consists of all the words
    stopwords = list(sw) #converting into list for easier use

    nlp = spacy.load('en_core_web_sm')  #nlp - object of spacy
    doc = nlp(text)


    tokens = [token.text for token in doc] #creating tokens from doc
    print(tokens)
    #but this contains stop words and punctuations

    